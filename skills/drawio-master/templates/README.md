# Template Resources

## Design Specification & Outline Reference

- `design_spec_reference.md` — reference template for project-level design specs
- `spec_lock_reference.md` — machine-readable execution contract skeleton

## Diagram Layout Templates

Each template is a folder containing a `.drawio` file (multi-sheet) + `design_spec.md` (metadata + style specification):

| ID | Folder | Pages | Use Cases |
|---|---|---|---|
| `ou_hierarchy` | `ou_hierarchy/` | 1 | Organization structure, OU tree, account layout |
| `security_iam` | `security_iam/` | 4 | Security delegation, IAM, logging, incident response |
| `networking` | `networking/` | 22 | VPC topology, TGW, routing, traffic flows |
| `aft_pipeline` | `aft_pipeline/` | 16 | CI/CD pipelines, AFT account vending, automation |

### Template Folder Structure

```
templates/{template_id}/
├── design_spec.md              # Template metadata + extracted styles + page roster
└── {source_file}.drawio        # Multi-sheet reference file (READ-ONLY ground truth)
```

Comparable to PPT Master's `templates/layouts/{layout_id}/` with `design_spec.md` + SVG files.

## Template Selection Rule

Match user request to ONE template based on primary topic:

| Primary Topic | Template ID |
|---|---|
| OU, org structure, account hierarchy | `ou_hierarchy` |
| Security, IAM, GuardDuty, Config, delegation | `security_iam` |
| VPC, networking, TGW, connectivity, routing | `networking` |
| Pipeline, automation, CI/CD, deployment flow | `aft_pipeline` |
| Mixed / unclear | Pick closest match, note in Design Spec |

## Template Consumption Rules

1. **Read `design_spec.md` first** — understand page roster, layout patterns, icon/edge styles
2. **Read .drawio file** — extract exact style strings for the specific sheet being referenced
3. **NEVER modify template files** — they are READ-ONLY ground truth
4. **Copy styles exactly** — do not simplify, improve, or mix between templates
5. **Reference specific sheet** — when generating, specify which sheet pattern is being followed
