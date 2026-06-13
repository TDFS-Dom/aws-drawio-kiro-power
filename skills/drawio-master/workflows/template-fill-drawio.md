---
description: Draw.io template fill workflow — use an existing .drawio diagram as template, keep layout/style intact, replace content (account names, services, labels, connections) without recreating from scratch
---

# Template Fill (Draw.io) Workflow

> Run when the user wants to fill new content into an existing diagram. Typical requests include "use this diagram but change the account names", "copy this layout for our new project", or "reuse this design with different services". They provide an existing `.drawio` as a native template and want the content filled back into that layout while keeping the visual design intact.

This workflow is **independent** from the full generation pipeline. It treats the source .drawio as a native template, keeps the original layout/style intact, and writes a new `.drawio` by cloning the source and replacing content directly in XML.

## When to Run

Recognize any request that combines an existing diagram with new content, for example:

| Pattern | Example |
|---|---|
| Existing `.drawio` + content swap | "Use this diagram but change account names to our project" |
| Existing `.drawio` + service replacement | "Same layout but replace GuardDuty with Inspector" |
| Existing `.drawio` + selective reuse | "Only keep the networking page, drop the rest" |
| Existing `.drawio` + label replacement | "Keep the design, just update all labels to English" |
| Clone + modify | "Copy the OU Design but add a new AI Services OU" |
| Direct wording | "Fill this diagram with our new account structure" |

**Hard rule**: Do NOT run the full pipeline (Design Spec → Reference Loading → XML Generation). This workflow directly edits existing XML.

---

## Step 1: Inputs

🚧 **GATE**: The user has provided:

| Input | Required | Notes |
|---|---:|---|
| Source .drawio file | Yes | Original diagram to reuse as template |
| Content changes | Yes | New account names, service list, labels, connections |
| Scope | Optional | Which pages to keep, which to modify, which to drop |

If content changes are unclear, ask: what accounts? what services? what labels change?

---

## Step 2: Analyze Source Diagram

1. Read the source .drawio file
2. List all pages (`<diagram name="...">`)
3. For each page, identify:
   - Container elements (accounts, regions, VPCs)
   - Service icons (with current labels)
   - Edge connections (source → target)
   - Text/label elements
4. Present a summary:

```
📋 SOURCE DIAGRAM ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━

File: {filename}
Pages: {N}

Page 1: {name}
  - Containers: {list}
  - Services: {list}
  - Connections: {N} edges

Changes needed:
  - [ ] {change 1}
  - [ ] {change 2}
  - ...

Shall I proceed with these changes?
```

⛔ **BLOCKING** — Wait for user confirmation.

---

## Step 3: Clone & Modify

1. Copy the entire source .drawio XML
2. For each confirmed change:
   - **Label replacement**: Find `value="old text"` → replace with new text
   - **Service swap**: Change `resIcon=mxgraph.aws4.{old}` → `resIcon=mxgraph.aws4.{new}`, update fillColor if category changes
   - **Add element**: Insert new mxCell following exact style from existing elements in same diagram
   - **Remove element**: Delete mxCell + connected edges
   - **Add page**: Clone existing `<diagram>` block, modify content
3. Preserve ALL styles — do NOT change any style strings unless the service category changes

**Critical rules:**
- Keep same IDs for unchanged elements
- Generate new unique IDs for added elements
- Update edge source/target when elements are moved/replaced
- Maintain parent hierarchy
- Keep container sizes — expand ONLY if new content doesn't fit

---

## Step 4: Validate

Run same 8-point validation as main pipeline:

| # | Check |
|---|---|
| 1 | `strokeColor=#ffffff` on all resourceIcon shapes |
| 2 | No HTML tags in value="" |
| 3 | No text overlap |
| 4 | No broken edges (source/target IDs still valid) |
| 5 | Z-order correct |
| 6 | Labels visible |
| 7 | Containers enclose children |
| 8 | Styles unchanged from source (unless intentional category swap) |

---

## Step 5: Output

Save to `projects/{new_filename}.drawio`.

```
## ✅ Template Fill Complete
- [x] Source: {source_file} ({N} pages)
- [x] Changes applied: {N} modifications
- [x] Validation passed
- [x] Output: projects/{new_filename}.drawio

Styles preserved from source. Open with draw.io to verify.
```

---

## Rules

- NEVER change styles unless service category changes
- NEVER restructure layout — only swap content
- NEVER add elements with styles not present in the source file
- ALWAYS preserve existing spacing, positions, container sizes
- ALWAYS validate edge connections after modifications
- If adding new elements → copy style from MOST SIMILAR existing element in same file
