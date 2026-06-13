---
layout_id: security_iam
kind: layout
summary: AWS Security services delegation, IAM design, logging, incident response across Landing Zone accounts.
canvas_format: standard
page_count: 4
page_types: [delegated_admin, security_logging, incident_response]
---

# security_iam - Security & IAM Design Specification

> Suitable for security services delegation diagrams, IAM architecture, centralized logging, incident response flows.

---

## I. Template Overview

| Property | Description |
|----------|-------------|
| **Template Name** | security_iam |
| **Source File** | `ACB-SWO_AWS LZ_Security and IAM Design_20260317.drawio` |
| **Pages** | 4 |
| **Use Cases** | Security Hub delegation, GuardDuty multi-account, Config aggregation, incident response automation |
| **Design Tone** | Security-focused, account-centric, delegation pattern |
| **Theme** | White background, Security red (#C7131F) + Management pink (#BC1356) |
| **Info Density** | Medium — repeated service pattern across account boxes |

---

## II. Canvas Specification

| Property | Value |
|----------|-------|
| **Page Width** | 850 |
| **Page Height** | 1100 |
| **dx** | 2156 |
| **dy** | 2029 |
| **Grid** | 10 |
| **Shadow** | 0 |

---

## III. Page Roster

| # | Sheet Name | Content | Pattern |
|---|---|---|---|
| 1 | `Delegated Security Admin` | Security Hub + GuardDuty + Config + Access Analyzer delegation from Info Security account to all other accounts | Central delegated admin, members feed upward |
| 2 | `Delegated Security Admin (Old)` | Previous version — legacy reference | Same pattern, older layout |
| 3 | `Security Logging (Old)` | Centralized logging architecture — CloudTrail, VPC Flow Logs to Log Archive | Account → S3 bucket aggregation |
| 4 | `Incident Response (Old)` | Security Hub → EventBridge → Step Functions → Auto Remediation + SIEM/ServiceNow | Left-to-right event-driven flow |

---

## IV. Layout Patterns

### Pattern A: Delegated Admin (sheets 1-2)
```
┌─ Log Archive Account ─┐
│   Security Hub ← *     │ (receives from delegated admin)
└────────────────────────┘
         ↑
┌─ Info Security Account (DELEGATED ADMIN) ─┐
│   GuardDuty → Security Hub                 │
│   Config    → Security Hub                 │
│   Access Analyzer → Security Hub           │
└────────────────────────────────────────────┘
         ↑                    ↑
┌─ Infrastructure ─┐  ┌─ Workload ─┐
│   Same 3 services │  │ Same 3 svc │
└───────────────────┘  └────────────┘
```

### Pattern B: Incident Response (sheet 4)
```
Workload Account → Security Hub → EventBridge → [SNS / Step Functions / Lambda] → [SIEM / ServiceNow / Auto-Remediation]
```

---

## V. Icon Styles

| Service | Shape | fillColor | gradientColor | strokeColor |
|---------|-------|-----------|---------------|-------------|
| GuardDuty | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.guardduty` | `#C7131F` | `#F54749` | `#ffffff` |
| Security Hub | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.security_hub` | `#C7131F` | `#F54749` | `#ffffff` |
| AWS Config | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.config` | `#BC1356` | `#F34482` | `#ffffff` |
| IAM Access Analyzer | `mxgraph.aws4.access_analyzer` | `#FF5252` | — | `none` |
| EventBridge | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.eventbridge` | `#E7157B` | — | `#ffffff` |
| Lambda | `mxgraph.aws4.resourceIcon` + `resIcon=mxgraph.aws4.lambda` | `#ED7100` | — | `#ffffff` |
| S3 Bucket | `mxgraph.aws4.bucket_with_objects` | `#7AA116` | — | `none` |
| IAM Role | `mxgraph.aws4.role` | `#DD344C` | — | `none` |

---

## VI. Container Styles

| Element | Style Pattern |
|---------|---------------|
| Account box | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;fontColor=#CD2264;fontSize=16;` |
| Region (nested) | `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;fontColor=#147EBA;dashed=1;` |

---

## VII. Edge Styles

| Type | Style |
|------|-------|
| Account → Delegated Admin | `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;` |
| Service → Security Hub (within account) | Same, short vertical connection |

---

## VIII. Key Design Principle

**Repetitive pattern**: The SAME 3 services (GuardDuty, Config, Access Analyzer → Security Hub) are repeated IDENTICALLY in every account box. Only the delegated admin account has the "central" role. This shows that findings flow FROM member accounts TO the delegated admin.
