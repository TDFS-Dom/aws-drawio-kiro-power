# Line Drawing Rules — draw.io AWS Architecture Diagrams

> **Research basis**: 949 edges từ 4 production `.drawio` files + visual analysis 44 exported PNG pages  
> **Source files**: AFT.drawio (362 edges), ACB_Networking (429), ACB_Security_IAM (128), ACB_OU_Design (30)

---

## PART 1: MANDATORY BASE — Không ngoại lệ

### Rule L1: edgeStyle BẮT BUỘC trên mọi edge

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

- **97.4% edges trong production** (924/949) dùng `edgeStyle=orthogonalEdgeStyle`
- Thiếu `edgeStyle` → draw.io dùng straight line cắt chéo qua container → **LỖI HIỂN THỊ**
- `rounded=0` LUÔN đi kèm — **KHÔNG BAO GIỜ** `rounded=1` trên edge

### Rule L2: Thứ tự attributes trong style string

```
edgeStyle=orthogonalEdgeStyle;     ← luôn đầu tiên
rounded=0;                          ← luôn thứ hai
orthogonalLoop=1;                   ← luôn thứ ba
jettySize=auto;                     ← luôn thứ tư
html=1;                             ← luôn có mặt
[strokeWidth=N;]                    ← sau html=1
[strokeColor=#XXXXXX;]             ← sau strokeWidth
[dashed=1;]                        ← sau strokeColor
[exitX=N;exitY=N;exitDx=0;exitDy=0;]    ← nhóm exit
[entryX=N;entryY=N;entryDx=0;entryDy=0;] ← nhóm entry
```

### Rule L3: html=1 BẮT BUỘC

`html=1` phải có trong mọi edge style. Đây là official draw.io requirement.

---

## PART 2: CATALOG 15 LOẠI EDGE (copy-paste)

> Chọn đúng loại dựa trên semantic, KHÔNG chọn theo màu đẹp.

### E1 — Hierarchy / OU Tree (default)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

Dùng khi: OU → Sub-OU, parent → child relationships. Không màu, không dày.

---

### E2 — Process Step (labeled, dày)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fontSize=12;fontStyle=1;
```

Dùng khi: Pipeline step với label đánh số "(1)", "(2)". `fontStyle=1` = bold label.

---

### E3 — Bidirectional (không mũi tên)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;
```

Dùng khi: On-prem ↔ TGW, DX ↔ Router. Hai chiều = không arrowhead.

---

### E4 — Dependency/Reference (dashed, không mũi tên)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=none;endFill=0;
```

Dùng khi: KMS encrypts S3 (không có data flow). Non-data relationship.

---

### E5 — Primary/Critical Flow (dày nhất)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;
```

Dùng khi: Main data path, primary connection trong diagram.

---

### E6 — AFT / Process Orange

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#FF9933;
```

Dùng khi: AFT account factory flow, automation pipeline trigger.

---

### E7 — Security Alert / Critical Path (đỏ)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF0000;strokeWidth=2;fontColor=#FF0000;
```

Dùng khi: Security finding propagation, critical alert path.

---

### E8 — Network Routing Subtle (xám xanh, dashed)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;dashed=1;fillColor=#bac8d3;strokeColor=#23445d;
```

Dùng khi: Route table entries, BGP routing, indirect network path.

---

### E9 — NonProd Shared Services (xanh dương, dashed, dày)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=3;fontSize=12;startArrow=classic;startFill=1;
```

Dùng khi: Non-Prod account → Shared Services. `startArrow` = chiều ngược lại so với endArrow.

---

### E10 — Prod Shared Services (xanh lá, không mũi tên)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;strokeWidth=2;strokeColor=#82B366;
```

Dùng khi: Production account ↔ Shared Service VPC. Xanh lá = Prod.

---

### E11 — Direct Connect / On-Prem Link (vàng cam, không mũi tên)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;strokeWidth=2;fillColor=#d5e8d4;strokeColor=#D79B00;
```

Dùng khi: DX connection, Site-to-Site VPN, on-prem link.

---

### E12 — Security Finding Flow (đỏ, mỏng)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#C7131F;strokeWidth=1;
```

Dùng khi: GuardDuty → Security Hub, thin security data path.

---

### E13 — Security Dependency (đỏ, dashed, mỏng)

```
edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#C7131F;fontSize=8;dashed=1;
```

Dùng khi: IAM policy reference, security control dependency (non-data).

---

### E14 — Integration / Data Link (xanh sáng)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#33FF33;
```

Dùng khi: Service integration, EventBridge → Lambda, cross-service data link.

---

### E15 — Networking Service Purple Dashed

```
html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;endArrow=classic;endFill=1;strokeColor=#8C4FFF;fontSize=10;dashed=1;labelBackgroundColor=#FFFFFF;
```

Dùng khi: DNS resolution (Route 53 → VPC), VPC → TGW connection type.  
**Lưu ý**: Edge này KHÔNG có `edgeStyle=orthogonalEdgeStyle` — là exception dùng auto-route với explicit exit/entry.

---

## PART 3: SPECIAL EDGE TYPES (exceptions có mục đích)

### S1 — Curved Edge (networking topology)

**Chỉ dùng trong networking diagram**, khi cần thể hiện logical path không phải physical routing.

```
edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontSize=12;startSize=8;endSize=8;
```

- Tìm thấy: 5 instances trong ACB_Networking_diagrams.drawio
- Visual: đường cong mềm thay vì right-angle turns
- Dùng khi: DNS query path, VPN tunnel overlay, logical peering

**Variant dashed (Backup path):**
```
edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;dashed=1;strokeColor=#999999;
```

- Màu `#999999` (xám) = Backup path, `dashed=1` = standby

---

### S2 — flexArrow (thick process arrow)

**Chỉ dùng trong process flow diagram** (AFT, Step Functions), KHÔNG dùng cho data flow thông thường.

```
shape=flexArrow;endArrow=classic;html=1;rounded=0;endWidth=8;endSize=7;fillColor=#FF8000;strokeColor=none;width=6;
```

- Tìm thấy: 2 instances trong ACB-SWO Security/IAM diagram
- Visual: mũi tên dày có fill color, chiều rộng uniform
- Dùng khi: High-level process step với visual emphasis mạnh

**Bidirectional variant:**
```
shape=flexArrow;endArrow=classic;startArrow=classic;html=1;rounded=0;fillColor=#000000;width=3.6;endSize=5.5;endWidth=9.4;startWidth=9.4;startSize=5.5;
```

---

### S3 — Floating Edge (no source/target ID)

Dùng làm **bus line** — element trực quan, không phải edge thực sự.

```xml
<mxCell id="bus-1" value="" style="endArrow=none;html=1;strokeWidth=4;strokeColor=#CD2264;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="500" y="80" as="sourcePoint" />
    <mxPoint x="500" y="600" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

Không có `source=` và `target=` attribute. Dùng `sourcePoint` và `targetPoint` thay thế.

---

## PART 4: ARROW CONFIGURATIONS

### Bảng quyết định arrow

| Semantic | endArrow | startArrow | Config |
|---|---|---|---|
| A gửi data đến B | → | (none) | `endArrow=classic;endFill=1` (default) |
| B nhận từ A (reverse) | ← | classic | `startArrow=classic;startFill=1;endArrow=none;endFill=0` |
| Hai chiều (↔) | none | none | `endArrow=none;endFill=0` |
| Dependency (không data) | none | none | `endArrow=none;endFill=0;dashed=1` |
| Primary process step | → | (none) | `endArrow=classic;endFill=1;strokeWidth=3` |

### Arrow size constants

```
startSize=8;endSize=8;   ← small arrow (default trong most edges)
endWidth=8;startWidth=8; ← dùng với flexArrow shape
```

---

## PART 5: COLOR → CATEGORY MAPPING

### Edge color = màu của SOURCE service

| AWS Category | strokeColor | Dùng với |
|---|---|---|
| Networking (VPC, TGW, Route53) | `#8C4FFF` | E15, hoặc base style + strokeColor |
| Security (GuardDuty, Security Hub, WAF) | `#C7131F` hoặc `#DD344C` | E12, E13 |
| Management (Control Tower, Config, Org) | `#BC1356` | Base + strokeColor |
| Compute (Lambda, EC2, ECS) | `#ED7100` | Base + strokeColor |
| DevTools (CodePipeline, CodeBuild) | `#C925D1` | Base + strokeColor |
| Storage (S3, EBS, Backup) | `#7AA116` | Base + strokeColor |
| AFT/Automation process | `#FF9933` | E6 |
| Security critical/alert | `#FF0000` | E7 |
| On-prem/DX link | `#D79B00` | E11 |
| Prod shared services | `#82B366` | E10 |
| NonProd shared services | `#6c8ebf` | E9 |
| Integration/EventBridge | `#33FF33` | E14 |
| Backup/Standby (neutral) | `#999999` | S1 variant |
| Network routing (subtle) | `#23445d` | E8 |

---

## PART 6: DASH PATTERNS

### Loại dashed

| dashPattern | Visual | Dùng khi |
|---|---|---|
| `dashed=1` (không dashPattern) | `- - - -` (8px dash, default) | Dependency, reference, standby |
| `dashed=1;dashPattern=1 1;` | `. . . .` (fine dots) | Logic flow trong AFT, "execution" path |
| `dashed=1;dashPattern=8 8;` | `──  ──  ──` (coarse) | Network routing, long-distance link |
| `dashed=1;dashPattern=3 3;` | `--- --- ---` (medium) | Dependency trung bình |

**Rule**: Chọn dashPattern dựa trên khoảng cách và tầm quan trọng:
- Fine (1 1) = low-level / implementation detail
- Default = standard dependency
- Coarse (8 8) = high-level / network layer

---

## PART 7: EXIT / ENTRY POINTS

### Khi NÀO cần exit/entry points

| Scenario | Cần exit/entry? |
|---|---|
| Source & target cùng container | KHÔNG (auto-route đủ) |
| Source & target container liền kề (1 hop) | NÊN CÓ (clean routing) |
| Source & target cách 2+ container | BẮT BUỘC |
| Fan-out (1 → N targets) | NÊN CÓ trên source |
| Fan-in (N → 1 target) | NÊN CÓ trên target |

### Coordinate reference

```
exitX=0;exitY=0.5;    ← thoát bên TRÁI (middle)
exitX=1;exitY=0.5;    ← thoát bên PHẢI (middle)
exitX=0.5;exitY=0;    ← thoát bên TRÊN (center)
exitX=0.5;exitY=1;    ← thoát bên DƯỚI (center)

entryX=0;entryY=0.5;  ← vào bên TRÁI (middle)
entryX=1;entryY=0.5;  ← vào bên PHẢI (middle)
entryX=0.5;entryY=0;  ← vào bên TRÊN (center)
entryX=0.5;entryY=1;  ← vào bên DƯỚI (center)
```

### entryPerimeter=0 — Pin tuyệt đối

```
entryX=0.75;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;
```

- Tìm thấy: 45+ instances trong production
- Tác dụng: Pin edge vào đúng coordinate, KHÔNG tự dịch sang perimeter gần nhất
- Dùng khi: Edge cần vào non-standard point (góc, cạnh chéo)

### Luôn include Dx=0;Dy=0

```
exitX=1;exitY=0.5;exitDx=0;exitDy=0;     ← ĐÚNG
exitX=1;exitY=0.5;                         ← THIẾU (có thể gây offset)
```

---

## PART 8: WAYPOINTS

### Khi NÀO cần waypoints

| Scenario | Waypoints? | Offset |
|---|---|---|
| Same-container routing | Không | — |
| Adjacent cross-account (1 hop) | Tuỳ | — |
| Cross-account distant (2+ hops) | BẮT BUỘC | 20px per edge |
| Fan-out (1 → 3+ targets) | BẮT BUỘC | 20px per edge |
| Fan-in (3+ → 1 target) | NÊN CÓ | 20px per entry |
| Lines crossing intermediate container | BẮT BUỘC | Route around |

### XML syntax

```xml
<mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;..." edge="1" parent="1" source="A" target="B">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="620" y="99" />
      <mxPoint x="620" y="119" />
    </Array>
  </mxGeometry>
</mxCell>
```

### Waypoint positioning rules

1. Đặt waypoints trong **khoảng trống giữa containers** (không overlap container content)
2. Mỗi parallel edge offset **20px** từ nhau (vertical stagger)
3. Fan-out từ 1 source: offset `exitY` theo 0.2, 0.5, 0.8 rồi waypoints mới stagger X
4. Corridor width: **50-80px** giữa source và target column

### Trunk corridor pattern (many-to-many)

```
Source A ──────┐
               │  ← trunk tại X cố định (vd: x=500)
Source B ──────┤  ← source B offset x=515
               │
               ├──── Target 1 (entryY=0.2)
               ├──── Target 2 (entryY=0.5)
               └──── Target 3 (entryY=0.8)
```

Mỗi source chiếm 1 "lane": x=500, x=515, x=530 (offset 15px).

---

## PART 9: MERGE TECHNIQUES (chống spaghetti)

### Quyết định merge

| Điều kiện | Kỹ thuật |
|---|---|
| 2-5 sources, cùng màu, cùng target | **Junction Point** |
| 6+ sources, cùng màu, cùng target area | **Bus Line** |
| HLD/overview, nhiều flows gộp lại | **Grouped Arrow** |
| Sources → KHÁC target | KHÔNG merge (dùng offset lanes) |
| Khác màu (khác flow type) | KHÔNG merge |
| Solid vs dashed | KHÔNG merge |

### Technique 1: Junction Point

```xml
<!-- S1 → Target: hội tụ tại x=450 -->
<mxCell id="e-s1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" source="s1" target="target">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="450" y="100" />
      <mxPoint x="450" y="300" />
    </Array>
  </mxGeometry>
</mxCell>
<!-- S2 → CÙNG Target: CÙNG X junction -->
<mxCell id="e-s2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" source="s2" target="target">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="450" y="200" />
      <mxPoint x="450" y="300" />
    </Array>
  </mxGeometry>
</mxCell>
```

### Technique 2: Bus Line (6+ sources)

```xml
<!-- Bus element (floating line, không source/target) -->
<mxCell id="bus" value="" style="endArrow=none;html=1;strokeWidth=4;strokeColor=#CD2264;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="500" y="80" as="sourcePoint" />
    <mxPoint x="500" y="600" as="targetPoint" />
  </mxGeometry>
</mxCell>
<!-- Source kết nối vào bus -->
<mxCell id="e-s1-bus" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;entryX=0;entryY=0.1;" edge="1" source="s1" target="bus">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### Technique 3: Grouped Arrow (HLD)

```xml
<mxCell id="e-grouped" value="All VPC Flow + DNS Logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=4;strokeColor=#8C4FFF;fontSize=10;fontStyle=1;" edge="1" source="src-accounts" target="tgt-logarchive">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

`strokeWidth=4` = dày nhất, label mô tả aggregate.

---

## PART 10: EDGE LABELS

### Inline label (preferred)

```xml
<mxCell id="edge-1" value="(1) Trigger" style="edgeStyle=orthogonalEdgeStyle;...;fontSize=12;fontStyle=1;" ...>
```

- `fontStyle=1` = bold cho step labels
- `fontStyle=0` = normal cho descriptive labels
- `fontSize=10` cho compact diagrams, `fontSize=12` cho standard

### Label background (khi label overlap edge)

```
labelBackgroundColor=#FFFFFF;
```

Thêm vào style string. Tìm thấy trong E15 và curved DNS edges.

### Step-numbered labels (AFT pattern)

```xml
value="(1) Store&#xa;Code Artifact"
```

- `&#xa;` = line break trong HTML
- Format: `(N) Action&#xa;Detail` cho labeled step edges
- Luôn kèm `fontStyle=1` (bold)

### Floating text (fallback)

Chỉ dùng khi label cần vị trí độc lập:

```
text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=10;
```

---

## PART 11: LEGEND / KEY BOX PATTERN

Khi diagram có nhiều loại edge → thêm Legend box.

```xml
<!-- Legend container (simple rounded box) -->
<mxCell id="legend" value="LEGENDS" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;fontStyle=1;fontSize=10;" vertex="1" parent="1">
  <mxGeometry x="X" y="Y" width="120" height="14" as="geometry" />
</mxCell>
<!-- Legend line: Active (solid orange) -->
<mxCell id="leg-active" value="Active" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#FF9933;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="X" y="Y+20" as="sourcePoint" />
    <mxPoint x="X+40" y="Y+20" as="targetPoint" />
  </mxGeometry>
</mxCell>
<!-- Legend line: Backup (dashed gray) -->
<mxCell id="leg-backup" value="Backup" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeColor=#999999;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="X" y="Y+40" as="sourcePoint" />
    <mxPoint x="X+40" y="Y+40" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

**Khi nào cần Legend**: diagram có 3+ loại edge khác nhau hoặc có edge đặc biệt (curved, backup path).

---

## PART 11b: EDGE `parent` ASSIGNMENT (thường bị bỏ sót)

### Quy tắc

| Scenario | parent= |
|---|---|
| Source và target trong CÙNG container | `parent="container-id"` |
| Source và target ở KHÁC container | `parent="1"` (root) |
| Legend line trong legend box | `parent="legend-container-id"` |
| Bus line / floating edge | `parent="1"` |

### Tại sao quan trọng

- `parent="container-id"` → edge di chuyển cùng container khi kéo
- `parent="1"` → edge cố định, không di chuyển theo container

### Ví dụ production (AFT.drawio)

```xml
<!-- CodeBuild → Terraform: CÙNG swimlane "Phase 3" → parent = swimlane ID -->
<mxCell id="edge-1" edge="1" parent="N2bL8cKAueUotPhLs3As-5"
  source="codebuild-cell-id" target="terraform-cell-id"
  style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Cross-account edge → parent = "1" -->
<mxCell id="edge-2" edge="1" parent="1"
  source="account-a-service" target="account-b-service"
  style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### `relative="1"` BẮT BUỘC trên mọi edge geometry

```xml
<mxGeometry relative="1" as="geometry" />        ← ĐÚNG
<mxGeometry as="geometry" />                      ← THIẾU relative → edge lỗi positioning
```

`relative="1"` làm cho geometry của edge tính toán relative to parent. Thiếu → edge bị render sai vị trí.

### Legend line geometry (khác regular edge)

Legend lines dùng `sourcePoint`/`targetPoint` trực tiếp (không có source/target cell), và kèm `width=`:

```xml
<mxCell id="leg-nonprod" edge="1" parent="legend-container-id"
  style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;strokeColor=#6C8EBF;strokeWidth=2;" value="">
  <mxGeometry relative="1" width="140" as="geometry">
    <mxPoint x="125" y="14.5" as="sourcePoint" />
    <mxPoint x="265" y="14.5" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

- `width="140"` = chiều dài line mẫu trong legend
- `x`, `y` = tọa độ relative to legend container
- KHÔNG có `source=` hay `target=` attributes

---

## PART 12: VIOLATIONS — KHÔNG BAO GIỜ LÀM

| ❌ Vi phạm | ✅ Thay thế |
|---|---|
| `edgeStyle` bị thiếu | Luôn có `edgeStyle=orthogonalEdgeStyle` |
| `rounded=1` trên edge | `rounded=0` |
| `edgeStyle=none` (ngoài Curved exception) | `edgeStyle=orthogonalEdgeStyle` |
| `strokeColor=light-dark(#FF9933,#FF9933)` | `strokeColor=#FF9933` (solid color) |
| Edge không có `html=1` | Thêm `html=1` |
| `fontFamily=Helvetica` trên edge | Không set fontFamily (dùng default) |
| Edge đi qua container không thuộc về | Route xung quanh container |
| Edge chồng lên icon (clearance < 20px) | Waypoints để route vòng |
| Nhiều parallel edges cùng path (overlap) | Stagger 20px per edge |
| Edge không có `source` và `target` (ngoài Bus/Legend exception) | Luôn set source và target |
| `parent="1"` cho edge trong cùng container | `parent="container-id"` khi source và target cùng cha |
| Thiếu `relative="1"` trong mxGeometry | `<mxGeometry relative="1" as="geometry" />` |

---

## PART 13: CHECKLIST — Verify mỗi edge trước khi submit

```
□ edgeStyle=orthogonalEdgeStyle có mặt
□ rounded=0 (không phải rounded=1)
□ html=1 có mặt
□ source= và target= ID hợp lệ (trừ bus/legend)
□ strokeColor khớp với AWS category của SOURCE service
□ strokeWidth đúng: data flow=2, dependency=1, primary=3
□ dashed=1 cho dependency/reference, solid cho data flow
□ Mũi tên đúng hướng data flow
□ Cross-account 2+ hops: có waypoints
□ Fan-out 1→3+: waypoints stagger 20px
□ Không edge nào chồng lên icon (clearance ≥ 20px)
□ Không edge nào xuyên qua container không thuộc về
□ Parallel edges cùng path: offset ≥ 20px
□ Label (nếu có): fontSize=12, fontStyle=1 cho step labels
□ 3+ edge types trong diagram: có Legend box
□ edge parent: cross-container → parent="1", same-container → parent="container-id"
□ mxGeometry có relative="1"
```

---

## PART 14: QUICK-PICK DECISION TREE

```
Cần vẽ 1 line →

  Data flow thực? 
  ├─ YES → strokeWidth=2, solid
  │         Source category color
  │         endArrow=classic (default)
  │
  └─ NO (reference/encrypt/depend) →
            strokeWidth=1, dashed=1
            Source category color
            endArrow=none;endFill=0

  Cùng container?
  ├─ YES → auto-route, không waypoints
  └─ NO → thêm exit/entry points
           Adjacent (1 hop)? → exit/entry đủ
           2+ hops? → thêm waypoints BẮT BUỘC

  Nhiều lines cùng chiều?
  ├─ 2-5 → Junction Point (cùng X waypoint)
  ├─ 6+ → Bus Line
  └─ HLD → Grouped Arrow (1 thick line + label)

  Cần curve?
  ├─ Networking topology/DNS → edgeStyle=none;curved=1
  └─ Mọi trường hợp khác → edgeStyle=orthogonalEdgeStyle
```


---

## PART 15: ADDITIONAL EDGE PATTERNS (từ production Log Aggregation diagrams)

> **Research basis**: Visual analysis từ Security/IAM Log Aggregation sheet — pattern cross-account log delivery flow  
> **Bổ sung**: 5 patterns chưa cover trong Part 1-14

---

### E16 — Vertical Sequential Dashed Arrow (sibling ordering)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#7AA116;dashed=1;dashPattern=3 3;
```

Dùng khi: Thể hiện **thứ tự / grouping** giữa sibling elements cùng level (ví dụ: 4 S3 buckets xếp dọc, arrow đi xuống giữa chúng).

**Đặc điểm:**
- `dashed=1` (KHÔNG solid — vì không phải data flow thực)
- CÓ arrowhead (`endArrow=classic`, default) — thể hiện direction/order
- `strokeWidth=1` (mỏng — phụ, không phải main flow)
- Color = Storage category (`#7AA116`) vì targets là S3 buckets
- Hướng: top → bottom (vertical chain)

**Khác với E4 (Dependency):** E4 KHÔNG có arrowhead (`endArrow=none`). E16 CÓ arrowhead — thể hiện sequential ordering, không phải bidirectional dependency.

```
┌─────────┐
│ Bucket 1 │
└────┬────┘
     │ ← E16 (dashed, có arrow, green)
     ▼
┌─────────┐
│ Bucket 2 │
└────┬────┘
     │
     ▼
┌─────────┐
│ Bucket 3 │
└─────────┘
```

---

### E12b — Intra-Account Security Data Flow (thick variant)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#C7131F;
```

Dùng khi: Active data flow giữa security services **trong cùng account** — ví dụ Security Hub → Kinesis Firehose, GuardDuty → Security Hub.

**Khác với E12:**
- E12 = `strokeWidth=1` (mỏng, cross-account thin path)
- **E12b = `strokeWidth=2`** (dày, intra-account active pipeline)

**Khi nào dùng E12 vs E12b:**
| Scenario | Edge |
|---|---|
| GuardDuty finding → Security Hub (cùng account) | **E12b** (thick, active pipeline) |
| Security Hub → Kinesis Firehose (cùng account) | **E12b** (thick, active pipeline) |
| Security Hub (Security Acct) → S3 (Log Archive Acct) | E12 (thin) hoặc dùng trunk pattern |
| Delegated admin reference | E13 (dashed, dependency) |

---

### Case 12: Vertical Trunk with Horizontal Branches

**Pattern**: 1 edge (hoặc trunk corridor) chạy **VERTICAL** (top → bottom), tại mỗi "tầng" (account level) nó rẽ **HORIZONTAL** sang target.

**Dùng khi**: Log aggregation — 1 source (Firehose/central service) delivers logs to multiple S3 buckets stacked vertically trong Log Archive Account.

```
                          │ ← Trunk (vertical)
                          │
    ┌─────────────┐       ├────→ [Bucket: Network Logs]
    │ Member Acct │───────┤
    └─────────────┘       │
                          │
    ┌─────────────┐       ├────→ [Bucket: Security Logs]
    │ Security Acct│──────┤
    └─────────────┘       │
                          │
    ┌─────────────┐       ├────→ [Bucket: CloudTrail Logs]
    │ Audit Acct  │───────┤
    └─────────────┘       │
                          └────→ [Bucket: Config Logs]
```

**Implementation — 2 approaches:**

#### Approach A: Shared X corridor (recommended for ≤5 branches)

Mỗi source-to-target edge chia sẻ cùng X coordinate cho vertical segment:

```xml
<!-- Member Acct sources → Network Bucket: trunk at x=550 -->
<mxCell id="e-member-netbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="vpc-flow-logs" target="bucket-network">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="550" y="150" />
      <mxPoint x="550" y="180" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Security Acct Firehose → Security Bucket: trunk at x=550, branch tại y=350 -->
<mxCell id="e-firehose-secbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#C7131F;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="kinesis-firehose" target="bucket-security">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="550" y="370" />
      <mxPoint x="550" y="400" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Audit Acct Trail → CloudTrail Bucket: trunk at x=565 (offset 15px), branch tại y=550 -->
<mxCell id="e-trail-ctbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#BC1356;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="org-trail" target="bucket-cloudtrail">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="565" y="560" />
      <mxPoint x="565" y="590" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Rules cho Vertical Trunk:**
1. Trunk X coordinate: đặt giữa source accounts (left) và target area (right) — thường 50-80px trước target column
2. Mỗi edge offset 15px X từ nhau: x=550, x=565, x=580 (tránh overlap visual)
3. Mỗi branch Y = target bucket Y center
4. Color: theo category của SOURCE service (Networking=#8C4FFF, Security=#C7131F, Management=#BC1356)

#### Approach B: Bus Line + spokes (for 6+ branches)

Khi có 6+ branches từ trunk, dùng Bus Line (S3 pattern) làm visual trunk, rồi individual spokes:

```xml
<!-- Vertical bus: collector trunk -->
<mxCell id="trunk-bus" value="" style="endArrow=none;html=1;strokeWidth=3;strokeColor=#CD2264;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="550" y="100" as="sourcePoint" />
    <mxPoint x="550" y="700" as="targetPoint" />
  </mxGeometry>
</mxCell>

<!-- Spoke: trunk → Bucket 1 (horizontal branch) -->
<mxCell id="spoke-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#CD2264;" edge="1" parent="1" source="trunk-bus" target="bucket-1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

---

### Case 3b: Bundled Parallel Merge (N sources → 1 target, corridor style)

**Pattern**: Nhiều edges từ N sources chạy **song song rất gần nhau** (bundled) rồi converge vào 1 target. Khác Case 3 (fan-in) ở chỗ các edges travel cùng path một đoạn dài trước khi vào target.

**Dùng khi**: VPC Flow Logs + DNS Query Logs + TGW Flow Logs → cùng 1 S3 bucket. Các sources nằm cạnh nhau horizontal, target ở xa bên phải.

```
[VPC Flow] ──────┐
                  ├══════════════════→ [S3 Bucket: Network Logs]
[DNS Query] ─────┤  ← bundled corridor
                  │
[TGW Flow] ──────┘
```

**Implementation:**

```xml
<!-- Source 1 (top): VPC Flow Logs → Network Bucket -->
<mxCell id="e-vpc-netbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;" edge="1" parent="1" source="vpc-flow-logs" target="bucket-network">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="420" y="130" />
      <mxPoint x="420" y="155" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Source 2 (middle): DNS Query Logs → Network Bucket -->
<mxCell id="e-dns-netbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="dns-query-logs" target="bucket-network">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="435" y="170" />
      <mxPoint x="435" y="175" />
    </Array>
  </mxGeometry>
</mxCell>

<!-- Source 3 (bottom): TGW Flow Logs → Network Bucket -->
<mxCell id="e-tgw-netbucket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.7;entryDx=0;entryDy=0;" edge="1" parent="1" source="tgw-flow-logs" target="bucket-network">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="450" y="210" />
      <mxPoint x="450" y="195" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Rules cho Bundled Parallel Merge:**
1. Tất cả edges CÙNG MÀU (cùng category) — vì đều là Networking
2. Waypoint X: stagger 15px per edge (420, 435, 450)
3. Entry Y: stagger trên target (0.3, 0.5, 0.7) — phân tán điểm vào
4. Visual effect: edges gần nhau → tạo "bundle" corridor appearance
5. CÓ THỂ dùng Grouped Arrow (E5 variant, `strokeWidth=4` + label) thay thế khi ở HLD level — nhưng trong detailed diagram phải vẽ từng edge riêng

**Khi nào dùng Bundled vs Junction Point vs Grouped Arrow:**

| N sources | Detail level | Cùng color? | Technique |
|---|---|---|---|
| 2-3 | Detailed | Yes | **Bundled Parallel** (Case 3b) |
| 2-5 | Detailed | Yes | **Junction Point** (Part 9, Tech 1) |
| 2-5 | HLD/overview | Yes | **Grouped Arrow** (1 thick line + label) |
| 6+ | Any | Yes | **Bus Line** (Part 9, Tech 2) |
| Any | Any | Mixed colors | KHÔNG merge — separate edges with offset lanes |

---

### PART 15.4: Rule #2 Amendment — Cross-Boundary Clarification

**Original Rule #2**: "LINES MUST NOT CROSS FOREIGN BOUNDARIES — A line MUST NEVER pass through a container it doesn't belong to. Route around."

**Clarification (AMENDMENT):**

Rule #2 áp dụng cho **INTERMEDIATE containers** — containers mà edge XUYÊN QUA nhưng source và target đều KHÔNG thuộc về.

**Rule #2 KHÔNG cấm:**
- Edge exits source container (source nằm bên trong) → **EXPECTED behavior**
- Edge enters target container (target nằm bên trong) → **EXPECTED behavior**

**Rule #2 CẤM:**
- Edge đi qua Container C khi source ∈ Container A và target ∈ Container B (C là intermediate) → **VIOLATION**

**Visual:**

```
✅ ALLOWED (exit own container + enter target container):
┌─── Account A ───┐         ┌─── Account B ───┐
│                  │         │                  │
│   [Firehose] ───┼────────→┼───→ [S3 Bucket]  │
│                  │         │                  │
└──────────────────┘         └──────────────────┘
        ↑ edge exits A                ↑ edge enters B
        (source container)            (target container)

❌ FORBIDDEN (pass through intermediate container):
┌─── Account A ───┐   ┌── Account C ──┐   ┌─── Account B ───┐
│                  │   │               │   │                  │
│   [Source] ──────┼───┼───XUYÊN QUA───┼───┼──→ [Target]     │
│                  │   │               │   │                  │
└──────────────────┘   └───────────────┘   └──────────────────┘
                            ↑ VIOLATION — route around C!
```

**Khi edge BẮT BUỘC phải cross intermediate container** (layout constraints make routing around impossible):
1. Ưu tiên: redesign layout để tránh
2. Nếu không thể tránh: route edge ĐI TRÊN hoặc ĐI DƯỚI intermediate container (waypoints Y ở ngoài boundary)
3. Last resort: nếu diagram space không cho phép route around → ghi note trong Design Spec rằng đây là acceptable trade-off

---

### PART 15.5: Cross-Account Log Aggregation Pattern (composite)

**Pattern tổng hợp** cho Log Aggregation diagrams — kết hợp Case 12 + Case 3b + E12b + E16.

**Layout structure:**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ┌── Member Accounts ──┐    ┌── Log Archive Account ──────────┐│
│  │ [VPC] [DNS] [TGW]   │    │  [region container]             ││
│  │       ↓ bundled      │ ───┤──→ [Bucket: Network]    ▲      ││
│  └──────────────────────┘    │                          │ E16  ││
│                              │                          ▼      ││
│  ┌── Security Account ─┐    │     [Bucket: Security]   ▲      ││
│  │ [GD]→[SH]→[Firehose]│ ───┤──→                       │ E16  ││
│  └──────────────────────┘    │                          ▼      ││
│                              │     [Bucket: CloudTrail] ▲      ││
│  ┌── Audit Account ────┐    │                           │ E16  ││
│  │ [Trail]  [Config]   │ ───┤──→                        ▼      ││
│  └──────────────────────┘    │     [Bucket: Config]            ││
│                              └─────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

**Edge types used in this pattern:**

| Connection | Edge Type | Why |
|---|---|---|
| GuardDuty → Security Hub (intra-account) | **E12b** (thick, solid, red) | Active security pipeline |
| Security Hub → Firehose (intra-account) | **E12b** (thick, solid, red) | Active security pipeline |
| VPC/DNS/TGW → Network Bucket (cross-account) | **Case 3b** bundled, color `#8C4FFF` | Multiple network sources → 1 target |
| Firehose → Security Bucket (cross-account) | **Case 12** trunk, color `#C7131F` | Vertical trunk with branch |
| Trail/Config → respective Buckets (cross-account) | **Case 12** trunk, color `#BC1356` | Management category |
| Bucket → Bucket (vertical ordering) | **E16** (dashed, arrow, green) | Visual ordering/grouping |

**Spacing for this pattern:**
- Left column (source accounts): x=50 to x=400
- Trunk corridor: x=450 to x=550
- Right column (Log Archive + buckets): x=600 to x=900
- Vertical gap between account containers: 40-60px
- Vertical gap between buckets: 120-160px (includes label space)

---

## PART 16: UPDATED CHECKLIST (append to Part 13)

Bổ sung vào checklist Part 13:

```
□ Vertical trunk patterns (Case 12): edges chia sẻ trunk X, offset 15px per lane
□ Bundled parallel (Case 3b): entries stagger trên target (entryY=0.3/0.5/0.7)
□ Sequential arrows (E16): dashed=1, CÓ arrowhead, strokeWidth=1
□ Cross-boundary: chỉ intermediate containers bị cấm — exit/enter own container OK
□ Intra-account security flow (E12b): strokeWidth=2 (thick) cho active pipeline
□ Log aggregation composite: verify E12b (intra) + Case 12 (cross) + E16 (ordering) consistency
```

---

## PART 17: UPDATED DECISION TREE (append to Part 14)

Bổ sung vào decision tree Part 14:

```
  Log aggregation / multi-target delivery?
  ├─ Sources cùng account, horizontal → Case 3b (Bundled Parallel)
  ├─ Sources khác account, targets xếp dọc → Case 12 (Vertical Trunk)
  └─ Ordering giữa targets (không phải data flow) → E16 (Sequential Dashed)

  Security services trong cùng account?
  ├─ Active pipeline (GD→SH, SH→Firehose) → E12b (thick, solid, #C7131F)
  └─ Reference/dependency (KMS key ref) → E13 (dashed, thin)

  Edge exits/enters container boundary?
  ├─ Source HOẶC target trong container đó → OK (allowed)
  └─ NEITHER source nor target trong container → VIOLATION (route around)
```
