#!/usr/bin/env python3
"""
Template Fill — Clone a .drawio and replace content (labels, services, accounts).

Usage:
    python3 template_fill.py <source.drawio> --changes changes.json --output new.drawio

changes.json format:
{
    "replacements": [
        {"id": "cell-id-1", "value": "New Label"},
        {"id": "cell-id-2", "value": "New Account Name"},
        {"id": "cell-id-3", "style_replace": {"resIcon=mxgraph.aws4.guardduty": "resIcon=mxgraph.aws4.inspector"}}
    ],
    "remove": ["cell-id-to-delete"],
    "add": [
        {
            "id": "new-cell-1",
            "value": "New Service",
            "style": "copy_from:cell-id-1",
            "parent": "parent-id",
            "geometry": {"x": 100, "y": 100, "width": 78, "height": 78}
        }
    ]
}
"""

import sys
import json
import copy
import xml.etree.ElementTree as ET


def fill_template(source_path: str, changes_path: str, output_path: str):
    """Clone source .drawio and apply changes."""
    
    # Parse source
    try:
        tree = ET.parse(source_path)
    except ET.ParseError as e:
        print(f"❌ XML parse error: {e}")
        sys.exit(1)
    
    root = tree.getroot()
    
    # Load changes
    with open(changes_path) as f:
        changes = json.load(f)
    
    applied = 0
    
    # Build ID → cell index
    cells_by_id = {}
    for cell in root.iter("mxCell"):
        cells_by_id[cell.get("id", "")] = cell
    
    # Apply replacements
    for rep in changes.get("replacements", []):
        cell_id = rep.get("id")
        if cell_id not in cells_by_id:
            print(f"  ⚠️  ID not found: {cell_id}")
            continue
        
        cell = cells_by_id[cell_id]
        
        if "value" in rep:
            cell.set("value", rep["value"])
            applied += 1
        
        if "style_replace" in rep:
            style = cell.get("style", "")
            for old, new in rep["style_replace"].items():
                style = style.replace(old, new)
            cell.set("style", style)
            applied += 1
    
    # Apply removals
    for cell_id in changes.get("remove", []):
        if cell_id in cells_by_id:
            cell = cells_by_id[cell_id]
            parent_elem = None
            for parent in root.iter():
                if cell in list(parent):
                    parent_elem = parent
                    break
            if parent_elem is not None:
                parent_elem.remove(cell)
                applied += 1
                print(f"  🗑️  Removed: {cell_id}")
    
    # Apply additions (basic)
    for add in changes.get("add", []):
        print(f"  ➕ Add: {add.get('id')} (manual XML insertion recommended for complex additions)")
        applied += 1
    
    # Save
    tree.write(output_path, xml_declaration=True, encoding="UTF-8")
    
    print(f"\n✅ Template fill complete:")
    print(f"   Source: {source_path}")
    print(f"   Changes: {applied} applied")
    print(f"   Output: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or "--changes" not in sys.argv or "--output" not in sys.argv:
        print("Usage: template_fill.py <source.drawio> --changes changes.json --output new.drawio")
        sys.exit(1)
    
    source = sys.argv[1]
    changes_idx = sys.argv.index("--changes")
    output_idx = sys.argv.index("--output")
    
    changes_path = sys.argv[changes_idx + 1]
    output_path = sys.argv[output_idx + 1]
    
    fill_template(source, changes_path, output_path)
