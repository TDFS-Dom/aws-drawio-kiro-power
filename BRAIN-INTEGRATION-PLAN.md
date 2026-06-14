# Brain Integration Plan — aws-drawio-kiro-power

> **Mục tiêu**: AI tìm đúng rule khi generate diagram, không quên rule quan trọng
> **Ràng buộc**: KHÔNG share source code brain. Chỉ share binary + seeded DB + config.

---

## 1. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Kiro IDE (User's workspace)                                │
│                                                             │
│  ┌──────────────┐     MCP (stdio)     ┌──────────────────┐ │
│  │ Drawio Master │◄───────────────────►│ Brain Server     │ │
│  │ (SKILL.md)    │  brain_query()      │ (binary, local)  │ │
│  │               │  brain_store()      │                  │ │
│  │ Step 3: Load  │◄── returns rules ───│ SQLite + FTS5    │ │
│  │ Step 5: Learn │──► stores success ──│ ~/.brain/brain.db│ │
│  └──────────────┘                      └──────────────────┘ │
│                                                             │
│  aws-drawio-kiro-power/          (KHÔNG push lên git)       │
│  ├── brain/                      brain/ (gitignored)        │
│  │   └── [source code local]                                │
│  │                                                          │
│  Deliverables (PUSH lên git):                               │
│  ├── brain-config/               ← MCP config + seed script │
│  │   ├── mcp.json                ← Kiro MCP connection      │
│  │   ├── seed-rules.sh           ← Ingest rules vào brain   │
│  │   └── README.md               ← Setup guide (no source)  │
│  └── skills/drawio-master/       ← SKILL.md updated         │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Deliverables (gì PUSH lên git, gì KHÔNG)

| File/Folder | Push? | Nội dung |
|---|---|---|
| `brain-config/mcp.json` | ✅ | MCP config cho Kiro kết nối brain server |
| `brain-config/seed-rules.sh` | ✅ | Script ingest rules vào brain (gọi brain_ingest + brain_store) |
| `brain-config/README.md` | ✅ | Hướng dẫn setup brain (download binary, run seed) |
| `brain-config/seeds/drawio-rules.db` | ✅ | Pre-seeded SQLite DB (đã ingest sẵn) |
| `skills/drawio-master/SKILL.md` | ✅ | Updated pipeline (Step 3 gọi brain_query) |
| `brain/` (source code) | ❌ | Gitignored. Private. |
| Binary (`~/.brain/brain`) | ❌ | User download riêng |

---

## 3. Implementation Steps

### Phase 1: MCP Config (ngay bây giờ)

**File: `brain-config/mcp.json`**
```json
{
  "mcpServers": {
    "brain": {
      "command": "~/.brain/brain",
      "args": [],
      "env": {
        "LAMBDA_BRAIN_DB_PATH": "~/.brain/drawio-brain.db",
        "LAMBDA_BRAIN_DECAY_LAMBDA": "0.005"
      },
      "disabled": false,
      "autoApprove": ["brain_query", "brain_store", "brain_recall", "brain_context"]
    }
  }
}
```

- Decay lambda = 0.005 (chậm hơn default 0.01) — rules decay chậm vì ít thay đổi
- DB riêng: `drawio-brain.db` (không mix với brain DB khác)
- Auto-approve: AI tự query/store không cần user confirm

---

### Phase 2: Seed Script (ingest rules vào brain)

**File: `brain-config/seed-rules.sh`**

Script đọc tất cả reference files → chunk → gọi `brain_store` cho mỗi rule/pattern.

**Rules cần ingest:**

| Source File | Chunk Strategy | Importance |
|---|---|---|
| `line-drawing-rules.md` | Mỗi Part = 1 chunk, mỗi E/AP/Case = 1 chunk riêng | 4-5 |
| `aws-icons.md` | Mỗi service category = 1 chunk | 3 |
| `draw-patterns.md` | Mỗi pattern section = 1 chunk | 4 |
| `shared-standards.md` | Mỗi anti-pattern = 1 chunk | 5 |
| `validation-rules.md` | Mỗi Check = 1 chunk | 4 |
| `geometry-rules.md` | Full file = 1 chunk | 4 |

**Chunk format (mỗi rule stored as):**

```
brain_store({
  content: "[FULL rule text]",
  summary: "AP-1: Route edges outside intermediate containers. Use bypass_x = max(container.right) + 40px",
  essence: "cross-account edge intermediate container bypass route outside",
  importance: 5,
  tags: ["edge", "routing", "anti-pattern", "cross-account", "intermediate"],
  project: "drawio-master",
  memory_type: "knowledge"
})
```

**Tagging strategy:**

| Tag | Khi nào dùng |
|---|---|
| `edge` | Mọi rule liên quan line/edge |
| `routing` | Waypoints, pathfinding, exit/entry |
| `style` | Container/icon style strings |
| `anti-pattern` | Những gì KHÔNG được làm |
| `cross-account` | Multi-account patterns |
| `geometry` | Sizing, spacing, placement |
| `validation` | Post-generation checks |
| `icon` | AWS service icon shapes |
| `security` | Security category services |
| `networking` | Networking category |

---

### Phase 3: Update SKILL.md Pipeline

**Thay đổi Step 3 (Load Sheet Styles):**

```markdown
### Step 3: Load Sheet Styles + Brain Query

🚧 GATE: User confirmed Design Spec.

**3a. Read sheet styles** (unchanged):
  1. Read: templates/{template_id}/sheets_index.md
  2. Read: templates/{template_id}/sheets/{NN}_{slug}.md

**3b. Brain Query — retrieve relevant rules** (NEW):
  
  Construct query from Design Spec:
  - Services involved → tag filter
  - Cross-account? → "cross-account routing intermediate"
  - Multiple targets? → "fan-in fan-out parallel"
  - Has KMS/encryption? → "KMS scope dashed dependency"
  
  Call: brain_query(query="{constructed query}", project="drawio-master", limit=5)
  
  Apply returned rules as HARD CONSTRAINTS during XML generation.

**3c. Read generic references** (unchanged):
  3. Read: references/draw-patterns.md
  4. Read: references/shared-standards.md
```

**Thêm Step 5b (Learn from success):**

```markdown
### Step 5b: Store Success Pattern (after validation passes)

IF validation passes on first try:
  brain_store({
    content: "Generated {diagram_type} with {N} accounts, {M} edges. Pattern: {edge_types_used}. No validation errors.",
    summary: "{diagram_type}: {accounts} → {targets}, used {Case_IDs}",
    essence: "{keywords from this specific diagram}",
    importance: 4,
    tags: [extracted from diagram],
    project: "drawio-master",
    memory_type: "learning"
  })

IF validation fails → fix → passes:
  brain_store({
    content: "GOTCHA: {what went wrong} → FIX: {what fixed it}",
    summary: "Avoid: {mistake}. Use: {correct approach}",
    essence: "{error keywords}",
    importance: 5,  ← higher because it's a learned mistake
    tags: ["gotcha", ...relevant_tags],
    project: "drawio-master",
    memory_type: "learning"
  })
```

---

### Phase 4: Pre-seeded DB (zero-setup experience)

Build `seeds/drawio-rules.db` bằng cách:

```bash
# 1. Start brain server locally
~/.brain/brain

# 2. Run seed script (calls brain_store for each rule)
bash brain-config/seed-rules.sh

# 3. Copy DB file
cp ~/.brain/drawio-brain.db brain-config/seeds/drawio-rules.db

# 4. Commit seeded DB (binary file, ~500KB)
git add brain-config/seeds/drawio-rules.db
```

**Máy mới setup:**
```bash
# 1. Copy pre-seeded DB
cp brain-config/seeds/drawio-rules.db ~/.brain/drawio-brain.db

# 2. Download brain binary (from private release / internal share)
# User tự handle — README hướng dẫn

# 3. Done. Kiro IDE auto-connect qua mcp.json
```

---

## 4. Query Examples (AI sẽ gọi tự động)

| Diagram Context | brain_query | Expected Top Results |
|---|---|---|
| Cross-account log aggregation | `"cross-account edge routing intermediate container S3 bucket"` | AP-1, Case 12, pathfinding algorithm |
| KMS encryption scope | `"KMS dashed dependency scope boundary multiple targets"` | E17, AP-5, E4 |
| VPC + DNS + TGW → 1 bucket | `"fan-in multiple sources single target parallel bundle"` | Case 3b, AP-4, Grouped Arrow |
| Intra-account Security Hub chain | `"intra-account security GuardDuty Security Hub Firehose"` | E12b, AP-3 |
| OU hierarchy tree | `"OU hierarchy tree parent child organization"` | E1, ou_hierarchy template |

---

## 5. Decay Tuning (cho rules use case)

| Parameter | Value | Lý do |
|---|---|---|
| `decay_lambda` | 0.005 | Rules decay chậm (~139h half-life vs default 69h) |
| `importance` range | 3-5 | Rules = knowledge, không có low-importance |
| GC (garbage collect) | Disabled | Rules không bao giờ bị xoá |
| `explicit_save` | true cho tất cả seeds | Prevent GC |

---

## 6. Security / Privacy

| Concern | Mitigation |
|---|---|
| Brain source code leak | `brain/` gitignored, binary only |
| DB contains rules text | Rules text đã public trong repo → OK |
| Brain server network access | STDIO mode only (no SSE), no network |
| API key needed? | Không — STDIO mode không cần auth |
| User data trong brain? | Chỉ rules + AI-generated learnings |

---

## 7. Timeline

| Phase | Effort | Deliverable |
|---|---|---|
| Phase 1: MCP Config | 10 min | `brain-config/mcp.json` |
| Phase 2: Seed Script | 1-2h | `brain-config/seed-rules.sh` (parse + store all rules) |
| Phase 3: Update SKILL.md | 30 min | Step 3b + Step 5b additions |
| Phase 4: Pre-seeded DB | 15 min | `brain-config/seeds/drawio-rules.db` |
| **Total** | **~3h** | Full integration, no source shared |

---

## 8. Folder Structure (final)

```
aws-drawio-kiro-power/              ← Git repo (public)
├── skills/drawio-master/
│   ├── SKILL.md                    ← Updated (Step 3b + 5b)
│   ├── references/                 ← Rules source (brain ingests from here)
│   ├── templates/
│   └── scripts/
├── brain-config/                   ← NEW: brain setup (no source code)
│   ├── mcp.json                    ← Kiro MCP connection config
│   ├── seed-rules.sh              ← Ingest script (calls binary, not source)
│   ├── seeds/
│   │   └── drawio-rules.db        ← Pre-seeded SQLite (ready to use)
│   └── README.md                   ← Setup guide
├── drawio/                         ← Generated outputs
├── brain/                          ← GITIGNORED (source code, private)
├── .gitignore
└── POWER.md
```

---

## 9. Tiếp theo

Confirm plan → tôi implement Phase 1-4 ngay.
