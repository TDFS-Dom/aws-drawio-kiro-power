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
> **EXCEPTION: Edges use 3 structural patterns (Data Flow/Dependency/Hierarchy) with colors from `references/draw-patterns.md` — no sheet lookup needed for edges.**

---

## 🚨 MANDATORY RULES (14 rules — sorted by priority)

### Priority A: Visual Quality (most critical — AI violates most often)
1. **LINES MUST NOT CROSS ICONS** — If any shape sits on the edge path → waypoints to route around. Clearance 20px.
2. **LINES MUST NOT CROSS FOREIGN BOUNDARIES** — A line MUST NEVER pass through a container it doesn't belong to. Route around.
3. **LINES MUST HAVE CLEAR DIRECTION** — Every data-flow line must have arrowhead. Bidirectional explicitly uses `endArrow=none`.
4. **ACCOUNTS USE AWS GROUPS** — Never use `rounded=1;whiteSpace=wrap` for accounts. Always `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account`.
5. **NO STYLE INVENTION** — If you write a container or icon style not found in a sheet file, it's a bug.

### Priority B: Style Source (wrong styles = wrong visual output)
6. **SHEET FILE IS LAW** — Every container/icon style MUST come from `templates/{id}/sheets/{NN}_{slug}.md`. **Exception for edges**: Edge base pattern is universal — colors from `references/draw-patterns.md`.

### Priority C: XML Structure (break = file won't render correctly)
7. **EVERY EDGE MUST HAVE `edgeStyle=orthogonalEdgeStyle`** — Omitting causes diagonal lines across containers.
8. **NO ROUNDED EDGES** — All edges: `rounded=0`. No exceptions.
9. **XML WRITE ORDER** — Containers → Edges → Shapes. Always.
10. **NO XML COMMENTS** — `<!-- -->` comments are strictly forbidden in output. (Official draw.io rule)
11. **ALWAYS `html=1`** — Include `html=1` in EVERY cell style string. (Official draw.io best practice)

### Priority D: Pipeline Discipline (break = workflow failure)
12. **SERIAL EXECUTION** — Steps in order. No skipping.
13. **BLOCKING = HARD STOP** — Step 2 waits for user confirmation. Do NOT proceed.
14. **NO SPECULATIVE XML** — Do NOT write any XML until Step 4.

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

> **Full color list**: See `references/draw-patterns.md` Edge table (E1-E15) for all allowed colors including `#FF9933` (AFT process), `#FF0000` (critical/alert), `#33FF33` (integration), `#D79B00` (DX/on-prem), `#6c8ebf` (NonProd shared), `#82B366` (Prod shared).

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

---

### 🚨 EDGE ROUTING CASES (11 patterns — pick the right one)

| # | Case | When | Trunk? | Waypoints? |
|---|---|---|---|---|
| 1 | **One-to-One** | A → B (single connection) | No | No (auto-route) |
| 2 | **One-to-Many** (fan-out) | KMS → 4 buckets | No | Yes (offset 20px per edge) |
| 3 | **Many-to-One** (fan-in) | GuardDuty + Config → Security Hub | No | Yes (stagger entryY) |
| 4 | **Many-to-Many** | 3 accounts → 4 buckets | Yes | Yes (per-lane X, per-target Y) |
| 5 | **Chain** | Pipeline → Build → Deploy | No | No (sequential) |
| 6 | **Same-container** | Service → Service (same account) | No | No (auto-route) |
| 7 | **Cross-account adjacent** | Account A → Account B (neighbors) | No | exit/entry points |
| 8 | **Cross-account distant** | Account A → Account C (skip B) | Yes | Yes (route around B) |
| 9 | **Bidirectional** | On-prem ↔ TGW | No | endArrow=none |
| 10 | **Dependency** | KMS encrypts S3 | No | dashed, thin |
| 11 | **Hub-spoke** | TGW ← many VPCs | No | Each spoke separate edge |

#### Case 1: One-to-One
```
[A] ────→ [B]
```
Auto-route. No waypoints needed unless containers between them.

#### Case 2: One-to-Many (fan-out)
```
         ┌──→ [T1]    exitY=0.3
[Source] ─┼──→ [T2]    exitY=0.5
         └──→ [T3]    exitY=0.7
```
- Each edge exits at different Y offset
- Waypoints: stagger X by 20px per edge
- Targets stacked vertically → entry at entryX=0;entryY=0.5 each

#### Case 3: Many-to-One (fan-in)
```
[S1] ──┐     entryY=0.2
[S2] ──┼──→ [Target]   entryY=0.5
[S3] ──┘     entryY=0.8
```
- Each source enters target at different Y
- **If sources are same flow type → MERGE into shared segment** (see MERGE RULE below)

---

### 🚨 3 MERGE TECHNIQUES (prevents spaghetti / nút thắt)

Choose technique based on NUMBER OF SOURCES merging:

| Sources | Technique | When |
|---|---|---|
| 2-5 | **Junction Point** | Small fan-in, clear origin visible |
| 6+ | **Bus Line** | Many sources, need clean vertical/horizontal collector |
| Any (HLD) | **Grouped Arrow** | High-level overview, detail not needed per-line |

---

#### Technique 1: Junction Point (2-5 sources → 1 target)

Sources merge at a single waypoint coordinate, then 1 shared segment goes to target.

```
[S1] ──┐
[S2] ──┤  ← junction at x=450
[S3] ──┼──────────────→ [Target]
[S4] ──┘
```

- All edges share SAME trunk X (or Y for horizontal merge)
- Same `target` ID → draw.io overlaps the shared segment visually
- Each source's waypoint converges to same coordinate

```xml
<!-- S1 → Target: junction at x=450 -->
<mxCell id="e-s1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" parent="1" source="s1" target="target-1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="450" y="100" />
      <mxPoint x="450" y="300" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- S2 → SAME Target: SAME junction X=450 -->
<mxCell id="e-s2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" parent="1" source="s2" target="target-1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="450" y="200" />
      <mxPoint x="450" y="300" />
    </Array>
  </mxGeometry>
</mxCell>
```

---

#### Technique 2: Bus Line (6+ sources → 1 or few targets)

A dedicated vertical "bus" line collects all sources, then dispatches to targets. Sources connect horizontally to the bus, bus runs vertically, targets branch off horizontally.

```
[S1] ────┐
[S2] ────┤
[S3] ────┤
[S4] ────┤  ║ BUS (vertical line at x=500)
[S5] ────┤  ║
[S6] ────┤  ║
[S7] ────┘  ║
            ╠════→ [Target 1]
            ╠════→ [Target 2]
            ╚════→ [Target 3]
```

**Implementation**: Use a visible vertical line as a "bus" element:
```xml
<!-- Bus line (visual element, not an edge) -->
<mxCell id="bus-1" value="" style="endArrow=none;html=1;strokeWidth=4;strokeColor=#CD2264;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="500" y="80" as="sourcePoint" />
    <mxPoint x="500" y="600" as="targetPoint" />
  </mxGeometry>
</mxCell>

<!-- Sources connect TO bus (short horizontal stubs) -->
<mxCell id="e-s1-bus" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;entryX=0;entryY=0.1;" edge="1" parent="1" source="s1" target="bus-1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Bus dispatches TO targets (horizontal branches) -->
<mxCell id="e-bus-t1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" parent="1" source="bus-1" target="target-1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

---

#### Technique 3: Grouped Arrow (HLD / high-level overview)

For high-level diagrams where individual lines would clutter — use ONE thick arrow representing the aggregate flow, with a label describing what flows through it.

```
┌─────────────┐                    ┌─────────────┐
│  Source      │                    │  Target     │
│  Accounts   │ ════════════════►  │  Log Archive│
│  (All)      │   "All Logs"       │  Account    │
└─────────────┘                    └─────────────┘
```

**Implementation**: Single thick edge with descriptive label:
```xml
<mxCell id="e-grouped" value="VPC Flow + DNS + TGW Logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=4;strokeColor=#8C4FFF;fontSize=10;fontStyle=1;" edge="1" parent="1" source="src-accounts" target="tgt-logarchive">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**When to use Grouped Arrow:**
- HLD (High-Level Design) diagrams where detail is zoomed out
- Executive overview — audiences don't need per-service lines
- When 5+ individual lines would make the diagram unreadable
- Label MUST describe what's aggregated: "All Security Findings", "VPC + DNS + TGW Logs"

---

### MERGE DECISION TABLE

| Condition | Technique |
|---|---|
| 2-5 sources, same color, same target | **Junction Point** |
| 6+ sources, same color, same target area | **Bus Line** |
| HLD/overview, many flows abstracted | **Grouped Arrow** |
| Sources → DIFFERENT targets | **Do NOT merge** (use offset lanes) |
| Different colors (different flow types) | **Do NOT merge** (keep separate) |
| Different line types (solid vs dashed) | **Do NOT merge** |

---

#### Case 4: Many-to-Many (trunk corridor) — MOST COMPLEX
```
[S1] ──┐     ┌──→ [T1]
[S2] ──┼─────┼──→ [T2]
[S3] ──┘     └──→ [T3]
       ↑ corridor
```
**Rules:**
1. Each source gets own X-lane: x=500, x=520, x=540 (offset 20px)
2. Each target gets own entry Y: entryY=0.2, 0.4, 0.6, 0.8
3. Color per source account (not per target)
4. Corridor placement: midpoint between source and target columns

```xml
<!-- Source 1 → Target 1: lane x=500 -->
<mxCell id="e-s1-t1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.2;entryDx=0;entryDy=0;" edge="1" parent="1" source="s1" target="t1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="500" y="100" />
      <mxPoint x="500" y="80" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Source 2 → Target 2: lane x=520 -->
<mxCell id="e-s2-t2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="s2" target="t2">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="520" y="300" />
      <mxPoint x="520" y="250" />
    </Array>
  </mxGeometry>
</mxCell>
```

#### Case 5: Chain (sequential)
```
[A] ──→ [B] ──→ [C] ──→ [D]
```
Simple sequential edges. Each edge independent.

#### Case 6: Same-container
```
┌─────────────────────────┐
│  [A] ────→ [B]          │
└─────────────────────────┘
```
Auto-route. Both elements share same parent. No exit/entry needed.

#### Case 7: Cross-account adjacent
```
┌────────┐    ┌────────┐
│   [A]  │───→│  [B]   │
└────────┘    └────────┘
```
Add exit/entry: `exitX=1;exitY=0.5;entryX=0;entryY=0.5`

#### Case 8: Cross-account distant (skip intermediate)
```
┌──────┐    ┌──────┐    ┌──────┐
│ [A]  │    │ SKIP │    │ [B]  │
└──────┘    └──────┘    └──────┘
     └──── waypoints route ABOVE or BELOW ────→
```
MUST use waypoints to route around the middle container.

#### Case 9: Bidirectional
```
[On-prem] ═══════ [TGW]
```
`endArrow=none;endFill=0` — no arrowhead either end.

#### Case 10: Dependency/Reference
```
[KMS] ┄┄┄┄┄ [S3 Bucket]
```
`strokeWidth=1;dashed=1;dashPattern=3 3` — thin short dash.
Route SEPARATELY from data flow lines (different Y band or X lane).

#### Case 11: Hub-spoke
```
         [VPC1]
          ↑ exitY=0.2
[VPC2] ← [TGW] → [VPC3]
  exitX=0     exitX=1
          ↓ exitY=0.8
         [VPC4]
```
Central hub has multiple exit points. Each spoke = separate edge with unique exit coordinates.

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

## GEOMETRY & SPACING RULES (prevents icons outside containers & text overlap)

### 🚨 THE #1 BUG: Icons fall outside container boundaries

**Root cause**: AI sets container width/height too small for the icons + labels inside.

**MANDATORY CALCULATION before writing XML:**

```
Container minimum width  = (number_of_icons_horizontal × icon_width) + (gaps × (n-1)) + (padding_left + padding_right)
Container minimum height = (number_of_icons_vertical × (icon_height + label_height)) + (gaps × (n-1)) + (padding_top + padding_bottom)
```

### Sizing Constants (from templates — measured from 836 containers + 1064 icons across 94 sheets)

**3 density levels** (spacing changes based on diagram complexity):

| Density | Icons | H-Gap | V-Gap | Left Pad | Top Pad | Use When |
|---|---|---|---|---|---|---|
| **Low** (1-5 icons) | ≤5 | 25 px | 56 px | 80 px | 40 px | Simple: single service, KMS reference |
| **Medium** (6-15 icons) | 6-15 | 52 px | 65 px | 74 px | 98 px | Standard: account with services |
| **High** (16+ icons) | ≥16 | 63 px | 52 px | 75 px | 60 px | Complex: HLD, multi-VPC, full arch |

**Pick density at Step 2** based on total icon count in Design Spec.

| Element | Size | Notes |
|---|---|---|
| AWS resource icon | 78×78 px | Most common (203x used). Also: 60×60, 50×50 |
| Sub-resource icon | 50×50 px | Endpoints, NAT GW, IGW (176x used) |
| Small icon | 40×40 px | DX, VPN, Lambda (inside containers) |
| Icon label height | 30 px | Below icon (`verticalLabelPosition=bottom`) |
| Icon total height (icon + label) | **108 px** | 78 + 30 |

> Full data: `references/geometry-rules.md` (extracted from `draw-patterns/` — 94 sheets)

### Container Sizing Formula

**1 icon inside container:**
```
width  = 50 (left) + 78 (icon) + 81 (right) = 209 px minimum
height = 41 (title) + 78 (icon) + 30 (label) + 50 (bottom) = 199 px minimum
```

**3 icons horizontal:**
```
width  = 50 + 78 + 60 + 78 + 60 + 78 + 81 = 485 px minimum
height = 41 + 78 + 30 + 50 = 199 px minimum
```

**3 icons vertical:**
```
width  = 50 + 78 + 81 = 209 px minimum
height = 41 + (78+30) + 53 + (78+30) + 53 + (78+30) + 50 = 521 px minimum
```

### Icon Placement Rules

**Relative to parent container (when `parent=container_id`):**
```xml
<!-- First icon: x=50, y=41 (below title) -->
<mxCell ... parent="container-id">
  <mxGeometry x="50" y="41" width="78" height="78" as="geometry" />
</mxCell>

<!-- Second icon horizontal: x=188, y=41 (50+78+60=188) -->
<mxCell ... parent="container-id">
  <mxGeometry x="188" y="41" width="78" height="78" as="geometry" />
</mxCell>

<!-- Second icon vertical: x=50, y=202 (41+78+30+53=202) -->
<mxCell ... parent="container-id">
  <mxGeometry x="50" y="202" width="78" height="78" as="geometry" />
</mxCell>
```

### Label Overlap Prevention

**Problem from screenshot**: "DNS Query Logs" text overlaps with icon below it.

**Rules:**
1. Icon label = 30px height reserved BELOW icon
2. Next icon starts at: `previous_icon_y + 78 (icon) + 30 (label) + 53 (gap) = +161px`
3. NEVER place icon at `previous_y + 100` — too close, labels WILL overlap
4. Safe vertical spacing between icon centers: **161px minimum** (78+30+53)
5. Safe horizontal spacing between icon centers: **138px minimum** (78+60)

### Container Boundary Check (MANDATORY before finalizing)

**For EVERY icon in the diagram, verify:**
```
icon_x + icon_width  ≤  parent_container_width - padding_right
icon_y + icon_height + label_height  ≤  parent_container_height - padding_bottom
```

**Example check:**
```
Container: x=100, y=100, width=300, height=200
Icon:      x=250, y=140, width=78, height=78 (relative to container)

Check horizontal: 250 + 78 = 328 > 300 ❌ OVERFLOW! → reduce icon x or increase container width
Check vertical:   140 + 78 + 30 = 248 > 200 ❌ OVERFLOW! → reduce icon y or increase container height
```

### Text Outside Container (CRITICAL)

**"delivery.logs.amazonaws.com" text in screenshot bleeds outside account boundary.**

**Rules:**
1. ALL text/label cells that belong to a container MUST have `parent="{container_id}"`
2. Text cells at container boundary → place INSIDE with 10px clearance
3. If text is too long → use `&#xa;` to wrap, or reduce fontSize
4. External annotations (outside all containers) → use `parent="1"` (root level)

### Account Container Minimum Sizes (from 836 actual containers)

| Content | Minimum Width | Minimum Height |
|---|---|---|
| 1 service icon | 209 | 199 |
| 2 icons horizontal | 347 | 199 |
| 3 icons horizontal | 485 | 199 |
| 2 icons vertical | 209 | 360 |
| 3 icons vertical | 209 | 521 |
| Region + 2 icons | 450 | 370 |
| VPC + subnets + icons | 520 | 420 |

> Actual account sizes from templates: min=160×80, avg=615×412, max=2110×1510

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
[Density]         {Low (≤5 icons) / Medium (6-15) / High (16+)}
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
3. Read: references/draw-patterns.md                      ← GENERIC PATTERNS (edges, containers, icons, text)
4. Read: references/shared-standards.md                      ← Anti-patterns
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

        <!-- NOTE: Do NOT include XML comments in actual output. -->
        <!-- This template shows PHASES for documentation only. -->
        <!-- In real output: just mxCell elements, no comments. -->

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
- [ ] `html=1` present in EVERY cell style
- [ ] NO XML comments (`<!-- -->`) in output — zero comments
- [ ] No text overlap (check geometry — vertical gap ≥ 161px between icon centers)
- [ ] **ALL icons inside parent container bounds** (icon_x+78 ≤ container_width-81, icon_y+108 ≤ container_height-50)
- [ ] **Container sized correctly** (use formula from GEOMETRY section)

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
| 8 | No text overlap | Icons vertical gap < 161px |
| 9 | Containers enclose children | icon_x+78 > container_width-81 |
| 10 | Edge strokeColor matches source category | Wrong color for flow type |
| 11 | **Icons inside bounds** | icon bleeds outside container |
| 12 | **Labels don't overlap icons below** | Vertical spacing too tight |

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
❌ <!-- XML comments -->                                   ← strictly forbidden (official draw.io rule)
❌ Any cell style missing html=1                           ← always include html=1
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
