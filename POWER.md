---
name: "aws-drawio"
displayName: "AWS Architecture Diagrams"
description: "Create professional AWS architecture diagrams in draw.io XML format — multi-account, Well-Architected, SA-grade quality"
keywords: ["aws", "drawio", "architecture", "diagram", "cloud", "vpc", "multi-account", "well-architected", "solutions-architect", "draw.io"]
icon: "icon.svg"
---

# AWS Architecture Diagram Power

Create professional, SA-grade AWS architecture diagrams in draw.io's native XML format. Focused exclusively on AWS — multi-account, multi-region, Well-Architected patterns.

## Output Format

Draw.io files are XML with this structure:

```xml
<mxfile host="app.diagrams.net" modified="DATE" agent="Claude" version="21.0.0" type="device">
  <diagram name="DIAGRAM_NAME" id="UNIQUE_ID">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- All diagram elements go here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Core Element Types

### Basic Shapes

```xml
<!-- Rectangle -->
<mxCell id="unique-id" value="Label Text" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
</mxCell>

<!-- Rounded Rectangle -->
<mxCell id="unique-id" value="Label" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
</mxCell>

<!-- Cylinder (Database) -->
<mxCell id="unique-id" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="80" as="geometry" />
</mxCell>

<!-- Ellipse -->
<mxCell id="unique-id" value="Node" style="ellipse;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="80" as="geometry" />
</mxCell>
```

### Containers & Groups

```xml
<!-- Swimlane (Container with Header) -->
<mxCell id="unique-id" value="Section Title" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="200" height="150" as="geometry" />
</mxCell>

<!-- Header Bar -->
<mxCell id="unique-id" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3D;strokeColor=#232F3D;" vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="400" height="40" as="geometry" />
</mxCell>
```

### Connectors & Arrows

```xml
<!-- Basic Arrow -->
<mxCell id="unique-id" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=2;strokeColor=#666666;" edge="1" parent="1" source="source-id" target="target-id">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Cross-Account Arrow (dashed + animated) -->
<mxCell id="unique-id" value="" style="endArrow=classic;html=1;dashed=1;dashPattern=12 4;strokeWidth=2;strokeColor=#1565C0;flowAnimation=1;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="200" y="200" as="sourcePoint" />
    <mxPoint x="400" y="200" as="targetPoint" />
  </mxGeometry>
</mxCell>

<!-- Flex Arrow (Replication/Data Flow) -->
<mxCell id="unique-id" value="" style="shape=flexArrow;endArrow=classic;html=1;fillColor=#FF8F00;strokeColor=#E65100;width=20;endSize=8;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="200" y="200" as="sourcePoint" />
    <mxPoint x="400" y="200" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

### Text Elements

```xml
<!-- Plain Text -->
<mxCell id="unique-id" value="Label Text" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="100" height="30" as="geometry" />
</mxCell>

<!-- Bold Title -->
<mxCell id="unique-id" value="Title" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#232F3D;" vertex="1" parent="1">
  <mxGeometry x="100" y="20" width="300" height="40" as="geometry" />
</mxCell>

<!-- Multi-line Text (use &#xa; for newlines) -->
<mxCell id="unique-id" value="Line 1&#xa;Line 2&#xa;Line 3" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="150" height="60" as="geometry" />
</mxCell>
```

## Common Style Properties

### Colors (use hex codes)

| Property | Purpose | Example |
|----------|---------|---------|
| `fillColor` | Background | `fillColor=#dae8fc` |
| `strokeColor` | Border | `strokeColor=#6c8ebf` |
| `fontColor` | Text | `fontColor=#232F3E` |

### AWS Color Palette

```
Compute (Orange):   fillColor=#ED7100;strokeColor=#ffffff
Storage (Green):    fillColor=#7AA116;strokeColor=#ffffff
Database (Purple):  fillColor=#C925D1;strokeColor=#ffffff
Networking (Violet):fillColor=#8C4FFF;strokeColor=#ffffff
Security (Red):     fillColor=#DD344C;strokeColor=#ffffff
Management (Pink):  fillColor=#E7157B;strokeColor=#ffffff
App Integration:    fillColor=#E7157B;strokeColor=#ffffff
```

### AWS Account Type Colors

```
Management:     fillColor=#FFF8E1;strokeColor=#FF8F00
Security/Audit: fillColor=#FCE4EC;strokeColor=#C62828
Log Archive:    fillColor=#E6F2FF;strokeColor=#147EBA
Tooling/AFT:    fillColor=#E8F5E9;strokeColor=#388E3C
Member Account: fillColor=#F3E5F5;strokeColor=#7B1FA2;dashed=1
```

### Typography

| Property | Values | Example |
|----------|--------|---------|
| `fontSize` | Number | `fontSize=12` |
| `fontStyle` | 0=normal, 1=bold, 2=italic, 3=bold+italic | `fontStyle=1` |
| `align` | left, center, right | `align=center` |
| `verticalAlign` | top, middle, bottom | `verticalAlign=middle` |

### Borders & Effects

| Property | Values | Example |
|----------|--------|---------|
| `rounded` | 0 or 1 | `rounded=1` |
| `strokeWidth` | Number | `strokeWidth=2` |
| `dashed` | 0 or 1 | `dashed=1` |
| `dashPattern` | Pattern | `dashPattern=12 4` |

## AWS Icons

AWS icons use `shape=mxgraph.aws4.resourceIcon` with `resIcon=mxgraph.aws4.SERVICE`:

```xml
<mxCell id="lambda-1" value="Lambda" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="78" height="78" as="geometry" />
</mxCell>
```

**CRITICAL**: All AWS icons MUST have `strokeColor=#ffffff` in their style string.

### Common resIcon Values

| Category | Services |
|----------|----------|
| Compute | `ec2`, `lambda`, `ecs`, `eks`, `fargate`, `batch` |
| Storage | `s3`, `elastic_block_store`, `elastic_file_system`, `fsx` |
| Database | `rds`, `dynamodb`, `aurora`, `elasticache`, `redshift`, `neptune` |
| Networking | `vpc`, `cloudfront`, `route_53`, `api_gateway`, `elastic_load_balancing`, `transit_gateway`, `direct_connect` |
| Security | `identity_and_access_management`, `cognito`, `secrets_manager`, `key_management_service`, `waf`, `shield` |
| Management | `cloudwatch`, `cloudformation`, `systems_manager`, `config`, `cloudtrail` |
| App Integration | `sns`, `sqs`, `step_functions`, `eventbridge` |
| Analytics | `kinesis`, `athena`, `glue`, `quicksight`, `emr` |
| AI/ML | `sagemaker`, `bedrock` (use generic if unavailable) |
| Migration | `database_migration_service`, `datasync`, `migration_hub` |

### AWS Group Containers

```xml
<!-- AWS Cloud -->
<mxCell id="aws-cloud" value="AWS Cloud" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud;strokeColor=#AAB7B8;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="600" height="400" as="geometry" />
</mxCell>

<!-- Region -->
<mxCell id="aws-region" value="ap-southeast-1" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#007F7F;dashed=1;" vertex="1" parent="1">
  <mxGeometry x="60" y="80" width="520" height="340" as="geometry" />
</mxCell>

<!-- VPC -->
<mxCell id="vpc" value="VPC 10.0.0.0/16" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="80" y="120" width="460" height="280" as="geometry" />
</mxCell>

<!-- Public Subnet -->
grIcon=mxgraph.aws4.group_public_subnet;strokeColor=#7AA116;fillColor=#E9F3E6

<!-- Private Subnet -->
grIcon=mxgraph.aws4.group_private_subnet;strokeColor=#00A4A6;fillColor=#E6F6F7

<!-- Availability Zone -->
grIcon=mxgraph.aws4.group_availability_zone;strokeColor=#00A4A6;fillColor=none;dashed=1

<!-- Security Group -->
grIcon=mxgraph.aws4.group_security_group;strokeColor=#DD344C;fillColor=#FFEBEE

<!-- Account -->
grIcon=mxgraph.aws4.group_account;strokeColor=#FF8F00;fillColor=#FFF8E1
```

## Diagram Patterns

### Multi-Account Layout (Landing Zone)

```
┌─────────────────────────────────────────────────────┐
│ AWS Cloud                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │
│  │ Management   │  │  Security    │  │  Log     │  │
│  │  Account     │→ │   Account    │→ │ Archive  │  │
│  └──────────────┘  └──────────────┘  └──────────┘  │
│         │                                           │
│         ▼                                           │
│  ┌──────────────┐  ┌──────────────┐                 │
│  │  Workload A  │  │  Workload B  │                 │
│  │  (Member)    │  │  (Member)    │                 │
│  └──────────────┘  └──────────────┘                 │
└─────────────────────────────────────────────────────┘
```

### Three-Tier Architecture

```
┌─────────────────────────────────────────┐
│ VPC                                     │
│  ┌─────────────────────────────────┐    │
│  │ Public Subnet                    │    │
│  │  [ALB]                          │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │ Private Subnet (App)            │    │
│  │  [ECS/EKS]                      │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │ Private Subnet (Data)           │    │
│  │  [RDS] [ElastiCache]            │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### Multi-Region DR

```
┌──────────────────┐         ┌──────────────────┐
│ Primary Region   │  ═══►   │ DR Region        │
│ (ap-southeast-1) │ Replic. │ (ap-northeast-1) │
│      🟢 Active   │         │      ⚪ Standby   │
└──────────────────┘         └──────────────────┘
         ▲                            ▲
         └────── Route 53 ────────────┘
                (Failover Routing)
```

## Best Practices

1. **Unique IDs**: Every mxCell needs a unique `id` attribute
2. **Parent hierarchy**: Set `parent="1"` for top-level elements
3. **strokeColor=#ffffff**: ALL AWS icons MUST have white stroke
4. **Z-Order**: Write edges BEFORE shapes in XML (shapes render on top)
5. **Labels**: Use full AWS service names, not abbreviations
6. **Multi-line**: Use `&#xa;` for newlines, NOT `<br>`
7. **Spacing**: 15-20px between containers, 40-80px between services
8. **A4 fit**: Max width 780px, max height 500px per diagram

## Workflow

1. Identify diagram type (Executive Overview, Network, Security, Data Flow, DR)
2. List all AWS services involved — verify icon names
3. Determine account boundaries and data flow direction
4. Set page dimensions in `mxGraphModel`
5. Write containers/groups first (AWS Cloud → Region → VPC → Subnet)
6. Write ALL edges (arrows)
7. Write ALL shapes (icons, detail boxes, labels) — renders on top of edges
8. Add legend at bottom, metadata at top-right
9. Validate: strokeColor=#ffffff on all icons, no HTML tags in labels
10. Save as `.drawio` file

## References

For detailed rules and complete icon lists, see:
- `steering/aws-architecture-diagram-rules.md` - **SA-grade diagram rules** (multi-account, arrows, validation, layout)
- `steering/architecture-patterns.md` - Common architecture diagram layouts
- `steering/style-guide.md` - Extended styling options and effects
- `steering/cloud-icons.md` - Complete AWS icon reference
- `steering/branding.md` - Company branding customisation guide
