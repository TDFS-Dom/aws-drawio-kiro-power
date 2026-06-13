| name | drawio-master |
| --- | --- |
| description | AI-driven AWS architecture diagram generation system. Converts architecture requirements into professional draw.io XML through multi-step pipeline with design spec confirmation. Use when user asks to "create diagram", "draw architecture", "vẽ diagram", "vẽ kiến trúc", or mentions "drawio", "draw.io", "architecture diagram". |

# Drawio Master Skill

> AI-driven AWS architecture diagram generation. Converts architecture requirements
> into professional draw.io XML through strict pipeline with design spec confirmation
> and template-matched execution.
>
> Core Pipeline: `Request Analysis → Design Spec ⛔ → Reference Loading → XML Generation → Validation → Output`

> [!CAUTION]
> ## 🚨 Global Execution Discipline (MANDATORY)
>
> This workflow is a strict serial pipeline. The following rules have the highest
> priority — violating any one of them constitutes execution failure:
>
> 1. **SERIAL EXECUTION** — Steps MUST be executed in order; the output of each step is the input for the next.
> 2. **BLOCKING = HARD STOP** — Steps marked ⛔ BLOCKING require a full stop; the AI MUST wait for explicit user response before proceeding and MUST NOT make any decisions on behalf of the user.
> 3. **NO SPECULATIVE EXECUTION** — "Pre-preparing" XML for subsequent Steps is FORBIDDEN (e.g., writing draw.io XML during the Design Spec phase).
> 4. **GATE BEFORE ENTRY** — Each Step has prerequisites (🚧 GATE) listed at the top; these MUST be verified before starting.
> 5. **TEMPLATE LOCK** — Once a template is selected in Step 2, ALL styles MUST come from that template's `sheets/` files. No mixing, no invention.
> 6. **SPEC_LOCK RE-READ** — Before generating XML, AI MUST re-read `spec_lock.md`. No values from memory or invented on the fly.
> 7. **XML MUST BE HAND-WRITTEN** — Every diagram XML is written by the main agent directly. Scripts that produce XML in batch are FORBIDDEN.
> 8. **NO STYLE INVENTION** — Styles not found in the template `sheets/*.md` files are FORBIDDEN. If a pattern doesn't exist in templates, ask the user.

> [!IMPORTANT]
> ## 🌐 Language & Communication Rule
>
> • Response language: match the user's input language.
> • Design Spec format: MUST follow its template structure regardless of conversation language.

---

## Template Index

| ID | Folder | Sheets | Diagram Type |
|---|---|---|---|
| ou_hierarchy | `templates/ou_hierarchy/` | 1 | OU structure, org hierarchy |
| security_iam | `templates/security_iam/` | 10 | Security services, IAM delegation |
| networking | `templates/networking/` | 42 | VPC, TGW, routing, connectivity |
| aft_pipeline | `templates/aft_pipeline/` | 42 | CI/CD, automation, deployment flows |

For full template details, read `templates/README.md`.

---

## Reference Resources

| Purpose | File |
|---|---|
| Strategist role definition | `references/strategist.md` |
| Executor common guidelines | `references/executor-base.md` |
| ACB visual standards (extracted from templates) | `references/acb-standards.md` |
| AWS icon catalog + external SVG source | `references/aws-icons.md` |
| Post-draw validation checklist | `references/validation-rules.md` |
| Company branding/colours | `references/branding.md` |
| Architecture layout patterns | `references/architecture-patterns.md` |
| Shapes, effects, extended styling | `references/style-guide.md` |

---

## Workflow

### Step 1: Request Analysis

🚧 GATE: User has provided a diagram request (description, requirements, existing diagram to modify, or architecture spec).

1. Parse user intent — what type of diagram is needed?
2. Identify AWS services mentioned
3. Determine scope (single page / multi-page, single account / multi-account)
4. Match to template from Template Index

> No clear architecture description? Ask user: what accounts, what services, what flows, what environment (Prod/NonProd).

✅ Checkpoint — Intent parsed, template identified. Proceed to Step 2.

---

### Step 2: Design Spec (MANDATORY — cannot be skipped)

🚧 GATE: Step 1 complete; request understood and template identified.

First, read the role definition:

```
Read references/strategist.md
```

🚧 **Mandatory gate**: before presenting Design Spec, MUST `read_file templates/design_spec_reference.md` and follow its full I–VII section structure.

⛔ **BLOCKING**: Present the Seven Confirmations as a single bundled recommendation and wait for explicit user confirmation before proceeding.

**Seven Confirmations:**
1. **Diagram type & template match**
2. **Canvas format & page dimensions**
3. **AWS accounts & scope**
4. **AWS services** (icon names verified against `references/aws-icons.md`)
5. **Flow direction & layout pattern**
6. **Edge/connection style & colors**
7. **Output filename**

**Output format:**

```
📐 DESIGN SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Diagram Type]    {type}
[Template]        {template_id}
[Reference Sheet] {sheet name from sheets_index.md}
[Canvas]          {dimensions}
[Scope]           {description}
[Accounts]        {list}
[Services]        {list with verified icon names}
[Flow Direction]  {direction}
[Edge Style]      {colors + rules}
[Pages]           {N}
[Output File]     {filename.drawio}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Shall I proceed with this spec?
```

After confirmation, output:
- `<project_path>/design_spec.md` — per `templates/design_spec_reference.md`
- `<project_path>/spec_lock.md` — per `templates/spec_lock_reference.md`

✅ Checkpoint — Design Spec confirmed. Proceed to Step 3.

---

### Step 3: Reference Loading

🚧 GATE: Step 2 complete; Design Spec confirmed by user.

Read the Executor role definition:

```
Read references/executor-base.md
```

**Actions:**
1. Read `templates/{template_id}/sheets_index.md` — identify the exact sheet to reference
2. Read `templates/{template_id}/sheets/{NN}_{sheet_slug}.md` — load **exact copy-paste ready style strings** for this specific pattern
3. Read `templates/{template_id}/design_spec.md` — understand layout pattern and design principles
4. Read `references/acb-standards.md` — anti-patterns and validation rules
5. Re-read `<project_path>/spec_lock.md`

> **Style extraction**: If `sheets/` folder doesn't exist yet, run:
> ```bash
> python3 ${SKILL_DIR}/scripts/extract_styles.py --all
> ```

> The sheet file is the PRIMARY source for XML generation. It contains extracted style strings from ONE specific sheet of the template .drawio file — copy them EXACTLY into generated XML. Do NOT modify, simplify, or "improve" them.

**Output confirmation:**
```
📝 Template: {template_id}
📄 Sheet: {sheet_name} (from sheets/{NN}_{slug}.md)
🎨 Styles loaded: {N} containers, {N} icons, {N} edges
📐 Canvas: {WxH}, grid=10
🔒 Spec lock: verified
```

✅ Checkpoint — References loaded, styles ready. Proceed to Step 4.

---

### Step 4: XML Generation

🚧 GATE: Step 3 complete; all styles extracted, spec_lock verified.

**Execution Rules:**
- Hand-write XML element by element
- Follow confirmed Design Spec exactly
- Use ONLY styles extracted in Step 3
- Main agent only — no delegation

**XML Write Order (MANDATORY):**
```xml
<mxfile host="app.diagrams.net" ...>
  <diagram name="..." id="...">
    <mxGraphModel dx="..." dy="..." grid="1" gridSize="10" guides="1"
     tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1"
     pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- PHASE 1: Containers (Account → Region → VPC) -->
        <!-- PHASE 2: ALL edges -->
        <!-- PHASE 3: ALL shapes (icons, labels, boxes) -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Per-element rules:**
- Unique descriptive IDs
- Correct parent hierarchy
- Styles EXACTLY from template
- No text overlap
- Edge routing with waypoints when needed

✅ Checkpoint — XML generated. Proceed to Step 5.

---

### Step 5: Validation

🚧 GATE: Step 4 complete; XML written.

**Run validation script:**
```bash
python3 ${SKILL_DIR}/scripts/validate_drawio.py <output_file.drawio>
```

Any `error` MUST be fixed before proceeding. `warning` entries: fix when straightforward.

**Manual checks (in addition to script):**

| # | Check | Fix if fails |
|---|---|---|
| 1 | `strokeColor=#ffffff` on all resourceIcon shapes | Script auto-detects |
| 2 | No HTML tags in `value=""` | Script auto-detects |
| 3 | No text overlap | Visual check — adjust positions |
| 4 | No edge through shapes without waypoints | Add waypoints |
| 5 | Z-order (edges before shapes in XML) | Reorder |
| 6 | All labels visible, not truncated | Fix sizing |
| 7 | Containers enclose all children | Expand |
| 8 | Styles match template (compare with sheet file) | Fix to match |

**If any check fails → fix and re-validate:**
```bash
python3 ${SKILL_DIR}/scripts/validate_drawio.py <output_file.drawio> --fix
```

✅ Checkpoint — Validation passed. Proceed to Step 6.

---

### Step 6: Output

🚧 GATE: Step 5 complete; all validations passed.

1. Save `.drawio` file to `projects/`
2. Report:

```
## ✅ Diagram Complete
- [x] Design Spec confirmed
- [x] Template matched: {name}
- [x] XML generated ({N} elements)
- [x] Validation passed (8/8 checks)
- [x] Output: projects/{filename}.drawio

Open with draw.io Desktop, app.diagrams.net, or VS Code Draw.io extension.
```

---

## Role Switching Protocol

Before loading references, output marker:

```
## [Role Switch: {Role Name}]
📖 Reading: references/{filename}
📋 Current task: {brief description}
```

---

## Standalone Workflows

| ID | File | Description |
|---|---|---|
| design-spec | `workflows/design-spec.md` | Design Spec confirmation flow (detailed patterns & examples) |
| template-fill | `workflows/template-fill-drawio.md` | Fill new content into existing .drawio — keep layout, swap labels/services/accounts |

---

## Notes

• Generated diagrams save to `projects/` by default
• Open .drawio with: draw.io Desktop (recommended), app.diagrams.net (web), VS Code Draw.io extension
• Per-sheet style files in `templates/{id}/sheets/` are the source of truth for styles
• To regenerate sheet files from source .drawio: `python3 scripts/extract_styles.py --all` (requires source .drawio in template folder)
• When unsure about a style → read the specific sheet .md file, copy the style string
• AI lost context? Ask it to re-read `skills/drawio-master/SKILL.md`
