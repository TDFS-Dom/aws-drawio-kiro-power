---
layout_id: ou_hierarchy
kind: layout
summary: AWS Organizations OU hierarchy tree — radial top-down from Organization root to OUs to Accounts.
canvas_format: landscape_wide
page_count: 1
page_types: [hierarchy]
---

# ou_hierarchy - OU Hierarchy Design Specification

> Suitable for AWS Organizations structure, Landing Zone OU layout, account hierarchy diagrams.

---

## I. Template Overview

| Property | Description |
|----------|-------------|
| **Template Name** | ou_hierarchy |
| **Source File** | `ACB _ OU Design 1.drawio` |
| **Pages** | 1 |
| **Use Cases** | Organization structure, OU tree, account layout, Landing Zone design |
| **Design Tone** | Hierarchical, structured, tree layout |
| **Theme** | White background, AWS Organizations pink (#BC1356) |
| **Info Density** | Medium — clear spacing between hierarchy levels |

---

## II. Canvas Specification

| Property | Value |
|----------|-------|
| **Page Width** | 850 |
| **Page Height** | 1100 |
| **dx** | 2828 (extends beyond page for wide tree) |
| **dy** | 1682 |
| **Grid** | 10 |
| **Shadow** | 0 |

---

## III. Page Roster

| # | Sheet Name | Content | Pattern |
|---|---|---|---|
| 1 | `Page-1` | Full OU hierarchy tree | Radial top-down tree |

---

## III. Layout Pattern

### Flow Direction
- **Radial Tree** — top-down from center
- Organization root at top-center (y≈210)
- OUs branch horizontally at shared Y-coordinate (y≈400 routing, y≈519 OU icons)
- Accounts below OUs (y≈700+)

### Hierarchy Levels
```
Level 0: Organization root (icon 78×78, gradient)
Level 1: Control Tower + SSO (service icons, horizontal neighbors)
Level 2: OUs (org unit icons, spread horizontally)
Level 3: Dashed boundary boxes (group accounts under OU)
Level 4: Account icons (inside boundary boxes)
```

### Routing Pattern
- All edges from Organization root share a single Y-coordinate waypoint (y=400)
- From waypoint, each edge routes orthogonally down to its target OU
- OU → boundary box edges are direct vertical

---

## IV. Icon Styles

| Element | Shape | fillColor | strokeColor | Size |
|---------|-------|-----------|-------------|------|
| Organization root | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.organizations` | `#BC1356` | `#ffffff` | 78×78 |
| Control Tower | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.control_tower` | `#E7157B` | `#ffffff` | 78×78 |
| SSO | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.single_sign_on` | `#DD344C` | `#ffffff` | 78×78 |
| OU icon | `mxgraph.aws4.organizations_organizational_unit` | `#BC1356` | `none` | 78×67 |
| Account icon | `mxgraph.aws4.organizations_account` | `#BC1356` | `none` | 74×78 |
| Management Account | `mxgraph.aws4.organizations_management_account` | `#BC1356` | `none` | 74×78 |

### Special Modifiers
- **Placeholder accounts**: `opacity=50` (faded/greyed out)
- **Suspended accounts**: `sketch=1;curveFitting=1;jiggle=2` (hand-drawn look)

---

## V. Container Styles

| Element | Style |
|---------|-------|
| OU boundary box | `fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#5A6C86;labelBackgroundColor=default;` |

---

## VI. Edge Styles

| Type | Style |
|------|-------|
| Organization → OU | `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontStyle=1;labelBackgroundColor=default;` |
| OU → boundary box | `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontStyle=1;labelBackgroundColor=default;` |

---

## VII. Label Conventions

- **Environment color coding**: Prod = `rgb(0,204,0)`, NonProd = `rgb(0,0,255)`
- **Font**: fontSize=12, fontStyle=1 (bold), fontColor=#232F3E
- **OU labels**: `{Name}\n<div>OU</div>`
- **Account labels**: `<div>{Name}</div><div>Account</div>`
- Organization root label: fontSize=14
