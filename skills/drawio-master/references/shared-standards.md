# Shared Diagram Standards

> Extracted from 4 reference .drawio template files (128+ pages). This is the SINGLE SOURCE OF TRUTH for all styles.
> NEVER invent styles. ONLY use what's documented here.

---

## Container Styles

| Type | grIcon | strokeColor | fillColor | fontColor | dashed |
|------|--------|-------------|-----------|-----------|--------|
| Account | `mxgraph.aws4.group_account` | `#CD2264` | `none` | `#CD2264` | 0 |
| Region | `mxgraph.aws4.group_region` | `#00A4A6` | `none` | `#147EBA` | 1 |
| VPC | `mxgraph.aws4.group_vpc2` | `#00CC00` | `none` | `#AAB7B8` | 0 |
| On-premise (DC) | `mxgraph.aws4.group_corporate_data_center` | `#7D8998` | `none` | `#5A6C86` | 0 |
| On-premise (generic) | `mxgraph.aws4.group_on_premise` | `#858B94` | `none` | `#858B94` | 0 |
| OU boundary (dashed box) | — | `#5A6C86` | `none` | `#5A6C86` | 1 |
| Step Functions | `mxgraph.aws4.group_aws_step_functions_workflow` | `#CD2264` | `none` | `#CD2264` | 0 |

## Icon Category Colors

| Category | fillColor | gradientColor | strokeColor |
|----------|-----------|---------------|-------------|
| Networking | `#8C4FFF` | — | `#ffffff` |
| Security (GuardDuty, Security Hub) | `#C7131F` | `#F54749` | `#ffffff` |
| Security (standalone shapes) | `#DD344C` | — | `none` |
| IAM Access Analyzer | `#FF5252` | — | `none` |
| Management (Config, Organizations) | `#BC1356` | `#F34482` | `#ffffff` |
| Management/App Integration | `#E7157B` | — | `#ffffff` |
| Compute (Lambda) | `#ED7100` | — | `#ffffff` |
| Developer Tools (CodeBuild, CodePipeline) | `#C925D1` | — | `#ffffff` |
| Storage (S3) | `#7AA116` | — | `none` |
| Organizations (all org shapes) | `#BC1356` | — | `none` |
| General/Third-party | `#232F3D` | — | `none` |
| External tools (user groups) | `#505050` | — | `none` |

## Edge Colors

### Architecture Diagrams (default for most templates)

Color edges by **source service AWS category**:

| Edge Purpose | strokeColor | strokeWidth | dashed | When |
|---|---|---|---|---|
| Networking data flow | `#8C4FFF` | 2 | 0 | VPC Flow Logs, DNS, TGW → destination |
| Security data flow | `#C7131F` | 2 | 0 | GuardDuty, Security Hub → destination |
| Management data flow | `#BC1356` | 2 | 0 | S3 Replication, Config → destination |
| Compute data flow | `#ED7100` | 2 | 0 | Lambda, Step Functions → destination |
| DevTools data flow | `#C925D1` | 2 | 0 | CodePipeline, CodeBuild → destination |
| Encryption/dependency | `#DD344C` | 1 | 1 | KMS → encrypted resources |
| Hierarchy (OU tree) | default (black) | 1 | 0 | Parent → child org nodes |

### AFT Pipeline Template Only (swimlane phases)

These colors apply ONLY to `aft_pipeline` template diagrams with phase swimlanes:

| Connection Type | strokeColor | fillColor | strokeWidth | endArrow |
|---|---|---|---|---|
| DX / TGW (orange) | `#D79B00` | `#d5e8d4` or `#ffe6cc` | 2 | none |
| Shared Services (blue) | `#6c8ebf` | `#dae8fc` | 2 | none |
| Prod (green) | `#82B366` | `#d5e8d4` | 2 | none |
| Default hierarchy | default | — | 1 | classic |
| Yellow milestone | `#d6b656` | `#fff2cc` | 3 | classic (dashed) |
| Green milestone | `#82b366` | `#d5e8d4` | 3 | classic (dashed) |
| Standard process | default | — | 2 | classic |

## Swimlane Phase Colors

| Phase | fillColor | strokeColor |
|---|---|---|
| Request (Yellow) | `#fff2cc` | `#d6b656` |
| Provisioning (Blue) | `#dae8fc` | `#6c8ebf` |
| Customization (Green) | `#d5e8d4` | `#82b366` |

## Environment Label Colors

| Env | Color |
|-----|-------|
| Prod | `rgb(0,204,0)` green |
| NonProd | `rgb(0,0,255)` blue |
| Standard | `#232F3E` |

## Font Standards

| Element | fontSize | fontStyle | fontColor |
|---------|----------|-----------|-----------|
| Diagram title | 24 | 1 (bold) | default |
| Account container label | 16 | 0 | `#CD2264` |
| VPC label | 15 | 1 (bold) | `rgb(0,0,0)` override |
| AWS icon label | 12 | 0 | `#232F3E` |
| OU/Account name | 12 | 1 (bold) | `#232F3E` |
| Edge label | 12 | 1 (bold) | default |
| Small annotation | 10 | 1 (bold) | default |

## Layout Rules

1. Grid: always ON (10px)
2. Shadow: always OFF
3. All edges: `edgeStyle=orthogonalEdgeStyle;rounded=0` (NO EXCEPTIONS — omitting `edgeStyle` causes diagonal lines)
4. Hierarchy: top→bottom (OU) or hub-spoke (networking)
5. No text overlap
6. Containers must fully enclose children
7. XML order: containers → edges → shapes
8. Cross-account edges: use exit/entry points for predictable routing

## Anti-patterns (FORBIDDEN)

- ❌ shadow="1"
- ❌ Curved edges (rounded=1 on edges)
- ❌ flowAnimation=1
- ❌ flexArrow shapes
- ❌ Colored fill on VPC/Region containers
- ❌ Custom fonts
- ❌ Emoji in labels
- ❌ Inventing new colors not listed above
- ❌ Auto-generated text annotations from spec documents (see AP-TEXT below)

### AP-TEXT — No Auto-Generated Text Annotations from Source Documents

> **Research basis**: Production observation — AI reads spec documents containing numbered flow descriptions (①②③④⑤⑥) and explanatory text, then copies them into the diagram as floating text cells. This clutters the diagram with content that belongs in the document, not in the visual.

**Problem**: When the source document (LLD/HLD chapter) uses numbered annotations like "① VPC Flow Logs deliver to network bucket via delivery.logs.amazonaws.com" to explain the architecture, AI auto-generates these as `text;html=1` cells inside the diagram. The diagram becomes cluttered with paragraph-level descriptions that duplicate the document.

**Rule**: Diagrams contain ONLY:
1. AWS service icons (with short labels: service name only)
2. Account/Region/VPC containers (with standard labels)
3. Edges (with optional SHORT edge labels — max 3-4 words)
4. Legend (if needed)

**FORBIDDEN in diagram output:**
- Numbered step descriptions (①②③④⑤⑥ or 1. 2. 3.)
- Writer/principal annotations ("delivery.logs.amazonaws.com", "aws:SourceOrgID condition")
- Policy descriptions ("DenyUnencryptedTransport", "Object Lock: Enabled")
- Replication role names as floating text ("acb-s3-replication-cloudtrail")
- Any text that explains HOW the architecture works (that belongs in the document)

**ALLOWED as edge labels (short):**
- "S3 Replication" (on replication edge)
- "Export" (on GuardDuty → S3 edge)
- "Firehose delivery" (on Firehose → S3 edge)

**Anti-pattern:**
❌ Adding text cell: "① delivery.logs.amazonaws.com with aws:SourceOrgID condition"
❌ Adding text cell: "SSE-KMS / Object Lock: Enabled / Versioning: Enabled"
❌ Adding text cell: "④ S3 Replication from CT Audit bucket"
✅ Edge label: "S3 Replication" (short, on the edge itself)
✅ No text cells — let the diagram be clean; explanations live in the document
