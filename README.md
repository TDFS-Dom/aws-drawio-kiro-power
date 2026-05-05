# AWS Architecture Diagram Power for Kiro

A Kiro Power that enables AI-assisted creation of professional AWS architecture diagrams in draw.io XML format. Focused exclusively on AWS — multi-account, multi-region, Well-Architected patterns at Solutions Architect grade quality.

## What is a Kiro Power?

Kiro Powers are structured prompts and reference materials that extend Kiro's capabilities in specific domains. When this Power is loaded, Kiro gains the ability to produce valid draw.io XML for AWS architecture diagrams that can be opened directly in [draw.io](https://app.diagrams.net/).

## Features

- **AWS-focused** — All AWS service icons, account containers, VPC/subnet groups
- **SA-grade quality** — Multi-account layouts, Well-Architected patterns, proper data flow
- **Native draw.io XML** — Files open directly in draw.io desktop or web app
- **Multi-account patterns** — Landing Zone, Control Tower, Organizations layouts
- **Multi-region DR** — Active-Standby, Pilot Light, Warm Standby patterns
- **Validation rules** — Arrow routing, z-order, icon consistency checks
- **A4/document ready** — Sized for Word/PDF export

## Quick Start

### For Kiro Users

1. Add the Power:
   - Go to Powers > Add Custom Power > import from URL, folder, or build your own
   - Select git URL or local folder where you cloned this repo

2. Select the AWS Architecture Diagrams Power, click Try Power

3. In Kiro Chat, ask for AWS diagrams:

```
Create an AWS architecture diagram showing a 3-tier web application 
with ALB, ECS Fargate, and Aurora across two availability zones 
in ap-southeast-1.
```

## Hints & Tips

- Discuss architecture requirements first, ask for a text/mermaid wireframe, iterate until the design fits, then ask Kiro to generate the draw.io file
- Specify the diagram type: "Executive Overview", "Network Architecture", "Security Architecture", "Data Flow", or "DR/Multi-Region"
- Name your AWS services explicitly for accurate icon selection
- Request legends for color-coded diagrams

## Repository Structure

```
aws-drawio/
├── POWER.md                                    # Main Power definition (required)
├── README.md                                   # This file
├── icon.svg                                    # Power icon (128x128)
└── steering/
    ├── aws-architecture-diagram-rules.md       # SA-grade layout & validation rules
    ├── architecture-patterns.md                # Common diagram layouts
    ├── branding.md                             # Company colour customisation
    ├── cloud-icons.md                          # AWS icon reference (complete)
    └── style-guide.md                          # Shapes, effects, and styling
```

## Example Outputs

- **Multi-account Landing Zone** — Organizations, Control Tower, SCPs, account structure
- **Three-tier architecture** — ALB → ECS/EKS → RDS/Aurora with Multi-AZ
- **Serverless** — API Gateway → Lambda → DynamoDB with EventBridge
- **Data Lake** — S3 → Glue → Athena → QuickSight pipeline
- **Multi-region DR** — Active-Standby with Route 53 failover
- **Network architecture** — Transit Gateway, Direct Connect, VPC peering
- **Security architecture** — GuardDuty, Security Hub, KMS, WAF layers
- **CI/CD pipeline** — CodePipeline → CodeBuild → CodeDeploy → ECS

## Customising for Your Organisation

### Adding Your Brand Colours

Edit `steering/branding.md` to define your organisation's colours. The AWS diagram will use these for headers, footers, and branded zones.

### Adding Company-Specific Patterns

Add your standard architecture patterns to `steering/architecture-patterns.md`.

## Opening Generated Files

1. Kiro outputs a `.drawio` file
2. Open with:
   - [draw.io Desktop](https://www.diagrams.net/) (recommended)
   - [draw.io Web](https://app.diagrams.net/)
   - VS Code with [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension

## Licence

MIT — Use freely, attribution appreciated.

## Acknowledgements

- Based on [scarr05/claude-skills-pub](https://github.com/scarr05/claude-skills-pub/tree/main)
- [draw.io / diagrams.net](https://www.diagrams.net/)
- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
