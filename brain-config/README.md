# Brain Integration — Setup Guide

> Optional enhancement: AI tìm đúng rule khi generate diagram.
> Không có brain → power vẫn hoạt động bình thường.

## Prerequisites

- Brain binary (`~/.brain/brain`) — liên hệ admin để nhận file
- macOS ARM (M1/M2/M3) hoặc Intel

## Setup (1 lần duy nhất)

### 1. Place binary

```bash
mkdir -p ~/.brain
cp /path/to/brain ~/.brain/brain
chmod +x ~/.brain/brain
```

### 2. Copy pre-seeded DB

```bash
cp brain-config/seeds/drawio-rules.db ~/.brain/brain.db
```

### 3. Add MCP config

Copy `brain-config/mcp.json` vào **user-level** Kiro MCP config:

```bash
# Mở file config
open ~/.kiro/settings/mcp.json

# Merge nội dung brain-config/mcp.json vào đó
```

Hoặc nếu chưa có file:
```bash
mkdir -p ~/.kiro/settings
cp brain-config/mcp.json ~/.kiro/settings/mcp.json
```

### 4. Verify

Restart Kiro → check MCP Servers panel → "brain" should show green.

## Re-seed (khi rules update)

```bash
bash brain-config/seed-rules.sh
```

## Multi-project

Brain DB dùng chung cho nhiều powers. Mỗi power dùng `project` filter riêng:

| Power | Project ID |
|---|---|
| aws-drawio-kiro-power | `drawio-master` |
| iac-tfsec-aws-power | `iac-tfsec` |
| ba-kit-power | `ba-kit` |
| qa-testing-kit | `qa-testing` |

## Troubleshooting

| Issue | Fix |
|---|---|
| Brain server not found | Verify `~/.brain/brain` exists + executable |
| Empty query results | Run `seed-rules.sh` lại |
| Permission denied | `chmod +x ~/.brain/brain` |
| Port conflict | Brain dùng stdio (không cần port) |
