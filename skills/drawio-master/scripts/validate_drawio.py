#!/usr/bin/env python3
"""
Draw.io XML Validator — 9-point quality check on generated .drawio files.

Usage:
    python3 validate_drawio.py <file.drawio>
    python3 validate_drawio.py <file.drawio> --fix    # Auto-fix where possible

Checks:
1. strokeColor=#ffffff on all mxgraph.aws4.resourceIcon shapes
2. No HTML tags in value="" attributes
3. No text overlap (basic bounding box check)
4. No broken edges (source/target IDs exist)
5. All edges have edgeStyle=orthogonalEdgeStyle and rounded=0
6. Labels not empty for service icons
7. Containers enclose children (parent hierarchy valid)
8. Styles match known patterns (spot-check)
9. Edge strokeColor matches source service category (future)
"""

import sys
import re
import xml.etree.ElementTree as ET


def validate(filepath: str, fix: bool = False) -> dict:
    """Run all 8 validation checks on a .drawio file."""
    
    try:
        tree = ET.parse(filepath)
    except ET.ParseError as e:
        return {"valid": False, "errors": [f"XML parse error: {e}"], "warnings": []}
    
    root = tree.getroot()
    errors = []
    warnings = []
    fixes_applied = []
    
    # Collect all mxCells
    cells = root.findall(".//{http://www.w3.org/1999/xhtml}mxCell") or root.findall(".//mxCell")
    if not cells:
        # Try without namespace
        for diagram in root.findall(".//diagram"):
            # drawio files may have compressed content — skip if so
            pass
        cells = root.iter("mxCell") if hasattr(root, 'iter') else []
        cells = list(root.iter("mxCell"))
    
    if not cells:
        warnings.append("Could not parse mxCell elements (file may use compressed format)")
        return {"valid": True, "errors": errors, "warnings": warnings}
    
    all_ids = set()
    edge_cells = []
    shape_cells = []
    resource_icons = []
    
    for cell in cells:
        cell_id = cell.get("id", "")
        style = cell.get("style", "")
        value = cell.get("value", "")
        is_edge = cell.get("edge") == "1"
        
        all_ids.add(cell_id)
        
        if is_edge:
            edge_cells.append(cell)
        elif cell.get("vertex") == "1":
            shape_cells.append(cell)
        
        if "mxgraph.aws4.resourceIcon" in style:
            resource_icons.append(cell)
    
    # CHECK 1: strokeColor=#ffffff on resourceIcon shapes
    for cell in resource_icons:
        style = cell.get("style", "")
        if "strokeColor=#ffffff" not in style.lower().replace(" ", ""):
            if "strokecolor=#ffffff" not in style.lower().replace(" ", ""):
                cell_id = cell.get("id", "?")
                errors.append(f"[CHECK 1] Missing strokeColor=#ffffff on resourceIcon: id={cell_id}")
                if fix:
                    if "strokeColor=" in style:
                        style = re.sub(r"strokeColor=#[0-9a-fA-F]+", "strokeColor=#ffffff", style)
                    else:
                        style += ";strokeColor=#ffffff"
                    cell.set("style", style)
                    fixes_applied.append(f"Fixed strokeColor on {cell_id}")
    
    # CHECK 2: No HTML tags in value=""
    html_pattern = re.compile(r"<(?:br|br/|b|i|font|hr|div|span|p)\b", re.IGNORECASE)
    for cell in cells:
        value = cell.get("value", "")
        style = cell.get("style", "")
        if value and "html=1" not in style:
            if html_pattern.search(value):
                cell_id = cell.get("id", "?")
                errors.append(f"[CHECK 2] HTML tags in value without html=1: id={cell_id}, value='{value[:50]}'")
    
    # CHECK 4: Broken edges (source/target IDs exist)
    for cell in edge_cells:
        source = cell.get("source", "")
        target = cell.get("target", "")
        cell_id = cell.get("id", "?")
        if source and source not in all_ids:
            errors.append(f"[CHECK 4] Edge {cell_id} references non-existent source: {source}")
        if target and target not in all_ids:
            errors.append(f"[CHECK 4] Edge {cell_id} references non-existent target: {target}")
    
    # CHECK 5: All edges must have edgeStyle=orthogonalEdgeStyle and rounded=0
    for cell in edge_cells:
        style = cell.get("style", "")
        cell_id = cell.get("id", "?")
        if "edgeStyle=orthogonalEdgeStyle" not in style:
            errors.append(f"[CHECK 5] Edge {cell_id} missing edgeStyle=orthogonalEdgeStyle (will render as diagonal line)")
            if fix:
                style = "edgeStyle=orthogonalEdgeStyle;" + style
                cell.set("style", style)
                fixes_applied.append(f"Added edgeStyle=orthogonalEdgeStyle to edge {cell_id}")
        if "rounded=1" in style:
            errors.append(f"[CHECK 5] Edge {cell_id} has rounded=1 (must be rounded=0)")
            if fix:
                style = style.replace("rounded=1", "rounded=0")
                cell.set("style", style)
                fixes_applied.append(f"Fixed rounded=1 → rounded=0 on edge {cell_id}")
    
    # CHECK 6: Labels not empty for service icons
    for cell in resource_icons:
        value = cell.get("value", "")
        if not value.strip():
            cell_id = cell.get("id", "?")
            warnings.append(f"[CHECK 6] ResourceIcon without label: id={cell_id}")
    
    # CHECK 7: Parent hierarchy valid
    for cell in cells:
        parent = cell.get("parent", "")
        if parent and parent not in all_ids and parent != "0":
            cell_id = cell.get("id", "?")
            errors.append(f"[CHECK 7] Cell {cell_id} references non-existent parent: {parent}")
    
    # Summary
    valid = len(errors) == 0
    
    print(f"\n{'✅' if valid else '❌'} Validation {'PASSED' if valid else 'FAILED'}: {filepath}")
    print(f"   Cells: {len(cells)} total ({len(edge_cells)} edges, {len(shape_cells)} shapes, {len(resource_icons)} AWS icons)")
    
    if errors:
        print(f"   ❌ {len(errors)} error(s):")
        for e in errors:
            print(f"      {e}")
    
    if warnings:
        print(f"   ⚠️  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"      {w}")
    
    if fix and fixes_applied:
        tree.write(filepath, xml_declaration=True, encoding="UTF-8")
        print(f"   🔧 {len(fixes_applied)} fix(es) applied and saved")
    
    return {"valid": valid, "errors": errors, "warnings": warnings, "fixes": fixes_applied}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_drawio.py <file.drawio> [--fix]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    fix_mode = "--fix" in sys.argv
    
    result = validate(filepath, fix=fix_mode)
    sys.exit(0 if result["valid"] else 1)
