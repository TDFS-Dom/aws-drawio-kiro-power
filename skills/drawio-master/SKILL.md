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
> **EXCEPTION: Edges use 3 fixed patterns defined in "WHAT EDGES LOOK LIKE" section — no sheet lookup needed for edges.**

---

## 🚨 MANDATORY RULES (numbered for audit)

1. **SERIAL EXECUTION** — Steps in order. No skipping.
2. **BLOCKING = HARD STOP** — Step 2 waits for user confirmation. Do NOT proceed.
3. **NO SPECULATIVE XML** — Do NOT write any XML until Step 4.
4. **SHEET FILE IS LAW** — Every style string MUST come from `templates/{id}/sheets/{NN}_{slug}.md`. **Exception for edges**: Edge base pattern (`edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;`) is universal — `strokeColor` and `strokeWidth` are set per the Edge Types table in "WHAT EDGES LOOK LIKE" section, not copied verbatim from sheets.
5. **NO STYLE INVENTION** — If you write a container or icon style not found in a sheet file, it's a bug. Edge styles follow the 3 allowed patterns in "WHAT EDGES LOOK LIKE" — no other edge styles permitted.
6. **XML WRITE ORDER** — Containers → Edges → Shapes. Always.
7. **NO ROUNDED EDGES** — All edges: `rounded=0`. No exceptions.
8. **EVERY EDGE MUST HAVE `edgeStyle=orthogonalEdgeStyle`** — Omitting causes diagonal lines that cut across containers. No exceptions.
9. **ACCOUNTS USE AWS GROUPS** — Never use `rounded=1;whiteSpace=wrap` for accounts. Always `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account`.

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

### 🚨 ABSOLUTE RULE: `edgeStyle=orthogonalEdgeStyle` on EVERY edge

**ALL edges MUST include `edgeStyle=orthogonalEdgeStyle`** — this ensures orthogonal routing (right-angle turns). Without it, draw.io uses direct/straight lines that cut diagonally across containers.

```
❌ WRONG (missing edgeStyle → diagonal line):
style="rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#DD344C;dashed=1;"

✅ CORRECT (orthogonal routing):
style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#DD344C;dashed=1;"
```

**ALWAYS**: `edgeStyle=orthogonalEdgeStyle;rounded=0`. **NEVER**: omit `edgeStyle`, never `rounded=1`.

---

### Edge Types (3 categories)

#### Type 1: Data Flow — Solid, colored, strokeWidth=2

For active data movement between services (logs, events, replication).

```xml
<mxCell id="{unique-id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor={COLOR};" edge="1" parent="1" source="{SOURCE_ID}" target="{TARGET_ID}">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Color by AWS category of the SOURCE service:**
| Source Category | strokeColor | Example |
|---|---|---|
| Networking (VPC Flow, DNS, TGW) | `#8C4FFF` | Flow Logs → S3 |
| Security (GuardDuty, Security Hub) | `#C7131F` | GuardDuty → S3 |
| Management (Config, Organizations, S3 Replication) | `#BC1356` | S3 Replication → S3 |
| Compute (Lambda, Step Functions) | `#ED7100` | Lambda → SQS |
| DevTools (CodePipeline, CodeBuild) | `#C925D1` | CodePipeline → CodeBuild |

#### Type 2: Dependency/Encryption — Dashed, thinner, strokeWidth=1

For non-data relationships: encryption keys, IAM policies, configuration references.

```xml
<mxCell id="{unique-id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor={COLOR};dashed=1;" edge="1" parent="1" source="{SOURCE_ID}" target="{TARGET_ID}">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Color matches the source service category** (same table as Type 1).
Example: KMS (Security) → S3 Bucket = `strokeColor=#DD344C;dashed=1`

#### Type 3: Hierarchy — Default weight, no color

For OU trees, org structure, parent-child relationships.

```xml
<mxCell id="{unique-id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="{SOURCE_ID}" target="{TARGET_ID}">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

No `strokeWidth` (defaults to 1), no `strokeColor` (defaults to black).

---

### Exit/Entry Points (RECOMMENDED for cross-account edges)

When source and target are in **different account containers**, add explicit exit/entry points to control routing direction:

```
exitX=1;exitY=0.5;exitDx=0;exitDy=0;    ← exit from RIGHT middle of source
entryX=0;entryY=0.5;entryDx=0;entryDy=0; ← enter LEFT middle of target
```

**Common patterns:**
| Flow Direction | Exit | Entry |
|---|---|---|
| Left → Right | `exitX=1;exitY=0.5` | `entryX=0;entryY=0.5` |
| Top → Bottom | `exitX=0.5;exitY=1` | `entryX=0.5;entryY=0` |
| Into container border | — | `entryPerimeter=0` (pin to exact coordinate) |

Without exit/entry points, draw.io auto-routes which may produce unexpected paths across nested containers.

---

### 🚨 Cross-Account Horizontal Flow (CRITICAL PATTERN)

**Problem**: When multiple edges go left→right across 3-4 account containers, orthogonal auto-routing causes edges to overlap and cut through intermediate containers.

**Solution**: Use explicit waypoints via `<Array>` points to control routing path.

#### Pattern: Parallel horizontal edges with vertical offset

When 3+ edges flow from left accounts to right accounts, stagger them vertically so they don't overlap:

```xml
<mxCell id="e-flow1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="src1" target="tgt1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="620" y="99" />
      <mxPoint x="620" y="119" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Waypoint Rules:**
1. Each parallel edge gets its own "channel" — offset by 20px vertically from neighbors
2. Waypoints should be placed in the GAPS between containers (not overlapping container content)
3. Use exit/entry points to force edges to leave/enter from specific sides
4. For fan-out (1 source → many targets), offset waypoints by 20px per edge

#### Pattern: Fan-out from single source (e.g., KMS → 4 buckets)

When one service connects to multiple targets stacked vertically:

```xml
<!-- First edge exits right, waypoints route to first target -->
<mxCell id="e-kms-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#DD344C;dashed=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="i-kms" target="target-1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="560" y="559" />
      <mxPoint x="560" y="119" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Key principle:** Explicit waypoints > auto-routing for cross-account diagrams. The extra XML is worth it for clean, non-overlapping edges.

#### Pattern: Vertical Trunk Line (multiple sources → multiple targets)

From the reference diagram (Log Archive): multiple log sources on LEFT feed into a vertical "trunk" corridor, then branch right to individual S3 buckets.

```
Source A ──────┐
               │  ← trunk at fixed X (e.g. x=500)
Source B ──────┤
               │
Source C ──────┘
               │
               ├──── Target 1 (bucket-network)
               │
               ├──── Target 2 (bucket-security)
               │
               └──── Target 3 (bucket-cloudtrail)
```

Implementation: each edge shares a common X-coordinate for waypoints, offset by 15-20px per edge:

```xml
<!-- Source A → Target 1: trunk at x=500 -->
<mxCell id="e-a-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;..." edge="1" parent="1" source="src-a" target="tgt-1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="500" y="150" />
      <mxPoint x="500" y="150" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Source B → Target 2: trunk at x=515 (offset 15px) -->
<mxCell id="e-b-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;..." edge="1" parent="1" source="src-b" target="tgt-2">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="515" y="350" />
      <mxPoint x="515" y="370" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Source C → Target 3: trunk at x=530 (offset 30px) -->
<mxCell id="e-c-3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;..." edge="1" parent="1" source="src-c" target="tgt-3">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="530" y="550" />
      <mxPoint x="530" y="590" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Trunk corridor width**: 50-80px between source containers and target containers. Each edge occupies a "lane" offset by 15px from its neighbor.

#### When to use waypoints vs auto-routing:

| Scenario | Approach |
|---|---|
| Source & target in SAME container | Auto-routing (no waypoints needed) |
| Source & target in ADJACENT containers (1 hop) | exit/entry points usually sufficient |
| Source & target separated by 2+ containers | Waypoints REQUIRED for clean routing |
| Fan-out: 1 source → 3+ targets | Waypoints REQUIRED to prevent overlap |
| Security Hub → Firehose (same container, vertical) | Auto-routing fine |

---

### Edge Labels

**Preferred**: Use `value=""` on the edge itself for short labels (inline with the line).

**Fallback**: Use separate text cells (floating labels) only when:
- Label text is multi-line
- Label needs precise positioning independent of edge routing
- Multiple annotations needed on same edge

Text label style for edge annotations:
```
text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=10;
```

---

### Edge Checklist (verify EVERY edge)

- [ ] Has `edgeStyle=orthogonalEdgeStyle` (NO EXCEPTIONS)
- [ ] Has `rounded=0`
- [ ] Has valid `source` and `target` IDs
- [ ] `strokeColor` matches source service category
- [ ] Data flow = `strokeWidth=2;` solid | Dependency = `strokeWidth=1;dashed=1;`
- [ ] Cross-account edges (2+ hops) have waypoints via `<Array as="points">`
- [ ] Fan-out edges (1→N) have staggered waypoints (20px offset per edge)
- [ ] No edge visually overlaps another edge on the same path
- [ ] No `curved`, `rounded=1`, or missing `edgeStyle`

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
➡️ Edges: using 3 standard patterns (Data Flow / Dependency / Hierarchy)
```

**CRITICAL**: From this point forward, ONLY container/icon styles from the loaded sheet file may appear in your XML. Edge styles use the 3 fixed patterns from "WHAT EDGES LOOK LIKE". If you need a container/icon style not in the file → STOP and tell the user.

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
- [ ] Container/icon style COPIED from sheet file (not invented)
- [ ] Edge style uses one of 3 allowed patterns (Data Flow / Dependency / Hierarchy)
- [ ] Unique ID
- [ ] Correct parent (nested in container? parent=container_id)
- [ ] `strokeColor=#ffffff` on ALL resourceIcon shapes
- [ ] `rounded=0` on ALL edges
- [ ] `edgeStyle=orthogonalEdgeStyle` on ALL edges (no exceptions)
- [ ] Edge type correct: data flow (solid/2px) vs dependency (dashed/1px) vs hierarchy (default)
- [ ] Edge `strokeColor` matches source service category color
- [ ] Cross-account edges (2+ hops) have waypoints or exit/entry points
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
| 3 | All edges have `edgeStyle=orthogonalEdgeStyle` | Omitting → diagonal lines |
| 4 | Accounts use `shape=mxgraph.aws4.group` | Using colored rectangles |
| 5 | No `shape=document/hexagon/cylinder3` | Using generic shapes |
| 6 | No invented colors | Using `#dae8fc`, `#d5e8d4` |
| 7 | Z-order: containers → edges → shapes | Mixing order |
| 8 | No text overlap | Elements too close |
| 9 | Containers enclose children | Children outside bounds |
| 10 | Edge strokeColor matches source category | Wrong color for flow type |

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
❌ Any CONTAINER or ICON style not found in a sheets/*.md file  ← style invention
❌ Any EDGE style not matching the 3 allowed patterns          ← only Data Flow / Dependency / Hierarchy
❌ Edge WITHOUT edgeStyle=orthogonalEdgeStyle             ← causes diagonal lines across containers
❌ Edge with curved/elbow routing                         ← only orthogonal allowed
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

### Data Flow Edge (solid, colored)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;
```

### Dependency Edge (dashed, thinner)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#DD344C;dashed=1;
```

### Hierarchy Edge (default, no color)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
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
