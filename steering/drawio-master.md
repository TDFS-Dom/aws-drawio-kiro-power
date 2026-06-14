# Drawio Master — Kiro Steering Entry Point

When the user asks to create, draw, or modify an AWS architecture diagram, you MUST follow the Drawio Master skill pipeline.

## Activation Triggers

Activate this skill when user mentions any of:
- "create diagram", "draw architecture", "vẽ diagram", "vẽ kiến trúc"
- "drawio", "draw.io", "architecture diagram"
- "OU design", "security diagram", "network diagram", "pipeline diagram"
- "VPC", "Transit Gateway", "Landing Zone" (in context of drawing)

## 🧠 Brain Rule Search (DO THIS BEFORE generating XML)

**At Step 3 — AFTER reading sheet styles, BEFORE writing XML:**

Call `brain_query` with keywords extracted from the diagram request. This retrieves the EXACT rules needed for THIS diagram.

```
brain_query(query="{2-3 keywords from diagram context}", project="drawio-master", limit=5)
```

**Keyword selection guide:**
| Diagram involves... | Query keywords |
|---|---|
| Cross-account edges | `routing intermediate bypass` |
| Multiple sources → 1 target | `fan-in stagger entry` |
| KMS / encryption | `KMS encryption scope` |
| Security Hub / GuardDuty | `security intra-account E12b` |
| Log aggregation / S3 buckets | `trunk vertical branch` |
| Parallel edges same direction | `lane offset parallel` |
| Edge routing general | `algorithm route edge` |
| Anti-patterns check | `anti-pattern violation` |

**Returned rules are HARD CONSTRAINTS** — apply them during XML generation.

If `brain_query` is not available (tool not found) → skip and proceed with file reading only.

## Entry Point

**Read and follow**: `skills/drawio-master/SKILL.md`

This file defines the complete 6-step pipeline:
1. Request Analysis
2. Design Spec Confirmation ⛔ (BLOCKING — wait for user)
3. Reference Loading + Brain Query
4. XML Generation (hand-write using template styles)
5. Validation (run script)
6. Output (save .drawio)

## Critical Rules

- **NEVER** generate draw.io XML without completing Step 2 (Design Spec confirmation)
- **NEVER** invent styles — only use what's extracted from template sheets
- **ALWAYS** call `brain_query` before XML generation (Step 3) if the tool is available
- **ALWAYS** read the specific sheet file from `templates/{id}/sheets/` before generating
- **ALWAYS** run `validate_drawio.py` after generation
- Output saves to `drawio/` directory

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
