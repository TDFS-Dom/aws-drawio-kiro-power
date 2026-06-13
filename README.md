# Drawio Master — AI generates professional AWS architecture diagrams from requirements

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

English | [Tiếng Việt](#)

> **This is a tool, not a wishing well.**
>
> Don't expect it to hand you a finished, perfect diagram in one shot. Its real value
> is taking most of the tedious draw.io XML work off your plate; the polishing that's
> left is yours — a natively editable .drawio file exists precisely so you can keep
> working on it in draw.io Desktop, not a flat image you can't touch.

## What it does

Drop in your architecture requirements and get back a real draw.io file: directly
editable, with proper AWS icons, account containers, VPC groups, color-coded
connections, and matching your organisation's existing diagram standards exactly.

**Drawio Master is different:**

- **Real draw.io XML** — if a file can't be opened and edited in draw.io, it shouldn't be called a diagram. Every element is directly clickable and editable
- **Template-matched** — diagrams match your existing production standards (4 reference files, 128+ pages of ground truth)
- **Design Spec first** — AI confirms scope, services, and layout BEFORE generating anything
- **No invention** — only styles extracted from your reference templates, never creative additions
- **Data stays local** — everything runs in your IDE, no uploads to external servers

## Quick Start

### 1. Prerequisites

- [Kiro IDE](https://kiro.dev/) installed
- This power added to Kiro (via git URL or local folder)

### 2. Set Up

```bash
git clone https://github.com/TDFS-Dom/aws-drawio-kiro-power.git
```

Or add directly in Kiro: Powers → Add Custom Power → Git URL.

### 3. Create

Tell Kiro what diagram you need:

```
You: Vẽ diagram network connectivity từ on-prem qua Transit Gateway tới các VPCs

AI: 📐 DESIGN SPEC
    [Diagram Type]    Network Design
    [Template]        ACB_Networking_diagrams .drawio (HLD sheet)
    [Canvas]          850×1100, grid=10
    [Scope]           On-prem DC → Direct Connect → Transit Gateway → VPCs
    [Accounts]        Network Account
    [Services]        Transit Gateway, Direct Connect, VPC, NAT Gateway, IGW
    [Flow Direction]  Left→Right (On-prem → AWS)
    [Edge Style]      Orange (#D79B00) = DX connections, Green (#82B366) = Prod
    [Pages]           1
    [Output File]     ACB_Network_HLD.drawio

    Shall I proceed with this spec?

You: Go

AI: ✅ Diagram Complete — projects/ACB_Network_HLD.drawio
```

**Output:** `.drawio` file saved to `projects/`. Open with draw.io Desktop (recommended).

### 4. Opening Generated Files

- [draw.io Desktop](https://www.diagrams.net/) (recommended)
- [draw.io Web](https://app.diagrams.net/)
- VS Code with [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension

## Pipeline

The AI follows a strict serial pipeline — no shortcuts, no speculative execution:

```
Step 1: Request Analysis          — Parse intent, identify template
Step 2: Design Spec Confirmation  — ⛔ BLOCKING — user must confirm
Step 3: Reference Loading         — Load template styles
Step 4: XML Generation            — Hand-write draw.io XML
Step 5: Validation                — 8-point quality check
Step 6: Output                    — Save .drawio file
```

Full pipeline definition: `skills/drawio-master/SKILL.md`

## Reference Templates

4 production-grade diagrams serve as the **single source of truth** for all generated diagrams:

| Template | Type | Pages | Use When |
|---|---|---|---|
| `ACB _ OU Design 1.drawio` | OU Hierarchy | 1 | Organization structure, OU tree |
| `ACB-SWO_AWS LZ_Security and IAM Design_20260317.drawio` | Security | 10 | Security delegation, IAM, logging |
| `ACB_Networking_diagrams .drawio` | Networking | 42 | VPC, TGW, routing, connectivity |
| `AFT.drawio` | Process/Flow | 42 | Account vending, CI/CD, automation |

## Repository Structure

```
aws-drawio-kiro-power/
├── skills/drawio-master/
│   ├── SKILL.md                     # Core pipeline definition
│   ├── references/                  # Technical docs (AI reads on-demand)
│   │   ├── acb-standards.md         # Extracted styles from templates
│   │   ├── aws-icons.md             # AWS icon catalog
│   │   ├── validation-rules.md      # Post-draw validation
│   │   ├── branding.md              # Company colours
│   │   ├── architecture-patterns.md # Layout patterns
│   │   └── style-guide.md           # Extended styling
│   ├── templates/                   # Reference .drawio files (ground truth)
│   │   ├── templates_index.md
│   │   └── *.drawio (4 files)
│   └── workflows/                   # Standalone sub-workflows
│       └── design-spec.md
├── projects/                        # Generated diagram outputs
├── examples/                        # Example outputs
├── docs/                            # Documentation
├── POWER.md                         # Kiro Power entry point
├── README.md                        # This file
├── icon.svg
└── .gitignore
```

## Documentation

| | Doc | Description |
|---|---|---|
| 📘 | `skills/drawio-master/SKILL.md` | Core workflow and rules |
| 📐 | `skills/drawio-master/templates/templates_index.md` | Template selection guide |
| 🎨 | `skills/drawio-master/references/acb-standards.md` | Visual standards reference |
| 🔍 | `skills/drawio-master/references/aws-icons.md` | AWS icon catalog |
| ✅ | `skills/drawio-master/references/validation-rules.md` | Validation checklist |

## The person using it matters more

The reference diagrams were made by experienced Solutions Architects. With the same
draw.io, an SA can produce something stunning while most people only ever touch basic
shapes. The difference isn't the tool, it's the person using it. If you can't get
there yet, it's most likely that you haven't learned the workflow — start with the
pipeline in SKILL.md and the template files.

## Contributing

Issues and PRs welcome. When contributing:
- Follow existing template styles — no creative additions
- Test with draw.io Desktop before submitting
- Keep reference files as ground truth

## License

[MIT](LICENSE) — Use freely, attribution appreciated.

## Acknowledgements

- [draw.io / diagrams.net](https://www.diagrams.net/)
- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
- [awsfundamentals.com/aws-icons](https://awsfundamentals.com/aws-icons) — External SVG icon source
- Inspired by [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) pipeline architecture
