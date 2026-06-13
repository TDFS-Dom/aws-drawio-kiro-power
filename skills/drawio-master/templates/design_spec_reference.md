# {project_name} - Design Spec

> Human-readable design narrative — diagram type, scope, accounts, services, layout.
> Read once by Executor for context.
>
> Machine-readable execution contract: `spec_lock.md` (styles / icons / colors / edge patterns extracted from template).
> Executor re-reads `spec_lock.md` before generating XML to resist context-compression drift.
> Keep both in sync; on divergence, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | {project_name} |
| **Diagram Type** | {OU Hierarchy / Security Design / Network Design / Process Flow} |
| **Template** | {template file from diagrams/} |
| **Canvas** | {page dimensions, e.g. 850×1100} |
| **Grid** | 10 |
| **Pages** | {number of diagram pages} |
| **Output File** | {filename.drawio} |
| **Created Date** | {date} |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Page Width** | {pageWidth} |
| **Page Height** | {pageHeight} |
| **Grid Size** | 10 |
| **Grid** | 1 (ON) |
| **Shadow** | 0 (OFF) |
| **Math** | 0 (OFF) |
| **dx / dy** | {canvas offsets — adjust to fit content} |

---

## III. Scope & Architecture

### Scope
- {1-2 sentence description of what the diagram depicts}

### AWS Accounts
| # | Account Name | Account Type | Container Style |
|---|---|---|---|
| 1 | {name} | {Management/Security/Infrastructure/Workload/Sandbox} | {from template} |

### AWS Services
| # | Service Name | Icon Shape | fillColor | Category |
|---|---|---|---|---|
| 1 | {name} | `mxgraph.aws4.{shape}` | `#{hex}` | {Compute/Network/Security/...} |

### Connections
| # | Source → Target | Edge Style | Color | Label |
|---|---|---|---|---|
| 1 | {source} → {target} | {orthogonal/dashed} | `#{hex}` | {label text or empty} |

---

## IV. Layout Design

### Flow Direction
- {Top→Bottom / Left→Right / Hub-Spoke / Radial Tree}

### Container Hierarchy
```
{Account containers}
  └── {Region containers (if needed)}
      └── {VPC containers (if needed)}
          └── {Services}
```

### Grouping Strategy
- {How elements are grouped — by OU, by function, by environment}

---

## V. Visual Theme (from template)

### Container Styles

| Container Type | strokeColor | fillColor | fontColor | dashed |
|---|---|---|---|---|
| Account | `#CD2264` | `none` | `#CD2264` | 0 |
| Region | `#00A4A6` | `none` | `#147EBA` | 1 |
| VPC | `#00CC00` | `none` | `#AAB7B8` | 0 |
| On-premise | `#7D8998` | `none` | `#5A6C86` | 0 |
| OU boundary (dashed box) | `#5A6C86` | `none` | `#5A6C86` | 1 |

### Icon Styles

| Category | fillColor | gradientColor | strokeColor |
|---|---|---|---|
| Security | `#C7131F` | `#F54749` | `#ffffff` |
| Management | `#BC1356` | `#F34482` | `#ffffff` |
| Networking | `#8C4FFF` | — | `#ffffff` |
| Compute | `#ED7100` | — | `#ffffff` |
| Developer Tools | `#C925D1` | — | `#ffffff` |
| Organizations | `#BC1356` | — | `none` |

### Edge Styles

| Connection Type | strokeColor | strokeWidth | endArrow | dashed |
|---|---|---|---|---|
| {type} | `#{hex}` | {1/2/3} | {classic/none} | {0/1} |

---

## VI. Environment Color Coding

| Environment | Inline HTML Color |
|---|---|
| **Prod** | `rgb(0, 204, 0)` — green |
| **NonProd** | `rgb(0, 0, 255)` — blue |
| Standard | `#232F3E` — AWS dark |

---

## VII. Technical Constraints

- [ ] All `mxgraph.aws4.resourceIcon` shapes MUST have `strokeColor=#ffffff`
- [ ] Sub-resource shapes (endpoints, gateway, firewall) use `strokeColor=none`
- [ ] Organizations shapes use `fillColor=#BC1356; strokeColor=none`
- [ ] No HTML tags in `value=""` — use `&#xa;` for newlines
- [ ] XML write order: containers → edges → shapes
- [ ] All edges use `edgeStyle=orthogonalEdgeStyle;rounded=0`
- [ ] No text overlap
- [ ] No edge crossing through shapes without waypoints
