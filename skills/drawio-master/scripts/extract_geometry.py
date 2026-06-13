#!/usr/bin/env python3
"""
Geometry Extractor — Analyze actual spacing, sizes, and positions from reference .drawio files.

Produces:
- Container actual sizes (min/max/avg)
- Icon sizes used
- Spacing between icons (horizontal & vertical)
- Padding inside containers (top, left, right, bottom)
- Icon-to-container-boundary margins

Usage:
    python3 extract_geometry.py <folder> --output geometry-rules.md
"""

import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
import statistics


def extract_geometry(folder_path):
    """Extract geometry data from all .drawio files."""
    
    containers = []  # {id, x, y, w, h, style, parent, sheet}
    icons = []       # {id, x, y, w, h, style, parent, sheet, value}
    edges = []       # {id, style, source, target, waypoints, sheet}
    
    all_cells = {}   # id → {x,y,w,h,parent}
    
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
                cid = cell.get("id", "")
                style = cell.get("style", "")
                parent = cell.get("parent", "")
                value = (cell.get("value", "") or "")[:60]
                is_edge = cell.get("edge") == "1"
                
                geom = cell.find("mxGeometry")
                if geom is None:
                    continue
                
                x = float(geom.get("x", 0) or 0)
                y = float(geom.get("y", 0) or 0)
                w = float(geom.get("width", 0) or 0)
                h = float(geom.get("height", 0) or 0)
                
                all_cells[cid] = {"x": x, "y": y, "w": w, "h": h, "parent": parent}
                
                if is_edge:
                    # Count waypoints
                    arr = geom.find("Array")
                    wp_count = len(list(arr)) if arr is not None else 0
                    edges.append({"id": cid, "style": style, "waypoints": wp_count, "sheet": sheet})
                elif "shape=mxgraph.aws4.group" in style or ("dashed=1" in style and "fillColor=none" in style):
                    containers.append({"id": cid, "x": x, "y": y, "w": w, "h": h, "style": style, "parent": parent, "sheet": sheet})
                elif "mxgraph.aws4" in style and w > 0:
                    icons.append({"id": cid, "x": x, "y": y, "w": w, "h": h, "style": style, "parent": parent, "sheet": sheet, "value": value})
    
    return containers, icons, edges, all_cells


def analyze_containers(containers):
    """Analyze container sizes."""
    widths = [c["w"] for c in containers if c["w"] > 0]
    heights = [c["h"] for c in containers if c["h"] > 0]
    
    # Group by type
    types = defaultdict(list)
    for c in containers:
        if "group_account" in c["style"]:
            types["account"].append(c)
        elif "group_region" in c["style"]:
            types["region"].append(c)
        elif "group_vpc" in c["style"]:
            types["vpc"].append(c)
        elif "group_security_group" in c["style"]:
            types["subnet"].append(c)
        elif "group_corporate" in c["style"] or "group_on_premise" in c["style"]:
            types["onprem"].append(c)
        elif "dashed=1" in c["style"]:
            types["dashed_box"].append(c)
        else:
            types["other"].append(c)
    
    return types, widths, heights


def analyze_icon_spacing(icons, all_cells):
    """Analyze spacing between icons."""
    # Group icons by parent container
    by_parent = defaultdict(list)
    for icon in icons:
        by_parent[icon["parent"]].append(icon)
    
    h_gaps = []  # horizontal gaps between adjacent icons
    v_gaps = []  # vertical gaps between adjacent icons
    
    for parent_id, icon_list in by_parent.items():
        if len(icon_list) < 2:
            continue
        
        # Sort by x then y
        sorted_x = sorted(icon_list, key=lambda i: (i["y"], i["x"]))
        
        for i in range(len(sorted_x) - 1):
            a = sorted_x[i]
            b = sorted_x[i + 1]
            
            # Same row (similar y)?
            if abs(a["y"] - b["y"]) < 20:
                gap = b["x"] - (a["x"] + a["w"])
                if 0 < gap < 200:
                    h_gaps.append(gap)
            # Same column (similar x)?
            elif abs(a["x"] - b["x"]) < 20:
                gap = b["y"] - (a["y"] + a["h"])
                if 0 < gap < 200:
                    v_gaps.append(gap)
            else:
                # Different row, measure vertical
                gap = b["y"] - (a["y"] + a["h"])
                if 0 < gap < 300:
                    v_gaps.append(gap)
    
    return h_gaps, v_gaps


def analyze_icon_padding(icons, containers, all_cells):
    """Analyze padding between icons and their parent container edges."""
    left_pads = []
    top_pads = []
    right_pads = []
    bottom_pads = []
    
    container_map = {c["id"]: c for c in containers}
    
    for icon in icons:
        parent_id = icon["parent"]
        if parent_id not in container_map:
            continue
        
        parent = container_map[parent_id]
        
        # Padding from left edge
        left_pad = icon["x"]
        if 0 < left_pad < 200:
            left_pads.append(left_pad)
        
        # Padding from top edge
        top_pad = icon["y"]
        if 0 < top_pad < 200:
            top_pads.append(top_pad)
        
        # Padding from right edge
        right_pad = parent["w"] - (icon["x"] + icon["w"])
        if 0 < right_pad < 500:
            right_pads.append(right_pad)
        
        # Padding from bottom edge
        bottom_pad = parent["h"] - (icon["y"] + icon["h"])
        if 0 < bottom_pad < 500:
            bottom_pads.append(bottom_pad)
    
    return left_pads, top_pads, right_pads, bottom_pads


def analyze_icon_sizes(icons):
    """Analyze icon dimensions used."""
    sizes = defaultdict(int)
    for icon in icons:
        size = f"{int(icon['w'])}x{int(icon['h'])}"
        sizes[size] += 1
    return dict(sorted(sizes.items(), key=lambda x: -x[1]))


def format_stats(values, label):
    """Format statistics for a list of values."""
    if not values:
        return f"{label}: no data"
    return f"{label}: min={min(values):.0f}, max={max(values):.0f}, avg={statistics.mean(values):.0f}, median={statistics.median(values):.0f} (n={len(values)})"


def build_report(containers, icons, edges, all_cells):
    """Build the geometry rules report."""
    lines = []
    lines.append("# Geometry Rules (Extracted from Reference Diagrams)")
    lines.append("")
    lines.append("> Auto-generated from 4 .drawio files. These are ACTUAL measurements, not estimates.")
    lines.append("> Use these numbers in SKILL.md for spacing calculations.")
    lines.append("")
    
    # Container sizes by type
    types, widths, heights = analyze_containers(containers)
    
    lines.append("## 1. Container Sizes (actual)")
    lines.append("")
    lines.append(f"Total containers analyzed: {len(containers)}")
    lines.append("")
    lines.append("| Type | Count | Width (min/avg/max) | Height (min/avg/max) |")
    lines.append("|---|---|---|---|")
    
    for tname, tlist in sorted(types.items(), key=lambda x: -len(x[1])):
        ws = [c["w"] for c in tlist if c["w"] > 0]
        hs = [c["h"] for c in tlist if c["h"] > 0]
        if ws and hs:
            lines.append(f"| {tname} | {len(tlist)} | {min(ws):.0f} / {statistics.mean(ws):.0f} / {max(ws):.0f} | {min(hs):.0f} / {statistics.mean(hs):.0f} / {max(hs):.0f} |")
    
    lines.append("")
    
    # Icon sizes
    lines.append("## 2. Icon Sizes (actual)")
    lines.append("")
    icon_sizes = analyze_icon_sizes(icons)
    lines.append("| Size (WxH) | Count | Usage |")
    lines.append("|---|---|---|")
    for size, count in list(icon_sizes.items())[:15]:
        lines.append(f"| {size} | {count} | {'primary' if count > 50 else 'secondary' if count > 10 else 'rare'} |")
    lines.append("")
    
    # Spacing between icons
    h_gaps, v_gaps = analyze_icon_spacing(icons, all_cells)
    
    lines.append("## 3. Spacing Between Icons (actual)")
    lines.append("")
    if h_gaps:
        lines.append(f"**Horizontal gaps**: min={min(h_gaps):.0f}, avg={statistics.mean(h_gaps):.0f}, median={statistics.median(h_gaps):.0f}, max={max(h_gaps):.0f} (n={len(h_gaps)})")
    else:
        lines.append("**Horizontal gaps**: insufficient data")
    lines.append("")
    if v_gaps:
        lines.append(f"**Vertical gaps**: min={min(v_gaps):.0f}, avg={statistics.mean(v_gaps):.0f}, median={statistics.median(v_gaps):.0f}, max={max(v_gaps):.0f} (n={len(v_gaps)})")
    else:
        lines.append("**Vertical gaps**: insufficient data")
    lines.append("")
    
    # Padding
    left_pads, top_pads, right_pads, bottom_pads = analyze_icon_padding(icons, containers, all_cells)
    
    lines.append("## 4. Icon-to-Container Padding (actual)")
    lines.append("")
    lines.append("| Edge | Min | Avg | Median | Max | N |")
    lines.append("|---|---|---|---|---|---|")
    for label, pads in [("Left", left_pads), ("Top", top_pads), ("Right", right_pads), ("Bottom", bottom_pads)]:
        if pads:
            lines.append(f"| {label} | {min(pads):.0f} | {statistics.mean(pads):.0f} | {statistics.median(pads):.0f} | {max(pads):.0f} | {len(pads)} |")
        else:
            lines.append(f"| {label} | — | — | — | — | 0 |")
    lines.append("")
    
    # Summary for SKILL.md
    lines.append("## 5. RECOMMENDED VALUES (for SKILL.md)")
    lines.append("")
    lines.append("Based on the actual measurements above:")
    lines.append("")
    lines.append("```")
    
    if h_gaps:
        lines.append(f"HORIZONTAL_GAP_BETWEEN_ICONS = {int(statistics.median(h_gaps))} px (median from {len(h_gaps)} measurements)")
    if v_gaps:
        lines.append(f"VERTICAL_GAP_BETWEEN_ICONS   = {int(statistics.median(v_gaps))} px (median from {len(v_gaps)} measurements)")
    if top_pads:
        lines.append(f"CONTAINER_TOP_PADDING        = {int(statistics.median(top_pads))} px (median from {len(top_pads)} measurements)")
    if left_pads:
        lines.append(f"CONTAINER_LEFT_PADDING       = {int(statistics.median(left_pads))} px (median from {len(left_pads)} measurements)")
    if right_pads:
        lines.append(f"CONTAINER_RIGHT_MARGIN       = {int(statistics.median(right_pads))} px (median)")
    if bottom_pads:
        lines.append(f"CONTAINER_BOTTOM_MARGIN      = {int(statistics.median(bottom_pads))} px (median)")
    
    most_common_size = list(icon_sizes.keys())[0] if icon_sizes else "78x78"
    lines.append(f"MOST_COMMON_ICON_SIZE        = {most_common_size} ({list(icon_sizes.values())[0] if icon_sizes else 0}x used)")
    
    lines.append("```")
    lines.append("")
    
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_geometry.py <folder> [--output geometry-rules.md]")
        sys.exit(1)
    
    folder = sys.argv[1]
    output = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
    
    print(f"Analyzing geometry from: {folder}")
    containers, icons, edges, all_cells = extract_geometry(folder)
    print(f"  Containers: {len(containers)}")
    print(f"  Icons: {len(icons)}")
    print(f"  Edges: {len(edges)}")
    
    report = build_report(containers, icons, edges, all_cells)
    
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n✅ Written to: {output}")
    else:
        print(report)
