---
layout_id: aft_pipeline
kind: layout
summary: AWS Account Factory Terraform (AFT) deployment, CI/CD pipelines, automation flows, multi-phase process diagrams.
canvas_format: standard_and_landscape
page_count: 16
page_types: [high_level, phase_detail, implementation, deep_dive, migration]
---

# aft_pipeline - AFT Pipeline Design Specification

> Suitable for CI/CD pipelines, Account Factory Terraform, deployment automation, multi-phase process flows, implementation detail diagrams.

---

## I. Template Overview

| Property | Description |
|----------|-------------|
| **Template Name** | aft_pipeline |
| **Source File** | `AFT.drawio` |
| **Pages** | 16 |
| **Use Cases** | AFT account vending, CodePipeline/CodeBuild flows, Terraform automation, phased deployment, implementation details |
| **Design Tone** | Process-oriented, phased, numbered steps, swimlane-based |
| **Theme** | White background, Phase colors (Yellow/Blue/Green), DevTools purple (#C925D1) |
| **Info Density** | Variable — High-level overview (medium) to Implementation detail (very high) |

---

## II. Canvas Specification

| Context | Page Width | Page Height | Notes |
|---------|-----------|-------------|-------|
| Standard pages | 850 | 1100 | HighLvl, phase details |
| Landscape pages | 1169 | 827 | Some flow diagrams |
| Large implementation | 3300 | 2339 | ImplementPhase pages |
| Migration detail | 1654 | 1169 | MigrateToOnpremise, MigrateToTFE |

---

## III. Page Roster

| # | Sheet Name | Content | Pattern |
|---|---|---|---|
| 1 | `HighLvl` | AFT end-to-end flow — 3 phases (Request → Provisioning → Customization) | Swimlane + numbered steps |
| 2 | `AFTFlowPhase1` | Phase 1 detail — account request pipeline | Left→Right process |
| 3 | `AnsibleRunner` | Ansible Runner automation | Process flow |
| 4 | `HardeningImage` | AMI hardening pipeline | Process flow |
| 5 | `MigrateToOnpremise` | Migration to on-premise | Left→Right flow |
| 6 | `MigrateToTFE` | Migration to Terraform Enterprise | Left→Right flow |
| 7 | `AFTBootstrap` | AFT bootstrap process | Process flow |
| 8 | `HighLvlP1` | Phase 1 zoom-in detail | Swimlane detail |
| 9 | `HighLvlP2` | Phase 2 zoom-in detail | Swimlane detail |
| 10 | `HighLvlP3` | Phase 3 zoom-in detail | Swimlane detail |
| 11 | `RegisterFlow1-DeepDive` | Account registration deep dive | Detailed flow |
| 12 | `ImplementPhase1` | Phase 1 implementation detail | Large canvas, detailed |
| 13 | `ImplementPhase3` | Phase 3 implementation detail | Large canvas, detailed |
| 14 | `ImplementPhase2` | Phase 2 implementation detail | Large canvas, detailed |
| 15 | `DevOpsTerraform` | DevOps Terraform workflow | Process + ownership |
| 16 | `DevAppOps_ZOOM` | DevAppOps zoomed detail | Detailed view |

---

## IV. Layout Patterns

### Pattern A: Swimlane Phases (sheet 1 — HighLvl)
```
┌─────────────────┐  ┌────────────────────┐  ┌──────────────────────┐
│ Phase 1: Request │  │ Phase 2: Provision │  │ Phase 3: Customize   │
│ (Yellow)         │  │ (Blue)             │  │ (Green)              │
│                  │  │                    │  │                      │
│ GitLab → Code   │→ │ Service Catalog →  │→ │ CodeBuild → Terraform│
│ Pipeline → Build│  │ Control Tower      │  │                      │
└─────────────────┘  └────────────────────┘  └──────────────────────┘
                              ↓
                    ┌── ACB Vended Account ──┐
```

### Pattern B: Grey Zone Backgrounds (sheets 1-10)
- Logical groupings use grey rectangles: `fillColor=light-dark(#E6E6E6,#CCCCCC);strokeColor=none`
- Section titles as text labels above grey zones

### Pattern C: Multi-zoom (sheets 1, 8-10, 12-14)
- HighLvl → HighLvlP1/P2/P3 → ImplementPhase1/2/3
- Same content at increasing detail levels

---

## V. Icon Styles

| Service | Shape | fillColor | strokeColor | Size |
|---------|-------|-----------|-------------|------|
| CodePipeline | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.codepipeline` | `#C925D1` | `#ffffff` | 60×60 |
| CodeBuild | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.codebuild` | `#C925D1` | `#ffffff` | 50-60 |
| DynamoDB | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.dynamodb` | `#C925D1` | `#ffffff` | 60×60 |
| Service Catalog | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.service_catalog` | `#E7157B` | `#ffffff` | 60×60 |
| Control Tower | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.control_tower` | `#E7157B` | `#ffffff` | 60×60 |
| Lambda | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.lambda` | `#ED7100` | `#ffffff` | 40-60 |
| Step Functions | `mxgraph.aws4.group` + `grIcon=mxgraph.aws4.group_aws_step_functions_workflow` | — | `#CD2264` | container |

---

## VI. External Tool Icons

| Tool | Style | Size |
|------|-------|------|
| GitLab | `shape=image;image=https://icons.diagrams.net/icon-cache1/Socialcones-2932/Gitlab-794.svg` | 60×60 |
| Terraform | `shape=image;image=data:image/png,...` (embedded base64) | 50×50 |
| User Group | `shape=mxgraph.mscae.intune.user_group;fillColor=#505050` | 50×37 |

---

## VII. Swimlane & Phase Colors

| Phase | Swimlane fillColor | strokeColor | strokeWidth |
|-------|-------------------|-------------|-------------|
| Phase 1: Request | `#fff2cc` | `#d6b656` | 2 |
| Phase 2: Provisioning | `#dae8fc` | `#6c8ebf` | 2 |
| Phase 3: Customization | `#d5e8d4` | `#82b366` | 2 |

---

## VIII. Edge Styles

| Type | Style | Use |
|------|-------|-----|
| Standard process step | `strokeWidth=2;fontSize=12;fontStyle=1` | Normal flow |
| Yellow milestone (dashed) | `strokeWidth=3;dashed=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1` | Phase 1 complete signal |
| Green milestone (dashed) | `strokeWidth=3;dashed=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1` | Phase 3 complete signal |

### Numbered Step Labels
- Format: `value="(N) Action description"`
- Edge labels: `fontStyle=1;fontSize=12;strokeWidth=2`
- Use `labelBackgroundColor=default` for readability

---

## IX. Container Styles

| Element | Style |
|---------|-------|
| Account | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;fontColor=#CD2264;fontSize=16;` |
| On-premise | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_on_premise;strokeColor=#858B94;fillColor=none;fontColor=#858B94;` |
| Grey zone | `rounded=0;whiteSpace=wrap;html=1;strokeColor=none;fillColor=light-dark(#E6E6E6,#CCCCCC);fontSize=16;` |
| Dashed boundary | `rounded=1;whiteSpace=wrap;html=1;dashed=1;dashPattern=8 8;arcSize=2;fontSize=16;` |
| Step Functions | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_step_functions_workflow;strokeColor=#CD2264;fillColor=none;fontColor=#CD2264;fontStyle=1;fontSize=11;` |

---

## X. Key Design Principles

1. **Left-to-right process flow** with numbered steps `(1)`, `(2)`, `(3)`...
2. **Phase-based color coding** — Yellow/Blue/Green consistent throughout
3. **Multi-zoom architecture** — same content at 3 detail levels (overview → phase → implementation)
4. **Grey backgrounds** group related services without borders
5. **Milestone markers** = thick dashed colored edges indicate "phase complete"
6. **External tools** (GitLab, Terraform) shown as embedded images, not AWS shapes
