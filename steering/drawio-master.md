# Drawio Master — Kiro Steering Entry Point

When the user asks to create, draw, or modify an AWS architecture diagram, you MUST follow the Drawio Master skill pipeline.

## Activation Triggers

Activate this skill when user mentions any of:
- "create diagram", "draw architecture", "vẽ diagram", "vẽ kiến trúc"
- "drawio", "draw.io", "architecture diagram"
- "OU design", "security diagram", "network diagram", "pipeline diagram"
- "VPC", "Transit Gateway", "Landing Zone" (in context of drawing)

## Entry Point

**Read and follow**: `skills/drawio-master/SKILL.md`

This file defines the complete 6-step pipeline:
1. Request Analysis
2. Design Spec Confirmation ⛔ (BLOCKING — wait for user)
3. Reference Loading (read specific sheet styles)
4. XML Generation (hand-write using template styles)
5. Validation (run script)
6. Output (save .drawio)

## Critical Rules

- **NEVER** generate draw.io XML without completing Step 2 (Design Spec confirmation)
- **NEVER** invent styles — only use what's extracted from template sheets
- **ALWAYS** read the specific sheet file from `templates/{id}/sheets/` before generating
- **ALWAYS** run `validate_drawio.py` after generation
- Output saves to `projects/` directory

## Quick Reference

| Template | When to use |
|---|---|
| `ou_hierarchy` | Organization structure, OU tree |
| `security_iam` | Security services, IAM, delegation |
| `networking` | VPC, TGW, routing, connectivity |
| `aft_pipeline` | CI/CD, automation, pipelines |

## File Reference

All skill files are relative to this power's root directory:

```
skills/drawio-master/SKILL.md              ← Full pipeline (THIS content below)
skills/drawio-master/references/           ← Technical docs
skills/drawio-master/templates/{id}/       ← Template folders
skills/drawio-master/templates/{id}/sheets/ ← Per-sheet style files
skills/drawio-master/scripts/              ← Validation scripts
```

**To find SKILL.md**: it is at `skills/drawio-master/SKILL.md` relative to the workspace root where this power is installed.
