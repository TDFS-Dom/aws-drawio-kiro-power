# Workflow: Design Spec Confirmation

## Purpose

Mandatory workflow before any diagram generation. Ensures AI confirms scope, template, and styling with user before writing XML.

## Trigger

User asks to create/draw/vẽ a diagram.

## Flow

```
User request → Parse intent → Match template → Present Design Spec ⛔ → User confirms → Output spec files
```

---

## Step 1: Parse Intent

From user request, extract:
- What type of architecture? (OU / Security / Networking / Pipeline)
- What AWS services mentioned?
- What accounts/environments?
- What scope? (single diagram / multi-page)

## Step 2: Match Template

Use `templates/README.md` selection table:

| Primary Topic | Template ID | File |
|---|---|---|
| OU, org hierarchy | `ou-hierarchy` | `ou-design.drawio` |
| Security, IAM | `security-iam` | `security-iam-design.drawio` |
| VPC, networking, TGW | `networking` | `networking-diagrams.drawio` |
| Pipeline, CI/CD, automation | `aft-pipeline` | `AFT.drawio` |

## Step 3: Present Design Spec

⛔ **BLOCKING** — Present and wait for confirmation:

```
📐 DESIGN SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Diagram Type]    {type}
[Template]        {file}
[Canvas]          {dimensions}
[Scope]           {description}
[Accounts]        {list}
[Services]        {list with verified icon names}
[Flow Direction]  {direction}
[Edge Style]      {colors + rules}
[Pages]           {N}
[Output File]     {filename.drawio}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Shall I proceed with this spec?
```

## Step 4: Handle Response

| User Response | Action |
|---|---|
| "OK" / "Go" / "Proceed" | Write design_spec.md + spec_lock.md → proceed to Executor |
| Requests changes | Update spec, present again |
| Asks questions | Answer, keep spec pending |

## Step 5: Output Spec Files

Write to `drawio/{project_name}/`:
- `design_spec.md` — from `templates/design_spec_reference.md`
- `spec_lock.md` — from `templates/spec_lock_reference.md`

---

## Rules

- NEVER skip this workflow
- NEVER generate XML before user confirms
- ALWAYS verify icon names before presenting spec
- ALWAYS match to exactly ONE template
- NEVER mix styles between templates
