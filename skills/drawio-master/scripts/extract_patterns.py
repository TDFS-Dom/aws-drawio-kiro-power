#!/usr/bin/env python3
"""
Pattern Extractor — Analyze all .drawio files and categorize ALL unique patterns.

Usage:
    python3 extract_patterns.py <folder_with_drawio_files> --output patterns.md

Categories:
- Edges (solid, dashed, colored, with/without arrows, with waypoints)
- Containers (accounts, regions, VPCs, on-prem, dashed boxes)
- AWS Icons (resourceIcon, standalone shapes, sub-resources)
- Text (titles, labels, annotations)
- Other shapes (rectangles, swimlanes, images)
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
from collections import defaultdict


def analyze_folder(folder_path):
    """Analyze all .drawio files in folder."""
    all_edges = {}
    all_containers = {}
    all_icons = {}
    all_text = {}
    all_other = {}

    for fname in sorted(os.listdir(folder_path)):
        if not fname.endswith(".drawio"):
            continue
        fpath = os.path.join(folder_path, fname)
        try:
            tree = ET.parse(fpath)
            root = tree.getroot()
        except ET.ParseError:
            continue

        for diagram in root.findall(".//diagram"):
            sheet_name = diagram.get("name", "Unnamed")
            model = diagram.find("mxGraphModel")
            if model is None:
                continue

            for cell in model.iter("mxCell"):
                style = cell.get("style", "")
                if not style:
                    continue

                value = (cell.get("value", "") or "").replace("\n", " ")[:80]
                is_edge = cell.get("edge") == "1"
                cell_id = cell.get("id", "")

                geom = cell.find("mxGeometry")
                size = ""
                if geom is not None:
                    w = geom.get("width", "")
                    h = geom.get("height", "")
                    if w and h:
                        size = f"{w}x{h}"

                # Check for waypoints
                has_waypoints = False
                if geom is not None:
                    arr = geom.find("Array")
                    if arr is not None and len(list(arr)) > 0:
                        has_waypoints = True

                source = cell.get("source", "")
                target = cell.get("target", "")

                key = style  # dedup by style

                entry = {
                    "style": style,
                    "label": value,
                    "size": size,
                    "source_file": fname,
                    "sheet": sheet_name,
                    "has_waypoints": has_waypoints,
                    "source_id": source,
                    "target_id": target,
                }

                if is_edge:
                    if key not in all_edges:
                        all_edges[key] = entry
                elif "shape=mxgraph.aws4.group" in style:
                    if key not in all_containers:
                        all_containers[key] = entry
                elif "dashed=1" in style and "fillColor=none" in style and "strokeColor=#5A6C86" in style:
                    if key not in all_containers:
                        all_containers[key] = entry
                elif "mxgraph.aws4" in style or "shape=mxgraph.mscae" in style:
                    if key not in all_icons:
                        all_icons[key] = entry
                elif "shape=image" in style:
                    if key not in all_other:
                        all_other[key] = entry
                elif "text;" in style or ("strokeColor=none" in style and "fillColor=none" in style and "align=" in style):
                    if key not in all_text:
                        all_text[key] = entry
                elif "swimlane" in style:
                    if key not in all_other:
                        all_other[key] = entry
                else:
                    if key not in all_other:
                        all_other[key] = entry

    return all_edges, all_containers, all_icons, all_text, all_other


def classify_edge(style):
    """Classify an edge into sub-category."""
    props = []
    if "dashed=1" in style:
        props.append("dashed")
    else:
        props.append("solid")

    if "endArrow=none" in style or "endFill=0" in style:
        props.append("no-arrow")
    elif "endArrow=classic" in style or "endArrow" not in style:
        props.append("arrow")

    # strokeWidth
    m = re.search(r"strokeWidth=(\d+)", style)
    if m:
        props.append(f"width={m.group(1)}")
    else:
        props.append("width=1")

    # strokeColor
    m = re.search(r"strokeColor=(#[0-9a-fA-F]+)", style)
    if m:
        props.append(f"color={m.group(1)}")

    # fillColor on edge (for thick colored)
    m = re.search(r"fillColor=(#[0-9a-fA-F]+)", style)
    if m and m.group(1) != "none":
        props.append(f"fill={m.group(1)}")

    return " | ".join(props)


def format_patterns_md(edges, containers, icons, text, other):
    """Format all patterns into a single comprehensive MD file."""
    lines = []
    lines.append("# Draw Patterns Catalog")
    lines.append("")
    lines.append("> Extracted from 4 reference .drawio files (43 sheets total).")
    lines.append("> These are ALL unique patterns found. Use ONLY these when generating diagrams.")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Category | Count |")
    lines.append(f"|---|---|")
    lines.append(f"| Edges | {len(edges)} |")
    lines.append(f"| Containers | {len(containers)} |")
    lines.append(f"| AWS Icons | {len(icons)} |")
    lines.append(f"| Text/Labels | {len(text)} |")
    lines.append(f"| Other Shapes | {len(other)} |")
    lines.append(f"| **Total** | **{len(edges)+len(containers)+len(icons)+len(text)+len(other)}** |")
    lines.append("")

    # ═══ EDGES ═══
    lines.append("---")
    lines.append("")
    lines.append("## 1. EDGES / LINES")
    lines.append("")
    lines.append(f"**{len(edges)} unique edge styles found.**")
    lines.append("")

    # Group by classification
    edge_groups = defaultdict(list)
    for key, entry in edges.items():
        classification = classify_edge(entry["style"])
        edge_groups[classification].append(entry)

    for classification, entries in sorted(edge_groups.items()):
        lines.append(f"### {classification} ({len(entries)} variants)")
        lines.append("")
        for e in entries[:5]:  # limit to 5 per group
            label = e["label"][:40] if e["label"] else e["sheet"]
            wp = " ⚡waypoints" if e["has_waypoints"] else ""
            lines.append(f"**{label}** (from `{e['sheet']}`){wp}")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")
        if len(entries) > 5:
            lines.append(f"_... and {len(entries)-5} more variants_")
            lines.append("")

    # ═══ CONTAINERS ═══
    lines.append("---")
    lines.append("")
    lines.append("## 2. CONTAINERS / GROUPS")
    lines.append("")
    lines.append(f"**{len(containers)} unique container styles found.**")
    lines.append("")

    for key, e in sorted(containers.items(), key=lambda x: x[1]["sheet"]):
        label = e["label"][:50] if e["label"] else "unlabeled"
        lines.append(f"**{label}** ({e['size']}) — from `{e['sheet']}`")
        lines.append("```")
        lines.append(e["style"])
        lines.append("```")
        lines.append("")

    # ═══ AWS ICONS ═══
    lines.append("---")
    lines.append("")
    lines.append("## 3. AWS ICONS")
    lines.append("")
    lines.append(f"**{len(icons)} unique icon styles found.**")
    lines.append("")

    # Sub-group: resourceIcon vs standalone
    resource_icons = []
    standalone_icons = []
    for key, e in icons.items():
        if "shape=mxgraph.aws4.resourceIcon" in e["style"]:
            resource_icons.append(e)
        else:
            standalone_icons.append(e)

    if resource_icons:
        lines.append(f"### Resource Icons ({len(resource_icons)})")
        lines.append("")
        for e in resource_icons:
            label = e["label"][:40] if e["label"] else "unlabeled"
            lines.append(f"**{label}** ({e['size']}) — from `{e['sheet']}`")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    if standalone_icons:
        lines.append(f"### Standalone / Sub-resource Icons ({len(standalone_icons)})")
        lines.append("")
        for e in standalone_icons:
            label = e["label"][:40] if e["label"] else "unlabeled"
            lines.append(f"**{label}** ({e['size']}) — from `{e['sheet']}`")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    # ═══ TEXT ═══
    lines.append("---")
    lines.append("")
    lines.append("## 4. TEXT / LABELS")
    lines.append("")
    lines.append(f"**{len(text)} unique text styles found.**")
    lines.append("")

    for key, e in list(text.items())[:20]:  # limit
        label = e["label"][:50] if e["label"] else "text element"
        lines.append(f"**{label}** ({e['size']}) — from `{e['sheet']}`")
        lines.append("```")
        lines.append(e["style"])
        lines.append("```")
        lines.append("")

    if len(text) > 20:
        lines.append(f"_... and {len(text)-20} more text styles_")
        lines.append("")

    # ═══ OTHER ═══
    lines.append("---")
    lines.append("")
    lines.append("## 5. OTHER SHAPES")
    lines.append("")
    lines.append(f"**{len(other)} unique other styles found.**")
    lines.append("")

    for key, e in list(other.items())[:20]:  # limit
        label = e["label"][:50] if e["label"] else "shape"
        lines.append(f"**{label}** ({e['size']}) — from `{e['sheet']}`")
        lines.append("```")
        lines.append(e["style"])
        lines.append("```")
        lines.append("")

    if len(other) > 20:
        lines.append(f"_... and {len(other)-20} more shapes_")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_patterns.py <folder> [--output patterns.md]")
        sys.exit(1)

    folder = sys.argv[1]
    output = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None

    print(f"Analyzing .drawio files in: {folder}")
    edges, containers, icons, text, other = analyze_folder(folder)
    print(f"  Edges: {len(edges)}")
    print(f"  Containers: {len(containers)}")
    print(f"  Icons: {len(icons)}")
    print(f"  Text: {len(text)}")
    print(f"  Other: {len(other)}")

    md = format_patterns_md(edges, containers, icons, text, other)

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"\n✅ Written to: {output}")
    else:
        print(md)
