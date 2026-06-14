# AWS Drawio Power for Kiro

> AI generates SA-grade AWS architecture diagrams as native `.drawio` files.

## What it does

Describe your architecture → get back a real, editable `.drawio` file with proper AWS icons, account containers, color-coded edges, and production-grade styling.

- **Native draw.io XML** — every element clickable and editable
- **Template-matched** — styles come from 128+ pages of production reference diagrams
- **Design Spec first** — AI confirms scope before generating anything
- **No invention** — only styles from templates, never creative additions
- **Local execution** — runs in Kiro IDE, nothing uploaded

## Install

```
Kiro IDE → Powers Panel → Add Custom Power → https://github.com/TDFS-Dom/aws-drawio-kiro-power.git
```

## Usage

```
You: Vẽ diagram log aggregation từ Member Accounts qua Security Hub tới Log Archive

AI: 📐 DESIGN SPEC
    [Diagram Type]    Security / Log Aggregation
    [Template]        security_iam
    [Scope]           Member → Security Account → Log Archive (S3 buckets)
    [Accounts]        Member, Information Security, Audit, Log Archive
    [Services]        GuardDuty, Security Hub, Kinesis Firehose, KMS, S3
    [Density]         Medium (6-15 icons)
    [Output File]     Log_Aggregation.drawio

    Shall I proceed?

You: Go

AI: ✅ Diagram Complete — drawio/Log_Aggregation.drawio
```

Open output with [draw.io Desktop](https://www.diagrams.net/), [draw.io Web](https://app.diagrams.net/), or VS Code [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).

## Pipeline

```
Step 1  Request Analysis        → match template
Step 2  Design Spec ⛔          → present & wait for user confirm
Step 3  Load Styles + Brain     → read template sheets + query relevant rules
Step 4  XML Generation          → write draw.io XML (styles copied, not invented)
Step 5  Validation              → 16-point quality check
Step 6  Output                  → save .drawio to drawio/
```

## Templates

| ID | Type | Pages | When |
|---|---|---|---|
| `ou_hierarchy` | Organization | 1 | OU tree, org structure |
| `security_iam` | Security | 10 | IAM, delegation, logging, encryption |
| `networking` | Networking | 42 | VPC, TGW, DX, routing |
| `aft_pipeline` | CI/CD | 42 | Account Factory, pipelines, automation |

## Brain (Optional)

AI-powered rule retrieval via FTS5 search. When connected, AI finds the exact rules needed for each diagram instead of loading 1500+ lines of reference docs.

**Not required** — power works without it. Brain just makes edge routing smarter.

Setup: see `brain-config/README.md`

## Structure

```
aws-drawio-kiro-power/
├── POWER.md                         # Kiro Power entry
├── steering/drawio-master.md        # Activation trigger
├── skills/drawio-master/
│   ├── SKILL.md                     # Pipeline (6 steps)
│   ├── references/                  # Rules & patterns (11 files)
│   ├── templates/                   # Style source (4 templates, 95 sheets)
│   ├── scripts/                     # Validation & extraction
│   └── workflows/                   # Sub-workflows
├── brain-config/                    # Brain setup (optional)
│   ├── mcp.json                     # MCP config template
│   ├── seed-rules.py               # Ingest rules into brain
│   └── seeds/drawio-rules.db       # Pre-seeded DB (228 rules)
├── drawio/                          # Generated outputs (gitignored)
└── icon.svg
```

## Key Files

| File | Purpose |
|---|---|
| `skills/drawio-master/SKILL.md` | Core pipeline + mandatory rules |
| `skills/drawio-master/references/line-drawing-rules.md` | Edge routing (17 types + anti-patterns + pathfinding) |
| `skills/drawio-master/references/aws-icons.md` | Icon catalog + known issues |
| `skills/drawio-master/references/validation-rules.md` | Post-generation checks |
| `skills/drawio-master/templates/{id}/sheets/*.md` | Copy-paste style source |

## License

MIT
