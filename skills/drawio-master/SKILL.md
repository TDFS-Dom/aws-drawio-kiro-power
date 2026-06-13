| name | drawio-master |
| --- | --- |
| description | AI-driven AWS architecture diagram generation. Converts requirements into draw.io XML using ONLY styles extracted from production templates. Use when user asks to "create diagram", "draw architecture", "vẽ diagram", or mentions "drawio", "draw.io". |

# Drawio Master Skill

> Core Pipeline: `Request Analysis → Design Spec ⛔ → Load Sheet Styles → XML Generation → Validation → Output`

> [!CAUTION]
> ## 🚨 EXECUTION DISCIPLINE — READ THIS FIRST
>
> **EVERY SINGLE STYLE STRING in the output XML MUST come from a `templates/{id}/sheets/*.md` file.**
>
> You are NOT a designer. You are a COPIER. Your job:
> 1. Read the sheet file
> 2. Copy the style strings EXACTLY
> 3. Change only `value=""`, `id=""`, and `<mxGeometry>` coordinates
>
> **VIOLATIONS THAT WILL HAPPEN IF YOU DON'T FOLLOW THIS:**
> - ❌ `rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc` ← INVENTED. Not in any template.
> - ❌ `shape=document` ← INVENTED. Templates use `mxgraph.aws4.*` shapes.
> - ❌ `shape=hexagon` ← INVENTED. Not in any template.
> - ❌ `shape=cylinder3` for S3 ← WRONG. Templates use `mxgraph.aws4.bucket_with_objects` or `mxgraph.aws4.s3`.
> - ❌ Custom colors like `#dae8fc`, `#d5e8d4`, `#fff2cc` ← INVENTED. Templates use `#CD2264`, `#8C4FFF`, `#BC1356`, etc.
>
> **IF A STYLE IS NOT IN THE SHEET FILE → YOU CANNOT USE IT. ASK THE USER.**

---

## 🚨 MANDATORY RULES (numbered for audit)

1. **SERIAL EXECUTION** — Steps in order. No skipping.
2. **BLOCKING = HARD STOP** — Step 2 waits for user confirmation. Do NOT proceed.
3. **NO SPECULATIVE XML** — Do NOT write any XML until Step 4.
4. **SHEET FILE IS LAW** — Every style string MUST come from `templates/{id}/sheets/{NN}_{slug}.md`.
5. **NO STYLE INVENTION** — If you write a style not found in a sheet file, it's a bug.
6. **XML WRITE ORDER** — Containers → Edges → Shapes. Always.
7. **NO ROUNDED EDGES** — All edges: `rounded=0`. No exceptions.
8. **ACCOUNTS USE AWS GROUPS** — Never use `rounded=1;whiteSpace=wrap` for accounts. Always `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account`.

---

## WHAT AWS ACCOUNTS LOOK LIKE (MANDATORY)

Every AWS Account boundary MUST use this exact pattern (from templates):

```xml
<mxCell id="{unique-id}" value="{Account Name}" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#CD2264;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="{X}" y="{Y}" width="{W}" height="{H}" as="geometry" />
</mxCell>
```

**NEVER** use `rounded=1;fillColor=#dae8fc` or any colored rectangle for accounts.

---

## WHAT AWS SERVICE ICONS LOOK LIKE (MANDATORY)

Every AWS service icon MUST use this pattern:

```xml
<mxCell id="{unique-id}" value="{Service Name}" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor={CATEGORY_COLOR};strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};" vertex="1" parent="{PARENT}">
  <mxGeometry x="{X}" y="{Y}" width="78" height="78" as="geometry" />
</mxCell>
```

**Category colors:**
- Security: `fillColor=#C7131F` (with `gradientColor=#F54749;gradientDirection=north`)
- Management: `fillColor=#BC1356` (with `gradientColor=#F34482;gradientDirection=north`)
- Networking: `fillColor=#8C4FFF`
- Compute: `fillColor=#ED7100`
- Storage: `fillColor=#7AA116`
- DevTools: `fillColor=#C925D1`

**NEVER** use `shape=document`, `shape=cylinder3`, `shape=hexagon`, or any generic shape for AWS services.

---

## WHAT EDGES LOOK LIKE (MANDATORY)

```xml
<mxCell id="{unique-id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor={COLOR};" edge="1" parent="1" source="{SOURCE_ID}" target="{TARGET_ID}">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**ALWAYS**: `rounded=0`. **NEVER**: `rounded=1`.

---

## Template Index

| ID | Folder | Sheets | Use When |
|---|---|---|---|
| `ou_hierarchy` | `templates/ou_hierarchy/` | 1 | OU structure, org tree |
| `security_iam` | `templates/security_iam/` | 10 | Security, IAM, delegation |
| `networking` | `templates/networking/` | 42 | VPC, TGW, routing |
| `aft_pipeline` | `templates/aft_pipeline/` | 42 | CI/CD, automation |

---

## WORKFLOW

### Step 1: Request Analysis

🚧 GATE: User provided a diagram request.

1. What type? → Match to template from index above
2. What sheet? → Read `templates/{id}/sheets_index.md`, pick closest sheet
3. What services? → List AWS services needed

If unclear → ask user.

✅ Proceed to Step 2.

---

### Step 2: Design Spec ⛔ BLOCKING

🚧 GATE: Template and sheet identified.

**Present to user and WAIT:**

```
📐 DESIGN SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Diagram Type]    {type}
[Template]        {template_id}
[Reference Sheet] {sheet name}
[Scope]           {what will be drawn}
[Accounts]        {list}
[Services]        {list — mxgraph.aws4.{name} verified}
[Flow Direction]  {direction}
[Output File]     {filename.drawio}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Shall I proceed?
```

**DO NOT WRITE XML UNTIL USER SAYS OK.**

✅ User confirmed → Step 3.

---

### Step 3: Load Sheet Styles

🚧 GATE: User confirmed Design Spec.

**Read these files IN ORDER:**

```
1. Read: templates/{template_id}/sheets_index.md
2. Read: templates/{template_id}/sheets/{NN}_{slug}.md   ← THE STYLES
3. Read: references/acb-standards.md                      ← Anti-patterns
```

**After reading, output:**
```
📄 Loaded: sheets/{NN}_{slug}.md
🎨 Containers: {N} styles available
🔷 Icons: {N} styles available
➡️ Edges: {N} styles available
```

**CRITICAL**: From this point forward, ONLY styles from the loaded sheet file may appear in your XML. If you need a style not in the file → STOP and tell the user.

✅ Styles loaded → Step 4.

---

### Step 4: XML Generation

🚧 GATE: Sheet styles loaded.

**Write order (MANDATORY):**

```xml
<mxfile host="app.diagrams.net" modified="..." agent="Kiro" version="24.0.0" type="device">
  <diagram id="..." name="...">
    <mxGraphModel dx="..." dy="..." grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ═══ PHASE 1: CONTAINERS (outermost → innermost) ═══ -->
        <!-- Account groups, Region groups, VPC groups -->

        <!-- ═══ PHASE 2: ALL EDGES ═══ -->
        <!-- Every connection/arrow -->

        <!-- ═══ PHASE 3: ALL SHAPES ═══ -->
        <!-- AWS icons, text labels, detail boxes -->

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Per-element checklist:**
- [ ] Style string COPIED from sheet file (not invented)
- [ ] Unique ID
- [ ] Correct parent (nested in container? parent=container_id)
- [ ] `strokeColor=#ffffff` on ALL resourceIcon shapes
- [ ] `rounded=0` on ALL edges
- [ ] No `<br>` or HTML tags in value — use `&#xa;`
- [ ] No text overlap (check geometry)

✅ XML written → Step 5.

---

### Step 5: Validation

🚧 GATE: XML complete.

**Run:**
```bash
python3 ${SKILL_DIR}/scripts/validate_drawio.py <file.drawio>
```

**Also manually verify:**

| # | Check | ❌ Common mistake |
|---|---|---|
| 1 | All icons have `strokeColor=#ffffff` | Forgetting on new icons |
| 2 | All edges have `rounded=0` | Using `rounded=1` |
| 3 | Accounts use `shape=mxgraph.aws4.group` | Using colored rectangles |
| 4 | No `shape=document/hexagon/cylinder3` | Using generic shapes |
| 5 | No invented colors | Using `#dae8fc`, `#d5e8d4` |
| 6 | Z-order: containers → edges → shapes | Mixing order |
| 7 | No text overlap | Elements too close |
| 8 | Containers enclose children | Children outside bounds |

Fix errors → re-validate → Step 6.

---

### Step 6: Output

```
## ✅ Diagram Complete
- [x] Design Spec confirmed
- [x] Template: {id} / Sheet: {name}
- [x] Styles: ALL from sheet file (0 invented)
- [x] Validation: passed
- [x] Output: projects/{filename}.drawio
```

---

## FORBIDDEN PATTERNS (auto-fail checklist)

If ANY of these appear in your output, the diagram FAILS:

```
❌ rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc    ← colored rectangle (not AWS group)
❌ shape=document                                        ← generic shape (use AWS icon)
❌ shape=hexagon                                         ← generic shape
❌ shape=cylinder3                                       ← use mxgraph.aws4.s3 or bucket_with_objects
❌ fillColor=#dae8fc / #d5e8d4 / #fff2cc / #f8cecc      ← invented pastel colors
❌ rounded=1 on edges                                    ← must be rounded=0
❌ strokeColor=#6c8ebf / #82b366 / #b85450 on accounts  ← wrong account style
❌ Any style string NOT found in a sheets/*.md file       ← style invention
```

---

## ALLOWED PATTERNS (copy these)

### Account Container
```
points=[[0,0],[0.25,0],...];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#CD2264;dashed=0;
```

### Region Container
```
...shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=1;
```

### VPC Container
```
...shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#00CC00;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

### S3 Bucket Icon
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#7AA116;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.bucket_with_objects;
```

### Standard Edge
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;
```

---

## Standalone Workflows

| ID | File | When |
|---|---|---|
| design-spec | `workflows/design-spec.md` | Detailed examples |
| template-fill | `workflows/template-fill-drawio.md` | Modify existing .drawio |

---

## Notes

• Output → `projects/` directory
• Open with: draw.io Desktop, app.diagrams.net, VS Code Draw.io extension
• Sheet files in `templates/{id}/sheets/` are the ONLY style source
• AI lost context? Re-read this file: `skills/drawio-master/SKILL.md`
