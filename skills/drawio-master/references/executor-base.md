# Executor Common Guidelines

> Technical constraints are in `references/acb-standards.md` and `references/validation-rules.md`.

---

## 1. Template Adherence Rules

### 1.0 Pre-generation Batch Read

**Hard rule**: Before generating XML, batch-read the template .drawio file this diagram references. Extract all container styles, icon styles, and edge styles once up front.

| Source | Read path |
|---|---|
| Template .drawio file | `templates/diagrams/{template_file}` |
| Spec lock | `<project_path>/spec_lock.md` |
| ACB standards | `references/acb-standards.md` |
| Icon catalog | `references/aws-icons.md` (verify names only) |

**Forbidden — re-reading during generation**:
- Template file already loaded
- ACB standards already loaded

`spec_lock.md` is re-read before starting XML generation.

### 1.1 Style Extraction from Template

For each element type in the template, extract the EXACT style string:

| Element | Extract |
|---|---|
| Account container | Full `style="..."` string |
| Region container | Full `style="..."` string |
| VPC container | Full `style="..."` string |
| Resource icon (per category) | Full `style="..."` string |
| Sub-resource icon | Full `style="..."` string |
| Organization shapes | Full `style="..."` string |
| Edges (per type) | Full `style="..."` string |

**Copy-paste these styles EXACTLY into generated XML.** Do not modify, simplify, or "improve" them.

---

## 2. Design Parameter Confirmation (Mandatory)

Before generating XML, output a brief confirmation:

```
📝 Template: {template file}
🎨 Styles extracted: {N containers, N icon types, N edge types}
📐 Canvas: {WxH}, grid={G}
🔒 Spec lock: {verified / missing}
```

### 2.1 Spec Lock Re-read (Mandatory)

**Hard rule**: Before generating XML, `read_file <project_path>/spec_lock.md`. Use only values from this file. If context was compacted, also re-read `design_spec.md`.

---

## 3. XML Generation Rules

### 3.1 Write Order (CRITICAL)

```xml
<mxfile host="app.diagrams.net" ...>
  <diagram name="..." id="...">
    <mxGraphModel dx="..." dy="..." grid="1" gridSize="10" ...>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- PHASE 1: Container/group cells (outermost → innermost) -->
        <!-- PHASE 2: ALL edges (arrows, connections) -->
        <!-- PHASE 3: ALL shapes (icons, labels, detail boxes) -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Elements written LATER render ON TOP. So: containers first (bottom), edges middle, shapes last (top).

### 3.2 ID Convention

- Unique descriptive IDs: `{type}-{name}-{N}` (e.g., `account-security-1`, `edge-tgw-vpc-1`, `icon-guardduty-1`)
- Parent hierarchy: top-level elements → `parent="1"`, nested → `parent="{container_id}"`

### 3.3 Geometry Rules

- Containers: must fully enclose all children (padding 15-20px)
- Icons inside containers: relative to parent geometry
- Spacing between containers: 15-20px
- Spacing between icons: 40-80px

### 3.4 Edge Routing

For EACH edge:
1. Identify source (x,y,w,h) and target (x,y,w,h)
2. Check if ANY shape exists between source and target
3. If YES → add waypoints (`Array as="points"`) to route around
4. Use `edgeStyle=orthogonalEdgeStyle;rounded=0` always

### 3.5 Label Rules

- Service icons: `verticalLabelPosition=bottom;verticalAlign=top;align=center`
- Full service names — no abbreviations in labels
- Multi-line: use `&#xa;` NOT `<br>` or `<br/>`
- Environment color coding in HTML: `<font style="color: rgb(0,204,0);">Prod</font>`

---

## 4. Post-Generation Validation

Run ALL checks from `references/validation-rules.md`:

| # | Check | Fix |
|---|---|---|
| 1 | `strokeColor=#ffffff` on all resourceIcon shapes | Add it |
| 2 | No HTML tags in value="" | Replace with &#xa; |
| 3 | No text overlap | Adjust positions |
| 4 | No edge through shapes | Add waypoints |
| 5 | Z-order correct (edges before shapes) | Reorder |
| 6 | Labels not truncated | Fix sizing |
| 7 | Containers enclose children | Expand |
| 8 | Styles match template | Fix to match |

---

## 5. Output

Save to `projects/{filename}.drawio`.

Report:
```
## ✅ Diagram Complete
- [x] Design Spec confirmed
- [x] Template: {name} ({N} styles extracted)
- [x] XML generated ({N} elements, {N} edges, {N} shapes)
- [x] Validation passed (8/8 checks)
- [x] Output: projects/{filename}.drawio
```
