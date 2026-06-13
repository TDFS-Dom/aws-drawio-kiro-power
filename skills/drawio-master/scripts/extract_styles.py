#!/usr/bin/env python3
"""
Style Extractor — Extract copy-paste ready style snippets PER SHEET from template .drawio files.

Usage:
    python3 extract_styles.py --all                    # Process all templates → sheets/ folder
    python3 extract_styles.py <template.drawio>        # Print summary to stdout
    python3 extract_styles.py <template.drawio> --sheet "HLD"   # Print single sheet

Output structure (per template folder):
    templates/{id}/
    ├── sheets/
    │   ├── 01_hld.md
    │   ├── 02_overall_prod_tgw_design.md
    │   └── ...
    └── sheets_index.md    # Quick lookup: sheet name → file

Each sheet file = 1 diagram pattern with exact copy-paste style strings.
AI reads ONLY the relevant sheet file at Step 3.
"""

import os
import sys
import re
import xml.etree.ElementTree as ET

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")


def slugify(name):
    """Convert sheet name to filename-safe slug."""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s


def extract_per_sheet(filepath):
    """Extract styles per sheet from a .drawio file."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    sheets = []

    for diagram in root.findall(".//diagram"):
        sheet_name = diagram.get("name", "Unnamed")
        model = diagram.find("mxGraphModel")
        if model is None:
            sheets.append({"name": sheet_name, "compressed": True, "containers": [], "icons": [], "edges": [], "other": []})
            continue

        containers = []
        icons = []
        edges = []
        other_shapes = []
        seen_styles = set()

        for cell in model.iter("mxCell"):
            style = cell.get("style", "")
            if not style or style in seen_styles:
                continue
            seen_styles.add(style)

            value = (cell.get("value", "") or "").replace("\n", " ")[:60]
            is_edge = cell.get("edge") == "1"
            cell_id = cell.get("id", "")

            geom = cell.find("mxGeometry")
            size = ""
            if geom is not None:
                w = geom.get("width", "")
                h = geom.get("height", "")
                if w and h:
                    size = f"{w}x{h}"

            entry = {"label": value or cell_id, "size": size, "style": style}

            if is_edge:
                edges.append(entry)
            elif "shape=mxgraph.aws4.group" in style or ("dashed=1" in style and "fillColor=none" in style):
                containers.append(entry)
            elif "mxgraph.aws4" in style or "shape=image" in style or "shape=mxgraph.mscae" in style:
                icons.append(entry)
            elif cell.get("vertex") == "1" and style:
                other_shapes.append(entry)

        sheets.append({
            "name": sheet_name,
            "compressed": False,
            "containers": containers,
            "icons": icons,
            "edges": edges,
            "other": other_shapes
        })

    return sheets


def format_sheet_md(sheet, sheet_num, source_file):
    """Format a single sheet as its own Markdown file."""
    lines = []
    lines.append(f"# Sheet {sheet_num}: {sheet['name']}")
    lines.append("")
    lines.append(f"> Source: `{source_file}` — sheet `{sheet['name']}`")
    lines.append("> Copy style strings EXACTLY when generating this pattern.")
    lines.append("")

    if sheet.get("compressed"):
        lines.append("(Compressed content — read from .drawio file directly)")
        return "\n".join(lines)

    total = len(sheet["containers"]) + len(sheet["icons"]) + len(sheet["edges"]) + len(sheet["other"])
    lines.append(f"**Elements**: {len(sheet['containers'])} containers, {len(sheet['icons'])} icons, {len(sheet['edges'])} edges, {len(sheet['other'])} other")
    lines.append("")

    if total == 0:
        lines.append("(Empty sheet)")
        return "\n".join(lines)

    # Containers
    if sheet["containers"]:
        lines.append("## Containers")
        lines.append("")
        for e in sheet["containers"]:
            lines.append(f"**{e['label']}** ({e['size']})")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    # Icons
    if sheet["icons"]:
        lines.append("## Icons")
        lines.append("")
        for e in sheet["icons"]:
            lines.append(f"**{e['label']}** ({e['size']})")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    # Edges
    if sheet["edges"]:
        lines.append("## Edges")
        lines.append("")
        for e in sheet["edges"]:
            lines.append(f"**{e['label']}**")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    # Other
    if sheet["other"]:
        lines.append("## Other Shapes")
        lines.append("")
        for e in sheet["other"]:
            lines.append(f"**{e['label']}** ({e['size']})")
            lines.append("```")
            lines.append(e["style"])
            lines.append("```")
            lines.append("")

    return "\n".join(lines)


def format_index_md(sheets, source_file):
    """Format the sheets index file."""
    lines = []
    lines.append(f"# Sheets Index — {source_file}")
    lines.append("")
    lines.append("> AI: read this file first, then load ONLY the sheet file you need.")
    lines.append("")
    lines.append(f"**Total: {len(sheets)} sheets**")
    lines.append("")
    lines.append("| # | Sheet Name | File | Containers | Icons | Edges |")
    lines.append("|---|---|---|---|---|---|")

    for i, sheet in enumerate(sheets, 1):
        slug = slugify(sheet["name"])
        fname = f"{i:02d}_{slug}.md"
        if sheet.get("compressed"):
            lines.append(f"| {i} | `{sheet['name']}` | `{fname}` | (compressed) | — | — |")
        else:
            lines.append(f"| {i} | `{sheet['name']}` | `{fname}` | {len(sheet['containers'])} | {len(sheet['icons'])} | {len(sheet['edges'])} |")

    lines.append("")
    return "\n".join(lines)


def process_all_templates():
    """Process all template folders — write per-sheet files into sheets/ folder."""
    processed = 0
    for folder_name in sorted(os.listdir(TEMPLATES_DIR)):
        folder_path = os.path.join(TEMPLATES_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue

        drawio_files = [f for f in os.listdir(folder_path) if f.endswith(".drawio")]
        if not drawio_files:
            continue

        drawio_path = os.path.join(folder_path, drawio_files[0])
        sheets_dir = os.path.join(folder_path, "sheets")
        os.makedirs(sheets_dir, exist_ok=True)

        print(f"  Processing: {folder_name}/{drawio_files[0]}")
        try:
            sheets = extract_per_sheet(drawio_path)

            # Write per-sheet files
            for i, sheet in enumerate(sheets, 1):
                slug = slugify(sheet["name"])
                fname = f"{i:02d}_{slug}.md"
                fpath = os.path.join(sheets_dir, fname)
                md = format_sheet_md(sheet, i, drawio_files[0])
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(md)

            # Write index
            index_path = os.path.join(folder_path, "sheets_index.md")
            index_md = format_index_md(sheets, drawio_files[0])
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(index_md)

            # Remove old monolithic styles.md if exists
            old_styles = os.path.join(folder_path, "styles.md")
            if os.path.exists(old_styles):
                os.remove(old_styles)

            total_styles = sum(
                len(s["containers"]) + len(s["icons"]) + len(s["edges"]) + len(s["other"])
                for s in sheets if not s.get("compressed")
            )
            print(f"    → sheets/ ({len(sheets)} files) + sheets_index.md")
            processed += 1
        except Exception as e:
            print(f"    ❌ Error: {e}")

    print(f"\n✅ Processed {processed} templates")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  extract_styles.py --all                         # Process all templates")
        print("  extract_styles.py <file.drawio>                 # Print summary")
        print("  extract_styles.py <file.drawio> --sheet 'HLD'   # Print single sheet")
        sys.exit(1)

    if sys.argv[1] == "--all":
        process_all_templates()
    else:
        filepath = sys.argv[1]
        sheets = extract_per_sheet(filepath)

        if "--sheet" in sys.argv:
            idx = sys.argv.index("--sheet")
            target = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
            for i, s in enumerate(sheets, 1):
                if s["name"] == target:
                    print(format_sheet_md(s, i, os.path.basename(filepath)))
                    break
            else:
                print(f"Sheet '{target}' not found. Available: {[s['name'] for s in sheets]}")
        else:
            print(format_index_md(sheets, os.path.basename(filepath)))
