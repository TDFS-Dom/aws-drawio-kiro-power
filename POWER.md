---
name: "aws-drawio"
displayName: "AWS Architecture Diagrams"
description: "Create professional AWS architecture diagrams in draw.io XML format — multi-account, Well-Architected, SA-grade quality"
keywords: ["aws", "drawio", "architecture", "diagram", "cloud", "vpc", "multi-account", "well-architected", "solutions-architect", "draw.io"]
icon: "icon.svg"
---

# AWS Architecture Diagram Power

Create professional, SA-grade AWS architecture diagrams in draw.io's native XML format.
Focused exclusively on AWS — multi-account, multi-region, Well-Architected patterns.

## This is a tool, not a wishing well

Don't expect it to hand you a finished, perfect diagram in one shot. Its real value
is taking most of the tedious XML work off your plate; the polishing that's left is
yours — a native .drawio file exists precisely so you can keep editing it in draw.io,
not a flat image you can't touch.

## How it works

Drawio Master is a workflow (a "skill") that works inside Kiro IDE. You chat with
the AI — "draw the LiteLLM gateway architecture" — and it follows a strict pipeline
to produce a real editable `.drawio` on your computer. No coding on your side; the
IDE is just where the conversation happens.

## Quick Start

1. Ask for a diagram in Kiro Chat
2. AI presents a **Design Spec** for confirmation (template, scope, services, layout)
3. You confirm or adjust
4. AI generates the `.drawio` file following exact template standards

```
You: Vẽ diagram cho network connectivity giữa on-prem và AWS qua Transit Gateway

AI: 📐 DESIGN SPEC
    [Diagram Type]    Network Design
    [Template]        ACB_Networking_diagrams .drawio
    [Scope]           On-prem → DX → TGW → VPCs (hub-spoke)
    ...
    Shall I proceed with this spec?

You: Go

AI: ✅ Diagram Complete — projects/ACB_Network_Connectivity.drawio
```

## Pipeline

The full execution pipeline is defined in `skills/drawio-master/SKILL.md`. Key rules inline:

### 🚨 EXECUTION DISCIPLINE

**You are NOT a designer. You are a COPIER.** Every style string in output XML MUST come from `skills/drawio-master/templates/{id}/sheets/*.md`.

**FORBIDDEN:**
- ❌ `rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc` ← use AWS group containers
- ❌ `shape=document` / `shape=hexagon` / `shape=cylinder3` ← use `mxgraph.aws4.*`
- ❌ Colors `#dae8fc`, `#d5e8d4`, `#fff2cc` ← use `#CD2264`, `#8C4FFF`, `#BC1356`
- ❌ `rounded=1` on edges ← always `rounded=0`

**Pipeline:**
```
Step 1: Request Analysis        → match template
Step 2: Design Spec ⛔ BLOCKING → present & wait for user OK
Step 3: Load Sheet Styles       → read templates/{id}/sheets/{NN}.md
Step 4: XML Generation          → copy styles from sheet file
Step 5: Validation              → python3 scripts/validate_drawio.py
Step 6: Output                  → save to projects/
```

**Full pipeline definition**: `skills/drawio-master/SKILL.md`

## Opening Generated Files

- [draw.io Desktop](https://www.diagrams.net/) (recommended)
- [draw.io Web](https://app.diagrams.net/)
- VS Code with [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension

## Reference Templates

4 production-grade diagrams serve as ground truth (128+ pages total):

| Template | Type | Pages |
|---|---|---|
| OU Design | Organization hierarchy | 1 |
| Security & IAM Design | Security services delegation | 10 |
| Networking Diagrams | VPC, TGW, connectivity | 42 |
| AFT Pipeline | Account vending, CI/CD | 42 |

## Repository Structure

```
aws-drawio-kiro-power/
├── skills/drawio-master/
│   ├── SKILL.md                      # Core pipeline definition
│   ├── references/                   # Technical docs (AI reads on-demand)
│   │   ├── acb-standards.md          # Visual standards + anti-patterns
│   │   ├── aws-icons.md              # AWS icon catalog
│   │   ├── validation-rules.md       # Post-draw validation rules
│   │   ├── strategist.md             # Strategist role definition
│   │   ├── executor-base.md          # Executor role definition
│   │   ├── branding.md               # Company colours
│   │   ├── architecture-patterns.md  # Layout patterns
│   │   └── style-guide.md            # Extended styling
│   ├── scripts/                      # Automation scripts
│   │   ├── extract_styles.py         # Extract styles per-sheet → sheets/ folder
│   │   ├── validate_drawio.py        # 8-point XML validation
│   │   ├── project_manager.py        # Project init/validate
│   │   └── template_fill.py          # Clone + replace content
│   ├── templates/                    # Reference templates (ground truth)
│   │   ├── {template_id}/
│   │   │   ├── design_spec.md        # Template overview + patterns
│   │   │   ├── sheets_index.md       # Sheet name → file lookup
│   │   │   ├── sheets/              # 1 file per sheet (copy-paste styles)
│   │   │   │   ├── 01_hld.md
│   │   │   │   ├── 02_xxx.md
│   │   │   │   └── ...
│   │   │   └── *.drawio              # Source file (READ-ONLY)
│   │   ├── design_spec_reference.md  # Project spec template
│   │   └── spec_lock_reference.md    # Execution contract template
│   └── workflows/                    # Standalone sub-workflows
│       ├── design-spec.md
│       └── template-fill-drawio.md
├── steering/                         # Kiro Power steering files
│   └── drawio-master.md              # Entry point → SKILL.md
├── projects/                         # Generated diagram outputs
├── POWER.md                          # This file (Kiro Power entry)
├── README.md                         # User-facing readme
├── icon.svg
└── .gitignore
```

## Key Principles

- **Template-matched** — Every diagram matches an existing production template exactly
- **Design Spec first** — AI confirms spec before writing any XML
- **No invention** — Only styles from reference files, never creative additions
- **Validation built-in** — Post-draw checks catch strokeColor, overlap, z-order issues
- **Natively editable** — Output is real draw.io XML, not images
