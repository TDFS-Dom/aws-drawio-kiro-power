---
layout_id: networking
kind: layout
summary: AWS networking architecture — VPC topology, Transit Gateway hub-spoke, routing tables, traffic flows, on-prem connectivity.
canvas_format: landscape_overflow
page_count: 22
page_types: [hld, tgw_design, vpc_detail, routing, traffic_flow, third_party]
---

# networking - Networking Design Specification

> Suitable for VPC topology, Transit Gateway designs, Direct Connect connectivity, ingress/egress flows, routing table diagrams, third-party integration.

---

## I. Template Overview

| Property | Description |
|----------|-------------|
| **Template Name** | networking |
| **Source File** | `ACB_Networking_diagrams .drawio` |
| **Pages** | 22 |
| **Use Cases** | Network HLD, TGW hub-spoke, VPC connectivity, routing tables, traffic flows, ingress/egress paths |
| **Design Tone** | Technical networking, hub-spoke centric, color-coded connections |
| **Theme** | White background, Networking purple (#8C4FFF), VPC green (#00CC00) |
| **Info Density** | High — multiple VPCs, on-prem DCs, color-coded paths |

---

## II. Canvas Specification

| Property | Value |
|----------|-------|
| **Page Width** | 827 |
| **Page Height** | 1169 |
| **page** | 0 (overflow mode — content extends beyond page boundaries) |
| **Grid** | 10 |
| **Shadow** | 0 |

---

## III. Page Roster

| # | Sheet Name | Content | Pattern |
|---|---|---|---|
| 1 | `HLD` | High-level network design — TGW at center, all VPCs + on-prem | Hub-spoke |
| 2 | `Overall Prod TGW design` | Prod TGW routing + attachments | Hub-spoke detail |
| 3 | `Overall NonProd TGW design` | NonProd TGW routing + attachments | Hub-spoke detail |
| 4 | `Share NonProd Service Account` | Shared Services VPC detail | VPC internal layout |
| 5 | `3rd nonprod party private link - provider` | PrivateLink provider setup | Left→Right flow |
| 6 | `3rd prod party private link - consumer` | PrivateLink consumer (Prod) | Left→Right flow |
| 7 | `3rd nonprod party private link - consumer` | PrivateLink consumer (NonProd) | Left→Right flow |
| 8 | `3rd prod party vpn` | Third-party VPN (Prod) | Left→Right flow |
| 9 | `3rd non prod party vpn` | Third-party VPN (NonProd) | Left→Right flow |
| 10 | `Internal connectivity_nonprod` | Internal connectivity routing | Routing diagram |
| 11 | `Onprem-ACB-NonProd-rtb` | On-prem to NonProd route tables | Routing table |
| 12 | `3rd Party NonProduction Connectivity` | Third-party NonProd connectivity | Connection diagram |
| 13 | `Egress NonProd Connectivity` | Egress path NonProd | Traffic flow |
| 14 | `Ingress Prod Connectivity` | Ingress path Prod | Traffic flow |
| 15 | `Ingress NonProd Connectivity` | Ingress path NonProd | Traffic flow |
| 16 | `External flow for integration` | External integration paths | Traffic flow |
| 17 | `Non HTTP Ingress traffic flow` | Non-HTTP ingress (TCP/UDP) | Traffic flow |
| 18 | `Egress traffic flow` | Egress traffic path | Traffic flow |
| 19 | `3rd party ingress vpn` | Third-party ingress via VPN | Connection diagram |
| 20 | `3rd party ingress private link` | Third-party ingress via PrivateLink | Connection diagram |
| 21 | `3rd party egress vpn` | Third-party egress via VPN | Connection diagram |
| 22 | `3rd party egress private link` | Third-party egress via PrivateLink | Connection diagram |

---

## IV. Layout Patterns

### Pattern A: Hub-Spoke (sheets 1-3)
- Transit Gateway at CENTER (large icon 90×90)
- VPCs arranged around TGW (north=shared services, south=ingress/egress, east=inspection)
- On-prem DCs on LEFT
- Color-coded connections by type

### Pattern B: VPC Detail (sheets 4+)
- Single VPC container with subnets
- Services inside subnets
- Route tables shown as separate elements

### Pattern C: Traffic Flow (sheets 13-22)
- Left→Right or Top→Bottom flow
- Numbered steps on edges
- Source → middlebox → destination

---

## V. Icon Styles

| Service | Shape | fillColor | strokeColor | Size |
|---------|-------|-----------|-------------|------|
| Transit Gateway | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.transit_gateway` | `#8C4FFF` | `#ffffff` | 90×90 |
| Direct Connect | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.direct_connect` | `#8C4FFF` | `#ffffff` | 30×30 |
| Site-to-Site VPN | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.site_to_site_vpn` | `#8C4FFF` | `#ffffff` | 30×30 |
| Endpoints / GWLB EP | `mxgraph.aws4.endpoints` | `#8C4FFF` | `none` | 50×50 |
| ALB | `mxgraph.aws4.application_load_balancer` | `#8C4FFF` | `none` | 50×50 |
| NAT Gateway | `mxgraph.aws4.nat_gateway` | `#8C4FFF` | `none` | 50×50 |
| Internet Gateway | `mxgraph.aws4.internet_gateway` | `#8C4FFF` | `none` | 50×50 |
| Generic Firewall | `mxgraph.aws4.generic_firewall` | `#232F3D` | `none` | 50×42 |

---

## VI. Container Styles

| Element | Style |
|---------|-------|
| VPC | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#00CC00;fillColor=none;fontColor=#AAB7B8;` |
| VPC (stacked, multiple) | Same but `fillColor=default` + offset 9px for visual stack |
| On-premise DC | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_corporate_data_center;strokeColor=#7D8998;fillColor=none;fontColor=#5A6C86;` |

---

## VII. Edge Styles (COLOR-CODED)

| Connection Type | strokeColor | fillColor | strokeWidth | endArrow |
|---|---|---|---|---|
| On-prem → TGW (Direct Connect) | `#D79B00` | `#d5e8d4` | 2 | none |
| Ingress/Egress/Inspection → TGW | `#d79b00` | `#ffe6cc` | 2 | none |
| Shared Services NonProd → TGW | `#6c8ebf` | `#dae8fc` | 2 | none |
| Shared Services Prod → TGW | `#82B366` | — | 2 | none |

**CRITICAL**: `endArrow=none;endFill=0` — all network connections are **bidirectional** (no arrowheads).

---

## VIII. Special Patterns

### Embedded Data Center Image
- On-prem buildings use `shape=image;image=data:image/png,...` (base64 encoded building icon)
- Size: 180×180 px

### Stacked VPC Visual (represents "many VPCs")
- 3 overlapping VPC containers offset ~9px each
- Back: `container=0;fillColor=default`
- Middle: `container=0;fillColor=default;shadow=0`
- Front: `container=1;fillColor=default` (holds label)

### Small Icon + Text Label
- DX/VPN icons at 30×30 with separate text cell above: `fontSize=10;fontStyle=1`

---

## IX. Key Design Principle

**Color = connection TYPE, not environment.** Orange = DX, Blue = shared services non-prod, Green = shared services prod. The TGW at center is the focal point — everything connects TO it. No arrowheads because all paths are bidirectional.
