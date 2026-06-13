# Scripts

Utility scripts for draw.io diagram workflow automation.

## Pipeline Scripts

| Script | Purpose | When to use |
|--------|---------|-------------|
| `extract_styles.py` | Extract style strings from template .drawio → `styles.md` | Step 3: Reference Loading (run once, or `--all` for all templates) |
| `validate_drawio.py` | Post-draw XML validation (8-point check) | Step 5: Validation |
| `project_manager.py` | Project init / validate / manage | Step 1: create project workspace |
| `template_fill.py` | Clone .drawio and replace content | template-fill-drawio workflow |

## Usage

```bash
# Extract styles from ALL templates (generates styles.md in each folder)
python3 ${SKILL_DIR}/scripts/extract_styles.py --all

# Extract styles from a single template
python3 ${SKILL_DIR}/scripts/extract_styles.py templates/networking/ACB_Networking_diagrams\ .drawio --output styles.md

# Validate a generated .drawio file
python3 ${SKILL_DIR}/scripts/validate_drawio.py drawio/my_diagram.drawio

# Auto-fix validation errors
python3 ${SKILL_DIR}/scripts/validate_drawio.py drawio/my_diagram.drawio --fix

# Create a new project
python3 ${SKILL_DIR}/scripts/project_manager.py init my_project

# Fill template with new content
python3 ${SKILL_DIR}/scripts/template_fill.py source.drawio --changes changes.json --output new.drawio
```

> Windows note: if `python3` fails, use `python` instead.
