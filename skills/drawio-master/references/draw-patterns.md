# Draw Patterns Reference

> AI reads this at Step 3. Pick the pattern that matches your need, copy the style string EXACTLY.
> Change ONLY: `id`, `value`, `source`, `target`, `<mxGeometry>`.

---

## EDGES (pick ONE per connection)

| ID | Color | Width | Arrow | Dashed | Use When |
|---|---|---|---|---|---|
| E1 | default | 1 | → | no | Hierarchy, OU tree, default connection |
| E2 | default | 2 | → | no | Process step, data flow (labeled) |
| E3 | default | 1 | — | no | Bidirectional (no arrowhead) |
| E4 | default | 1 | — | yes | Dependency, non-data reference |
| E5 | default | 3 | → | no | Primary/important flow |
| E6 | `#FF9933` | 2 | → | no | AFT process / orange flow |
| E7 | `#FF0000` | 2 | → | no | Security alert / critical path |
| E8 | `#23445d` | 1 | — | yes | Network routing (subtle) |
| E9 | `#6c8ebf` | 3 | → | yes | NonProd shared services |
| E10 | `#82B366` | 2 | — | no | Prod shared services (green, no arrow) |
| E11 | `#D79B00` | 2 | — | no | Direct Connect / DX / on-prem link |
| E12 | `#C7131F` | 1 | → | no | Security finding flow (thin) |
| E13 | `#C7131F` | 1 | → | yes | Security dependency (dashed) |
| E14 | `#33FF33` | 2 | → | no | Integration / data link (green bright) |
| E15 | `#8C4FFF` | 1 | → | yes | Networking service (purple, dashed) |

### Edge Templates (copy-paste)

#### E1: Default hierarchy (200x used)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

#### E2: Process step with label (128x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fontSize=12;fontStyle=1
```

#### E3: Bidirectional no-arrow (67x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;
```

#### E4: Dashed dependency (66x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=none;endFill=0;
```

#### E5: Thick primary flow (63x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;
```

#### E6: Orange process (37x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#FF9933;
```

#### E7: Red security/critical (32x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF0000;strokeWidth=2;fontColor=#FF0000;
```

#### E8: Subtle network routing (26x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;dashed=1;fillColor=#bac8d3;strokeColor=#23445d;
```

#### E9: NonProd blue dashed (20x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=3;fontSize=12;startArrow=classic;startFill=1;
```

#### E10: Prod green no-arrow (7x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;strokeWidth=2;strokeColor=#82B366;
```

#### E11: DX orange no-arrow (4x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;strokeWidth=2;fillColor=#d5e8d4;strokeColor=#D79B00;
```

#### E12: Security thin solid (5x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#C7131F;strokeWidth=1;
```

#### E13: Security thin dashed (5x)
```
edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#C7131F;fontSize=8;dashed=1;
```

#### E14: Integration green (6x)
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#33FF33;
```

#### E15: Networking purple dashed (2x)
```
html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;endArrow=classic;endFill=1;strokeColor=#8C4FFF;fontSize=10;dashed=1;labelBackgroundColor=#FFFFFF;
```

---

## CONTAINERS (pick ONE per boundary)

| ID | Type | strokeColor | Use When |
|---|---|---|---|
| C1 | Subnet (teal) | `#00A4A6` | Private subnet, security group boundary |
| C2 | VPC (purple) | `#8C4FFF` | VPC boundary (standard) |
| C3 | Account | `#CD2264` | AWS Account boundary |
| C4 | AWS Cloud alt | `#232F3E` | Top-level AWS cloud |
| C5 | VPC (green) | `#00CC00` | VPC boundary (HLD style) |
| C6 | Region | `#00A4A6` dashed | Region boundary |
| C7 | On-prem DC | `#7D8998` | Corporate data center |
| C8 | Subnet (green) | `#7AA116` | Public subnet / NAT subnet |
| C9 | AWS Cloud | `#232F3E` | AWS Cloud wrapper |
| C10 | Subnet (blue) | `#006EAF` | Management subnet |
| C11 | OU boundary | `#5A6C86` dashed | Dashed box grouping accounts under OU |
| C12 | On-prem | `#858B94` | On-premise generic |
| C13 | EC2 instance | `#D86613` | EC2 instance contents |
| C14 | Step Functions | `#CD2264` | Step Functions workflow |

### Container Templates (copy-paste)

#### C1: Subnet teal (277x) — most used
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

#### C2: VPC purple (147x)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

#### C3: Account (106x)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#CD2264;dashed=0;
```

#### C5: VPC green (32x) — HLD networking
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#00CC00;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

#### C6: Region dashed (24x)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=1;
```

#### C7: On-prem DC (18x)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_corporate_data_center;strokeColor=#7D8998;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#5A6C86;dashed=0;
```

#### C8: Public/NAT subnet green (18x)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#7AA116;fillColor=#F2F6E8;verticalAlign=top;align=left;spacingLeft=30;fontColor=#248814;dashed=0;
```

#### C11: OU boundary dashed (13x)
```
fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#5A6C86;labelBackgroundColor=default;
```

#### C12: On-prem generic (11x)
```
sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_on_premise;strokeColor=#858B94;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#858B94;dashed=0;
```

---

## ICONS (pick by AWS service category)

| ID | Category | fillColor | gradient | stroke | Type | Use When |
|---|---|---|---|---|---|---|
| I1 | Networking (sub-resource) | `#8C4FFF` | — | `none` | standalone | Endpoints, NAT GW, IGW, GWLB |
| I2 | Networking (service) | `#8C4FFF` | — | `#ffffff` | resourceIcon | TGW, VPC, Route53, Direct Connect |
| I3 | Management | `#E7157B` | — | `#ffffff` | resourceIcon | Control Tower, CloudWatch, Config |
| I4 | DevTools | `#C925D1` | — | `#ffffff` | resourceIcon | CodeBuild, CodePipeline, DynamoDB |
| I5 | General/dark | `#232F3D` | — | `none` | standalone | Firewall, User, Generic |
| I6 | Compute (sub-resource) | `#ED7100` | — | `none` | standalone | Lambda (small), Auto Scaling |
| I7 | Compute (service) | `#ED7100` | — | `#ffffff` | resourceIcon | Lambda, EC2, ECS |
| I8 | Organizations | `#BC1356` | — | `none` | standalone | OU, Account, Mgmt Account |
| I9 | Security (w/gradient) | `#C7131F` | `#F54749` | `#ffffff` | resourceIcon | GuardDuty, Security Hub |
| I10 | Storage | `#7AA116` | — | `#ffffff` | resourceIcon | S3, EBS, Backup |
| I11 | Management (w/gradient) | `#BC1356` | `#F34482` | `#ffffff` | resourceIcon | Organizations, Config |
| I12 | Security (standalone) | `#DD344C` | — | `none` | standalone | IAM Role, Finding, Shield |
| I13 | Security (service) | `#DD344C` | — | `#ffffff` | resourceIcon | WAF, KMS, Secrets Manager |
| I14 | IAM Access Analyzer | `#FF5252` | — | `none` | standalone | Access Analyzer only |

### Icon Templates (copy-paste)

#### I1: Networking sub-resource (301x) — endpoints, NAT, IGW
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.{SHAPE_NAME};
```
Shapes: `endpoints`, `nat_gateway`, `internet_gateway`, `application_load_balancer`, `network_load_balancer`

#### I2: Networking service (148x) — TGW, VPC, Route53
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `transit_gateway`, `vpc`, `route_53`, `direct_connect`, `cloudfront`

#### I3: Management service (94x) — Control Tower, CloudWatch
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#E7157B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `control_tower`, `cloudwatch`, `cloudformation`, `systems_manager`, `service_catalog`

#### I4: DevTools (85x) — CodeBuild, CodePipeline
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `codebuild`, `codepipeline`, `codedeploy`, `dynamodb`

#### I7: Compute service (43x) — Lambda, EC2
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `lambda`, `ec2`, `ecs`, `eks`, `fargate`

#### I8: Organizations standalone (40x) — OU, Account
```
outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#BC1356;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.{SHAPE_NAME};labelBackgroundColor=default;
```
Shapes: `organizations_organizational_unit`, `organizations_account`, `organizations_management_account`

#### I9: Security with gradient (27x) — GuardDuty, Security Hub
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `guardduty`, `security_hub`

#### I10: Storage (23x) — S3
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `s3`, `elastic_block_store`, `backup`

#### I11: Management with gradient (16x) — Organizations, Config
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{SERVICE_NAME};
```
Services: `organizations`, `config`

#### I14: IAM Access Analyzer (12x) — standalone, no gradient
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF5252;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.access_analyzer;
```

---

## TEXT (pick by role)

| ID | fontSize | Bold | Use When |
|---|---|---|---|
| T1 | 24 | yes | Diagram title |
| T2 | 16 | yes | Section / module header |
| T3 | 16 | no | Account container label |
| T4 | 12 | yes | Edge label, annotation |
| T5 | 10 | no | Small note, disclaimer |

### Text Templates

#### T1: Title (24px bold)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=24;fontStyle=1
```

#### T2: Section header (16px bold)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=16;fontStyle=1
```

#### T4: Edge label / annotation (12px bold)
```
text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=12;fontStyle=1
```

#### T5: Small note (10px)
```
text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=10;
```
