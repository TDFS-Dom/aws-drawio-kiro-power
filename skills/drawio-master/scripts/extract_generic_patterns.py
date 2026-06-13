#!/usr/bin/env python3
"""
Generic Pattern Extractor — Deduplicate and normalize patterns into generic templates.

Instead of 994 raw styles, produce a concise catalog of GENERIC patterns:
- Edges: ~15 generic types (solid/dashed × color × width × arrow)
- Containers: ~10 generic types (account, region, VPC, on-prem, dashed box, swimlane)
- Icons: ~8 generic types (per AWS category color)
- Text: ~5 generic types (title, label, annotation, edge-label)

Usage:
    python3 extract_generic_patterns.py <folder> --output generic-patterns.md
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
from collections import defaultdict


def extract_all_styles(folder_path):
    """Extract all styles from all .drawio files."""
    edges = []
    containers = []
    icons = []
    text_styles = []
    other = []

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
            sheet = diagram.get("name", "")
            model = diagram.find("mxGraphModel")
            if model is None:
                continue
            for cell in model.iter("mxCell"):
                style = cell.get("style", "")
                if not style:
                    continue
                value = (cell.get("value", "") or "")[:60]
                is_edge = cell.get("edge") == "1"

                if is_edge:
                    edges.append(style)
                elif "shape=mxgraph.aws4.group" in style:
                    containers.append(style)
                elif "dashed=1" in style and "fillColor=none" in style and "strokeColor=#5A6C86" in style:
                    containers.append(style)
                elif "mxgraph.aws4" in style:
                    icons.append(style)
                elif "text;" in style or ("strokeColor=none" in style and "fillColor=none" in style):
                    text_styles.append(style)
                elif "swimlane" in style:
                    other.append(style)
                else:
                    other.append(style)

    return edges, containers, icons, text_styles, other


def normalize_edge(style):
    """Extract generic properties from an edge style."""
    props = {}
    props["dashed"] = "1" if "dashed=1" in style else "0"
    props["arrow"] = "none" if ("endArrow=none" in style or "endFill=0" in style) else "classic"

    m = re.search(r"strokeWidth=(\d+)", style)
    props["width"] = m.group(1) if m else "1"

    m = re.search(r"strokeColor=(#[0-9a-fA-F]+)", style)
    props["color"] = m.group(1) if m else "default"

    m = re.search(r"fillColor=(#[0-9a-fA-F]+)", style)
    props["fill"] = m.group(1) if m and m.group(1) not in ("none", "#FFFFFF", "#ffffff") else ""

    props["has_shape_link"] = "1" if "shape=link" in style else "0"

    return tuple(sorted(props.items()))


def normalize_container(style):
    """Extract generic properties from a container style."""
    m = re.search(r"grIcon=mxgraph\.aws4\.([^;]+)", style)
    gr_icon = m.group(1) if m else "none"

    m = re.search(r"strokeColor=(#[0-9a-fA-F]+)", style)
    stroke = m.group(1) if m else "default"

    dashed = "1" if "dashed=1" in style else "0"

    return (gr_icon, stroke, dashed)


def normalize_icon(style):
    """Extract generic properties from an icon style."""
    # resIcon type
    m = re.search(r"resIcon=mxgraph\.aws4\.([^;]+)", style)
    res_icon = m.group(1) if m else ""

    # shape (for standalone)
    m = re.search(r"shape=mxgraph\.aws4\.([^;]+)", style)
    shape = m.group(1) if m else ""

    # fillColor
    m = re.search(r"fillColor=(#[0-9a-fA-F]+)", style)
    fill = m.group(1) if m else ""

    # gradientColor
    m = re.search(r"gradientColor=(#[0-9a-fA-F]+)", style)
    gradient = m.group(1) if m else ""

    # strokeColor
    m = re.search(r"strokeColor=(#[0-9a-fA-F]+|none)", style)
    stroke = m.group(1) if m else ""

    return (fill, gradient, stroke, "resourceIcon" if res_icon else "standalone")


def build_generic_md(edges, containers, icons, text_styles, other):
    """Build generic patterns markdown."""
    lines = []
    lines.append("# Generic Patterns Catalog")
    lines.append("")
    lines.append("> Normalized from 994 raw styles into reusable generic templates.")
    lines.append("> AI picks the matching pattern, fills in placeholders, done.")
    lines.append("")

    # ═══ EDGES ═══
    lines.append("## 1. EDGE PATTERNS")
    lines.append("")

    edge_groups = defaultdict(int)
    edge_examples = {}
    for style in edges:
        key = normalize_edge(style)
        edge_groups[key] += 1
        if key not in edge_examples:
            edge_examples[key] = style

    lines.append(f"**{len(edge_groups)} generic edge patterns** (from {len(edges)} total)")
    lines.append("")
    lines.append("| # | Type | Color | Width | Arrow | Dashed | Count | Use When |")
    lines.append("|---|---|---|---|---|---|---|---|")

    sorted_edges = sorted(edge_groups.items(), key=lambda x: -x[1])
    for i, (key, count) in enumerate(sorted_edges, 1):
        props = dict(key)
        etype = "link" if props.get("has_shape_link") == "1" else "standard"
        use_when = ""
        color = props["color"]
        if color == "#D79B00" or color == "#d79b00":
            use_when = "Network/DX connectivity"
        elif color == "#82B366" or color == "#82b366":
            use_when = "Prod shared services"
        elif color == "#6c8ebf":
            use_when = "NonProd shared services"
        elif color == "#CD2264":
            use_when = "Account/security flow"
        elif color == "#8C4FFF":
            use_when = "Networking service flow"
        elif color == "#C7131F":
            use_when = "Security finding flow"
        elif color == "#BC1356":
            use_when = "Management/replication"
        elif color == "#ED7100":
            use_when = "Compute/Lambda"
        elif color == "#C925D1":
            use_when = "DevTools/Pipeline"
        elif color == "#33FF33":
            use_when = "Integration/data link"
        elif color == "#DD344C":
            use_when = "Security/IAM dependency"
        elif color == "default":
            use_when = "Hierarchy/default"

        lines.append(f"| {i} | {etype} | `{color}` | {props['width']} | {props['arrow']} | {'yes' if props['dashed']=='1' else 'no'} | {count} | {use_when} |")

    lines.append("")
    lines.append("### Edge Templates (copy-paste)")
    lines.append("")

    # Output top 15 most-used patterns
    for i, (key, count) in enumerate(sorted_edges[:15], 1):
        props = dict(key)
        lines.append(f"#### E{i}: {props['color']} | width={props['width']} | {'dashed' if props['dashed']=='1' else 'solid'} | {'no-arrow' if props['arrow']=='none' else 'arrow'} (used {count}x)")
        lines.append("```")
        lines.append(edge_examples[key])
        lines.append("```")
        lines.append("")

    # ═══ CONTAINERS ═══
    lines.append("---")
    lines.append("")
    lines.append("## 2. CONTAINER PATTERNS")
    lines.append("")

    container_groups = defaultdict(int)
    container_examples = {}
    for style in containers:
        key = normalize_container(style)
        container_groups[key] += 1
        if key not in container_examples:
            container_examples[key] = style

    lines.append(f"**{len(container_groups)} generic container patterns** (from {len(containers)} total)")
    lines.append("")
    lines.append("| # | grIcon | strokeColor | Dashed | Count | Use When |")
    lines.append("|---|---|---|---|---|---|")

    sorted_containers = sorted(container_groups.items(), key=lambda x: -x[1])
    for i, (key, count) in enumerate(sorted_containers, 1):
        gr_icon, stroke, dashed = key
        use_when = ""
        if "group_account" in gr_icon:
            use_when = "AWS Account boundary"
        elif "group_region" in gr_icon:
            use_when = "Region boundary"
        elif "group_vpc2" in gr_icon:
            use_when = "VPC boundary"
        elif "corporate_data_center" in gr_icon:
            use_when = "On-premise DC"
        elif "group_on_premise" in gr_icon:
            use_when = "On-premise generic"
        elif "security_group" in gr_icon:
            use_when = "Security group / subnet"
        elif "step_functions" in gr_icon:
            use_when = "Step Functions workflow"
        elif gr_icon == "none":
            use_when = "Dashed boundary box (OU grouping)"

        lines.append(f"| {i} | `{gr_icon}` | `{stroke}` | {'yes' if dashed=='1' else 'no'} | {count} | {use_when} |")

    lines.append("")
    lines.append("### Container Templates (copy-paste)")
    lines.append("")

    for i, (key, count) in enumerate(sorted_containers, 1):
        gr_icon, stroke, dashed = key
        lines.append(f"#### C{i}: {gr_icon} (used {count}x)")
        lines.append("```")
        lines.append(container_examples[key])
        lines.append("```")
        lines.append("")

    # ═══ ICONS ═══
    lines.append("---")
    lines.append("")
    lines.append("## 3. ICON PATTERNS (by category color)")
    lines.append("")

    icon_groups = defaultdict(int)
    icon_examples = {}
    for style in icons:
        key = normalize_icon(style)
        icon_groups[key] += 1
        if key not in icon_examples:
            icon_examples[key] = style

    lines.append(f"**{len(icon_groups)} generic icon patterns** (from {len(icons)} total)")
    lines.append("")
    lines.append("| # | fillColor | gradient | strokeColor | Type | Count |")
    lines.append("|---|---|---|---|---|---|")

    sorted_icons = sorted(icon_groups.items(), key=lambda x: -x[1])
    for i, (key, count) in enumerate(sorted_icons, 1):
        fill, gradient, stroke, icon_type = key
        lines.append(f"| {i} | `{fill}` | `{gradient or '—'}` | `{stroke}` | {icon_type} | {count} |")

    lines.append("")
    lines.append("### Icon Templates (copy-paste, top 15)")
    lines.append("")

    for i, (key, count) in enumerate(sorted_icons[:15], 1):
        fill, gradient, stroke, icon_type = key
        lines.append(f"#### I{i}: fill={fill} | {icon_type} (used {count}x)")
        lines.append("```")
        lines.append(icon_examples[key])
        lines.append("```")
        lines.append("")

    # ═══ TEXT ═══
    lines.append("---")
    lines.append("")
    lines.append("## 4. TEXT PATTERNS")
    lines.append("")

    # Deduplicate text by key properties
    text_dedup = {}
    for style in text_styles:
        m = re.search(r"fontSize=(\d+)", style)
        fs = m.group(1) if m else "12"
        bold = "1" if "fontStyle=1" in style else "0"
        key = (fs, bold)
        if key not in text_dedup:
            text_dedup[key] = style

    lines.append(f"**{len(text_dedup)} generic text patterns**")
    lines.append("")
    lines.append("| # | fontSize | Bold | Template |")
    lines.append("|---|---|---|---|")

    for i, ((fs, bold), style) in enumerate(sorted(text_dedup.items(), key=lambda x: -int(x[0][0])), 1):
        lines.append(f"| T{i} | {fs} | {'yes' if bold=='1' else 'no'} | (see below) |")

    lines.append("")
    for i, ((fs, bold), style) in enumerate(sorted(text_dedup.items(), key=lambda x: -int(x[0][0])), 1):
        lines.append(f"#### T{i}: fontSize={fs}, bold={'yes' if bold=='1' else 'no'}")
        lines.append("```")
        lines.append(style)
        lines.append("```")
        lines.append("")

    # ═══ OTHER ═══
    lines.append("---")
    lines.append("")
    lines.append("## 5. OTHER SHAPE PATTERNS")
    lines.append("")

    # Classify by shape type
    other_types = defaultdict(list)
    for style in other:
        if "swimlane" in style:
            other_types["swimlane"].append(style)
        elif "rounded=0" in style and "whiteSpace=wrap" in style:
            other_types["rectangle"].append(style)
        elif "rounded=1" in style:
            other_types["rounded_rect"].append(style)
        elif "shape=image" in style:
            other_types["image"].append(style)
        elif "ellipse" in style:
            other_types["ellipse"].append(style)
        else:
            other_types["misc"].append(style)

    for stype, styles in sorted(other_types.items()):
        lines.append(f"### {stype} ({len(styles)} variants)")
        lines.append("")
        # Show 1 representative
        lines.append("```")
        lines.append(styles[0])
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_generic_patterns.py <folder> [--output file.md]")
        sys.exit(1)

    folder = sys.argv[1]
    output = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None

    edges, containers, icons, text_styles, other = extract_all_styles(folder)
    md = build_generic_md(edges, containers, icons, text_styles, other)

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ Written to: {output}")
    else:
        print(md)
