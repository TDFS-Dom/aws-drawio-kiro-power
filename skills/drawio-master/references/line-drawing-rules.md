# Line Drawing Rules — draw.io AWS Architecture Diagrams

> **Research basis**: 949 edges từ 4 production `.drawio` files + visual analysis 44 exported PNG pages  
> **Source files**: AFT.drawio (362 edges), ACB_Networking (429), ACB_Security_IAM (128), ACB_OU_Design (30)

---

## PART 0: CONTAINER BORDER = LINE (thường bị bỏ sót)

> **Nguyên nhân phổ biến nhất của "line crossing icon"**: không phải edge, mà là container border.

### Container border là đường kẻ

Mọi container (Account, VPC, Subnet, Swimlane...) có border = đường kẻ 4 cạnh. Rule "LINES MUST NOT CROSS ICONS" áp dụng cho **cả container border**, không chỉ edge.

```
❌ SAI — Container quá nhỏ → border cắt qua icon:
  ┌──────────────────┐
  │ [Icon A]  [Icon B│←── border cắt qua Icon B
  └──────────────────┘

✅ ĐÚNG — Container đủ rộng → border ở ngoài icons:
  ┌─────────────────────┐
  │ [Icon A]  [Icon B]  │
  └─────────────────────┘
```

### Kiểm tra bắt buộc trước khi viết XML

Với MỖI container (tọa độ icon là relative to container):

```
PHẢI ĐẢM BẢO:
  icon_x + icon_width + right_padding  ≤  container_width      (horizontal)
  icon_y + icon_height + label(30px) + bottom_padding  ≤  container_height  (vertical)

  right_padding  = 81px (minimum)
  bottom_padding = 50px (minimum)
```

Ví dụ: icon tại x=370 (relative), width=78 → cần container_width ≥ 370 + 78 + 81 = **529px**

Nếu vi phạm → tăng container width/height. KHÔNG thu nhỏ icon.

### Pattern lỗi phổ biến nhất (Production observed)

```
Purple VPC container chứa 3 icons horizontal:
  AI tính: width = 50 (pad) + 78 + 60 + 78 = 266px ← THIẾU icon thứ 3 và right padding
  ĐÚNG:    width = 50 + 78 + 60 + 78 + 60 + 78 + 81 = 485px minimum
```

Kết quả: container border cắt qua icon thứ 2 và 3 → vi phạm rule 1 + rule 2.

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
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#C7131F;fontSize=8;dashed=1;
```

Dùng khi: IAM policy reference, security control dependency (non-data).

---

### E14 — Integration / Data Link (xanh sáng)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#33FF33;
```

Dùng khi: Service integration, EventBridge → Lambda, cross-service data link.

---

### E15 — Networking Service Purple Dashed ⚠️ EXCEPTION

> **⚠️ EXCEPTION**: Edge này KHÔNG dùng `edgeStyle=orthogonalEdgeStyle`. Đây là special case — chỉ dùng khi cần DNS resolution curve với explicit exit/entry. Xem PART 3 để hiểu các exceptions.

```
html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;endArrow=classic;endFill=1;strokeColor=#8C4FFF;fontSize=10;dashed=1;labelBackgroundColor=#FFFFFF;
```

Dùng khi: DNS resolution (Route 53 → VPC), VPC → TGW connection type với explicit left→right direction.  
**KHÔNG dùng** cho các networking edges thông thường — dùng `edgeStyle=orthogonalEdgeStyle` + `strokeColor=#8C4FFF` thay thế.

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

## PART 12: EDGE `parent` ASSIGNMENT (thường bị bỏ sót)

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

## PART 13: VIOLATIONS — KHÔNG BAO GIỜ LÀM

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

---

## PART 13b: LINE ROUTING ANTI-PATTERNS (AI hay tạo ra — BẮT BUỘC tránh)

> Những lỗi routing dưới đây xảy ra khi AI để draw.io auto-route thay vì explicitly control waypoints. **PHẢI detect và tránh TRƯỚC KHI viết XML.**

### ❌ AP-1: Vertical trunk xuyên qua intermediate accounts

**Lỗi**: Line chạy thẳng đứng xuyên qua account container mà source/target đều KHÔNG thuộc về.

```
┌── Member ──────┐
│   [source]     │
└───────┼────────┘   ← exits OK
        │
┌───────┼────────┐   ← XUYÊN QUA Security Account ❌
│       │        │
└───────┼────────┘
        │
┌───────┼────────┐
│       ▼        │
│   [target]     │   ← enters OK
└────────────────┘
```

**Fix**: Route NGOÀI tất cả intermediate containers (bên phải hoặc trái):

```
┌── Member ──────┐
│   [source]─────┼───┐
└────────────────┘   │  ← route OUTSIDE (x = rightmost + 40px)
                     │
┌── Security ────┐   │  ← edge bypasses this container ✅
│                │   │
└────────────────┘   │
                     │
┌── Target ──────┐   │
│   [target]←────┼───┘
└────────────────┘
```

**Waypoint X** = max(all container right edges) + 40px

---

### ❌ AP-2: Multiple edges chồng tại cùng X/Y (spaghetti)

**Lỗi**: 3+ edges chạy vertical cùng X coordinate → nhìn như 1 đường dày, không phân biệt được.

**Fix**: Mỗi edge = 1 lane riêng, offset 20px:
- Edge 1: x=500 (lane 1)
- Edge 2: x=520 (lane 2)
- Edge 3: x=540 (lane 3)

**Corridor width** = N edges × 20px. Plan corridor TRƯỚC khi viết XML.

---

### ❌ AP-3: Edge zigzag 3+ turns khi 1-2 turns đủ

**Lỗi**: Waypoints không tối ưu → edge đi vòng vèo qua nhiều góc vuông.

**Fix**: Mỗi edge tối đa **2 turns** (exit → horizontal → vertical → entry). Nếu cần 3+ turns → layout containers sai, cần re-arrange containers TRƯỚC.

---

### ❌ AP-4: Fan-in edges chồng nhau thành 1 khối

**Lỗi**: VPC + DNS + TGW → cùng 1 bucket, 3 edges chạy cùng path → trông như 1 line dày.

**Fix A (detailed)**: Stagger entryY (0.25 / 0.50 / 0.75) + stagger waypoint X (offset 20px per edge).

**Fix B (HLD)**: Dùng 1 Grouped Arrow `strokeWidth=4` với label "VPC Flow, DNS, TGW Logs".

---

### ❌ AP-5: Dashed edge (dependency) overlap với solid edge (data flow)

**Lỗi**: KMS dashed line chạy cùng path với Firehose solid line → không phân biệt.

**Fix**: Dashed edges route ở Y band KHÁC, minimum **30px offset** từ nearest solid edge. Dependency lines LUÔN ở separate visual layer.

---

### ❌ AP-6: Edge hugs container border (trông như double border)

**Lỗi**: Edge exit bottom → chạy dọc theo border → trông như border bị double.

**Fix**: Ưu tiên exit RIGHT (`exitX=1;exitY=0.5`) cho left→right flows. Chỉ exit BOTTOM khi target thực sự ở phía dưới VÀ không có intermediate container.

---

### ❌ AP-7: Thiếu exit/entry points → auto-route tạo detour

**Lỗi**: AI không set exit/entry → draw.io tự chọn exit point → đường đi vô nghĩa.

**Fix**: **MỌI cross-account edge BẮT BUỘC có explicit exit/entry:**
```
exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;
```

Không explicit exit/entry = auto-route gamble. KHÔNG chấp nhận.

---

### 🚨 MANDATORY: Pre-XML Edge Planning

**TRƯỚC KHI viết bất kỳ edge XML nào**, list plan:

```
EDGE PLAN:
1. [source] → [target] | type: solid/dashed | direction: L→R/T→B | lane: N | intermediate containers to avoid: [...] | exit/entry: explicit
2. ...
```

**Verify plan:**
- [ ] Mỗi edge có lane riêng (không overlap neighbor)
- [ ] Không edge nào cross intermediate container
- [ ] Dashed edges ở separate Y/X band từ solid edges
- [ ] Mọi cross-account edge có explicit exit/entry
- [ ] Max 2 turns per edge

---

## PART 13c: PATHFINDING ALGORITHM (Tính waypoints chính xác)

> Thay vì đoán waypoints → dùng thuật toán dưới đây để TÍNH TOÁN path cho mỗi edge. Chạy TRƯỚC KHI viết XML.

### Input (từ Edge Plan + Container Layout)

```
Cho mỗi edge cần vẽ:
  - source_cell: {id, x, y, width, height, parent_container}
  - target_cell: {id, x, y, width, height, parent_container}
  - edge_type: solid | dashed
  - lane_index: 0, 1, 2... (assigned trong Edge Plan)

Layout data (đã biết từ Step 4):
  - containers[]: {id, x, y, width, height}  ← tất cả account/region containers
  - LANE_OFFSET = 20  ← px offset giữa parallel lanes
  - CLEARANCE = 40    ← px minimum gap giữa edge và container border
  - BAND_GAP = 30     ← px offset giữa dashed band và solid band
```

### Algorithm: Route Edge

```
FUNCTION routeEdge(source, target, containers, edge_type, lane_index):

  ──── STEP 1: Xác định Exit/Entry Points ────

  direction = detectDirection(source, target)
  
  IF direction == LEFT_TO_RIGHT:
    exit  = {x: source.x + source.width, y: source.y + source.height/2}   # exitX=1, exitY=0.5
    entry = {x: target.x,               y: target.y + target.height/2}   # entryX=0, entryY=0.5
  
  ELIF direction == TOP_TO_BOTTOM:
    exit  = {x: source.x + source.width/2, y: source.y + source.height}   # exitX=0.5, exitY=1
    entry = {x: target.x + target.width/2, y: target.y}                   # entryX=0.5, entryY=0
  
  ELIF direction == RIGHT_TO_LEFT:
    exit  = {x: source.x,                  y: source.y + source.height/2}  # exitX=0, exitY=0.5
    entry = {x: target.x + target.width,   y: target.y + target.height/2}  # entryX=1, entryY=0.5

  ──── STEP 2: Tìm intermediate containers (obstacles) ────

  obstacles = []
  FOR each container in containers:
    IF container == source.parent_container: SKIP
    IF container == target.parent_container: SKIP
    IF edgePathIntersects(exit, entry, container):
      obstacles.append(container)
  
  ──── STEP 3: Tính route path ────

  IF obstacles == EMPTY:
    # Direct route — no waypoints needed (hoặc 1 waypoint cho clean L-shape)
    IF exit.y == entry.y:
      waypoints = []   # straight horizontal
    ELIF exit.x == entry.x:
      waypoints = []   # straight vertical
    ELSE:
      # L-shape: 1 turn
      mid_x = exit.x + (entry.x - exit.x) / 2
      waypoints = [{x: mid_x, y: exit.y}, {x: mid_x, y: entry.y}]
  
  ELSE:
    # Has obstacles → route OUTSIDE
    route_side = chooseSide(source, target, obstacles)
    
    IF route_side == RIGHT:
      bypass_x = max(c.x + c.width for c in obstacles) + CLEARANCE + (lane_index * LANE_OFFSET)
    ELIF route_side == LEFT:
      bypass_x = min(c.x for c in obstacles) - CLEARANCE - (lane_index * LANE_OFFSET)
    ELIF route_side == TOP:
      bypass_y = min(c.y for c in obstacles) - CLEARANCE - (lane_index * LANE_OFFSET)
    ELIF route_side == BOTTOM:
      bypass_y = max(c.y + c.height for c in obstacles) + CLEARANCE + (lane_index * LANE_OFFSET)
    
    # Generate waypoints (max 2 turns):
    IF route_side in [RIGHT, LEFT]:
      waypoints = [
        {x: bypass_x, y: exit.y},    # turn 1: go to bypass lane
        {x: bypass_x, y: entry.y}    # turn 2: go to target Y level
      ]
    ELSE:
      waypoints = [
        {x: exit.x,   y: bypass_y},  # turn 1: go to bypass lane
        {x: entry.x,  y: bypass_y}   # turn 2: go to target X level
      ]

  ──── STEP 4: Apply band offset (dashed vs solid separation) ────

  IF edge_type == DASHED:
    FOR each wp in waypoints:
      wp.y -= BAND_GAP   # dashed edges route ABOVE solid edges
  
  ──── STEP 5: Apply fan-in/fan-out stagger ────

  # Nếu nhiều edges cùng target → stagger entry Y
  same_target_edges = edges.filter(e => e.target == target AND e != this_edge)
  IF same_target_edges.count > 0:
    total = same_target_edges.count + 1
    my_index = lane_index % total
    entry.y = target.y + (target.height * (my_index + 1) / (total + 1))
    # Update last waypoint Y to match new entry.y
    IF waypoints.length > 0:
      waypoints[-1].y = entry.y

  RETURN {exit, entry, waypoints}
```

### Helper Functions

```
FUNCTION detectDirection(source, target):
  dx = target.x - source.x
  dy = target.y - source.y
  IF abs(dx) > abs(dy):
    RETURN LEFT_TO_RIGHT if dx > 0 else RIGHT_TO_LEFT
  ELSE:
    RETURN TOP_TO_BOTTOM if dy > 0 else BOTTOM_TO_TOP

FUNCTION chooseSide(source, target, obstacles):
  # Prefer routing on the SAME SIDE as target relative to obstacles
  # Rule: don't cross MORE containers
  
  max_obstacle_right = max(c.x + c.width for c in obstacles)
  min_obstacle_left  = min(c.x for c in obstacles)
  max_obstacle_bottom = max(c.y + c.height for c in obstacles)
  min_obstacle_top   = min(c.y for c in obstacles)
  
  # If target is to the RIGHT of obstacles → route RIGHT
  IF target.x > max_obstacle_right: RETURN RIGHT
  # If target is to the LEFT of obstacles → route LEFT
  IF target.x + target.width < min_obstacle_left: RETURN LEFT
  # If target is BELOW obstacles → route BOTTOM (but only if no more obstacles below)
  IF target.y > max_obstacle_bottom: RETURN BOTTOM
  # Default: route to side with more space
  space_right = canvas_width - max_obstacle_right
  space_left  = min_obstacle_left
  RETURN RIGHT if space_right >= space_left else LEFT

FUNCTION edgePathIntersects(exit_point, entry_point, container):
  # Check if straight line between exit and entry would cross container bbox
  # Use axis-aligned bounding box intersection
  line_min_x = min(exit_point.x, entry_point.x)
  line_max_x = max(exit_point.x, entry_point.x)
  line_min_y = min(exit_point.y, entry_point.y)
  line_max_y = max(exit_point.y, entry_point.y)
  
  # Orthogonal edge actually travels L-shaped, so check both segments:
  # Segment 1: horizontal from exit to mid_x
  # Segment 2: vertical from mid_x to entry
  # Simplified: if container bbox overlaps the rectangular area between exit and entry
  RETURN NOT (container.x > line_max_x OR 
              container.x + container.width < line_min_x OR
              container.y > line_max_y OR 
              container.y + container.height < line_min_y)
```

### Output Format (chuyển thành XML)

```
Kết quả routeEdge():
  exit  = {x: 450, y: 200}    → exitX, exitY (convert to 0-1 relative)
  entry = {x: 600, y: 350}    → entryX, entryY (convert to 0-1 relative)
  waypoints = [{x: 520, y: 200}, {x: 520, y: 350}]

Convert to exit/entry relative values:
  exitX  = (exit.x - source.x) / source.width     # 0-1
  exitY  = (exit.y - source.y) / source.height     # 0-1
  entryX = (entry.x - target.x) / target.width     # 0-1
  entryY = (entry.y - target.y) / target.height     # 0-1

XML output:
```

```xml
<mxCell id="e-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#8C4FFF;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="src-id" target="tgt-id">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="520" y="200" />
      <mxPoint x="520" y="350" />
    </Array>
  </mxGeometry>
</mxCell>
```

### Worked Example: Log Aggregation Diagram

```
Layout:
  Member Account:    {x: 30,  y: 20,  w: 400, h: 250}
  Security Account:  {x: 30,  y: 310, w: 400, h: 300}
  Audit Account:     {x: 30,  y: 650, w: 400, h: 250}
  Log Archive:       {x: 550, y: 20,  w: 400, h: 880}

Edge: Firehose (Security) → acb-logs-cloudtrail (Log Archive)
  source: {x: 200, y: 520, w: 78, h: 78, parent: Security}
  target: {x: 700, y: 560, w: 78, h: 78, parent: Log Archive}

Step 1 (direction = LEFT_TO_RIGHT):
  exit  = {x: 278, y: 559}   → exitX=1, exitY=0.5
  entry = {x: 700, y: 599}   → entryX=0, entryY=0.5

Step 2 (obstacles):
  Path from (278,559) → (700,599):
  - Member Account: y range 20-270 → does NOT intersect (559 > 270) ✅
  - Audit Account: y range 650-900 → does NOT intersect (559 < 650) ✅
  - No obstacles!

Step 3 (no obstacles → L-shape):
  mid_x = 278 + (700-278)/2 = 489
  waypoints = [{x: 489, y: 559}, {x: 489, y: 599}]

Step 4 (solid edge → no band offset)

Step 5 (check fan-in to same target):
  Other edges to acb-logs-cloudtrail: Audit Trail edge (lane 1)
  total = 2, my_index = 0
  entry.y = 560 + (78 * 1/3) = 586
  waypoints[-1].y = 586

Final: exit=(278,559), entry=(700,586), waypoints=[(489,559),(489,586)]
```

### Khi NÀO apply algorithm vs auto-route

| Scenario | Algorithm? |
|---|---|
| Same-container edge (source & target cùng parent) | ❌ Auto-route |
| Adjacent containers (no intermediate) | ⚠️ Set exit/entry, waypoints optional |
| Cross-container with intermediate obstacles | ✅ MANDATORY algorithm |
| Fan-in/fan-out (1→N or N→1) | ✅ MANDATORY (stagger calculation) |
| Parallel edges same direction | ✅ MANDATORY (lane assignment) |
| Single simple L→R edge no obstacles | ❌ Exit/entry enough |

```
MANDATORY (mọi edge):
□ edgeStyle=orthogonalEdgeStyle có mặt (trừ E15, S1, S2 exceptions)
□ rounded=0 (không phải rounded=1)
□ html=1 có mặt
□ relative="1" trong mxGeometry
□ source= và target= ID hợp lệ (trừ bus/legend/floating)
□ parent đúng: cross-container → "1", same-container → "container-id"

STYLE:
□ strokeColor khớp với AWS category của SOURCE service (xem PART 5)
□ strokeWidth đúng: data flow=2, dependency=1, primary=3, intra-account security=2
□ dashed=1 cho dependency/reference/encryption scope, solid cho data flow
□ Mũi tên đúng hướng: data flow → endArrow=classic, bidirectional/dependency → endArrow=none

ROUTING:
□ Cross-account 2+ hops: có waypoints + exit/entry points
□ Fan-out 1→3+: waypoints stagger 20px per edge
□ Không edge nào chồng lên icon (clearance ≥ 20px)
□ Không edge nào xuyên qua INTERMEDIATE container (source/target không thuộc container đó)
□ Parallel edges cùng path: offset ≥ 20px (vertical stagger)
□ Vertical trunk (Case 12): chia sẻ trunk X, offset 15px per lane

LABELS:
□ Label (nếu có): fontSize=12, fontStyle=1 cho step labels
□ labelBackgroundColor=#FFFFFF nếu label overlap edge

COMPOSITE PATTERNS:
□ 3+ edge types trong diagram: có Legend box
□ Log aggregation: verify E12b (intra) + Case 12 (cross) + E16 (ordering) + E17 (encryption) consistency
□ Intra-account security flow: E12b (strokeWidth=2, solid #C7131F)
□ KMS scope: E17 = dashed container bao quanh targets + dashed edge từ KMS
□ Bundled parallel: chain + aggregation connector (Case 3b) OR individual parallel edges

CONTAINER SIZE (trước khi đặt icon):
□ container_width ≥ rightmost_icon_x + icon_width + 81px
□ container_height ≥ bottom_icon_y + icon_height + 30px(label) + 50px
□ Không container border nào cắt qua child icon
```

---

## PART 15: QUICK-PICK DECISION TREE

```
Cần vẽ 1 line →

  Data flow thực? 
  ├─ YES → strokeWidth=2, solid, endArrow=classic
  │         Source category color (PART 5)
  │         Security intra-account? → E12b (strokeWidth=2)
  │
  └─ NO (reference/encrypt/depend) →
            strokeWidth=1, dashed=1, endArrow=none;endFill=0
            Source category color
            KMS encryption? → E17 (scope container + dashed edge)

  Cùng container?
  ├─ YES → parent="container-id", auto-route, không waypoints
  └─ NO  → parent="1", thêm exit/entry points
            Adjacent (1 hop)? → exit/entry đủ
            2+ hops? → waypoints BẮT BUỘC (route around intermediate)

  Nhiều lines cùng chiều?
  ├─ 2-5 sources, cùng target → Junction Point (cùng X waypoint)
  ├─ 6+ sources → Bus Line
  └─ HLD → Grouped Arrow (1 thick line + label)

  Log aggregation / multi-target delivery?
  ├─ Sources cùng account, horizontal → Case 3b (Bundled/Chain + Connector)
  ├─ Sources khác account, targets xếp dọc → Case 12 (Vertical Trunk)
  └─ Ordering giữa targets (không data flow) → E16 (dashed, pink, có arrow)

  Security services?
  ├─ Active pipeline cùng account (GD→SH, SH→Firehose) → E12b
  ├─ Cross-account security finding → E12 (thin)
  └─ Reference/dependency (IAM, KMS key ref) → E13 hoặc E17

  Edge exits/enters container boundary?
  ├─ Source HOẶC target trong container đó → OK
  └─ NEITHER source nor target → VIOLATION → route around

  Cần curve?
  ├─ Networking topology/DNS → S1 (edgeStyle=none;curved=1)
  └─ Mọi trường hợp khác → edgeStyle=orthogonalEdgeStyle
```

---

## PART 16: ADDITIONAL EDGE PATTERNS (từ production Log Aggregation diagrams)

> **Research basis**: Visual analysis từ Security/IAM Log Aggregation sheet — pattern cross-account log delivery flow  
> **Bổ sung**: 5 patterns chưa cover trong Part 1-15

---

### 16.1 — E16: Vertical Sequential Dashed Arrow (sibling ordering)

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#CD2264;dashed=1;dashPattern=3 3;
```

Dùng khi: Thể hiện **thứ tự / grouping / log delivery sequence** giữa sibling elements cùng level (ví dụ: 4 S3 buckets xếp dọc trong Log Archive, arrow đi xuống giữa chúng).

**Đặc điểm:**
- `dashed=1` (KHÔNG solid — vì không phải data flow thực, chỉ ordering visual)
- CÓ arrowhead (`endArrow=classic`, default) — thể hiện direction/order
- `strokeWidth=1` (mỏng — phụ, không phải main flow)
- Color = **Account/org pink** (`#CD2264`) — cùng màu account group border, thể hiện đây là organizational ordering
- Hướng: top → bottom (vertical chain)

**Tại sao dùng `#CD2264` thay vì Storage green `#7AA116`:**
- Các arrows này KHÔNG thể hiện S3 data flow (bucket → bucket) — S3 không tự replicate giữa chúng
- Chúng thể hiện **log delivery ordering** trong context AWS Organization → dùng Organization/Account color
- Production diagram xác nhận: cùng màu hồng với account container borders

**Khác với E4 (Dependency):** E4 KHÔNG có arrowhead (`endArrow=none`). E16 CÓ arrowhead — thể hiện sequential ordering, không phải bidirectional dependency.

```
┌─────────┐
│ Bucket 1 │
└────┬────┘
     │ ← E16 (dashed, có arrow, pink #CD2264)
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

### 16.2 — E12b: Intra-Account Security Data Flow (thick variant)

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

### 16.3 — Case 12: Vertical Trunk with Horizontal Branches

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

### 16.4 — Case 3b: Bundled Parallel Merge (N sources → 1 target, corridor style)

**Pattern**: Nhiều edges từ N sources chạy **song song rất gần nhau** (bundled) rồi converge vào 1 target. Khác Case 3 (fan-in) ở chỗ các edges travel cùng path một đoạn dài trước khi vào target.

**Dùng khi**: VPC Flow Logs + DNS Query Logs + TGW Flow Logs → cùng 1 S3 bucket. Các sources nằm cạnh nhau horizontal, target ở xa bên phải.

**Hai variant trong production:**

#### Variant A: Individual parallel edges (mỗi source = 1 edge riêng)

```
[VPC Flow] ──────┐
                  ├══════════════════→ [S3 Bucket: Network Logs]
[DNS Query] ─────┤  ← bundled corridor
                  │
[TGW Flow] ──────┘
```

#### Variant B: Chain + Aggregation Point (production preferred — from screenshot)

Trong production, pattern thực tế là:
1. Sources nối CHAIN (VPC → DNS → TGW) bằng arrows nhỏ (thể hiện log consolidation path)
2. Source cuối (TGW) exit vào 1 **Aggregation Connector** (rectangular element)
3. Connector element → 1 single arrow → target bucket

```
[VPC Flow] ──→ [DNS Query] ──→ [TGW Flow] ──→ [█████████] ═══════→ [S3 Bucket]
                                                 ↑ Aggregation
                                                   Connector
```

**Aggregation Connector element** — rectangular visual box (KHÔNG phải AWS icon):

```xml
<!-- Aggregation connector: visual element representing consolidated log stream -->
<mxCell id="agg-connector" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#8C4FFF;strokeWidth=2;" vertex="1" parent="{account-container-id}">
  <mxGeometry x="{X}" y="{Y}" width="60" height="80" as="geometry" />
</mxCell>
```

**Rules:**
- Connector có `strokeColor` = cùng category color (Networking=#8C4FFF)
- `fillColor=none` (transparent) hoặc subtle fill
- Đặt SAU last service trong chain, TRƯỚC exit point của container
- 1 single output edge từ connector → target (thay vì N parallel edges)

**Khi nào Variant A vs B:**
| Scenario | Variant |
|---|---|
| Sources independent (không consolidate trước khi gửi) | A (parallel edges) |
| Sources chain/consolidate trước rồi gửi 1 stream | **B (chain + connector)** |
| HLD/overview level | Grouped Arrow (1 thick line + label) |

---

### 16.5 — E17: Encryption Scope Boundary (KMS dashed container + dependency edge)

**Pattern mới**: Dashed rectangle bao quanh target resources + label "SSE-KMS Encryption" + dashed edge từ KMS icon.

**Dùng khi**: Thể hiện KMS encryption scope — nhiều S3 buckets đều encrypted bởi cùng 1 KMS key.

**2 elements cần vẽ:**

#### Element 1: Dashed Scope Container (NOT an account — pure visual boundary)

```xml
<!-- KMS Encryption scope: dashed boundary around encrypted resources -->
<mxCell id="kms-scope" value="SSE-KMS Encryption" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#CD2264;strokeWidth=1;dashed=1;dashPattern=5 5;verticalAlign=top;align=left;spacingLeft=10;spacingTop=5;fontSize=11;fontColor=#CD2264;container=1;collapsible=0;" vertex="1" parent="1">
  <mxGeometry x="{X}" y="{Y}" width="{W}" height="{H}" as="geometry" />
</mxCell>
```

**Đặc điểm:**
- `dashed=1;dashPattern=5 5` — long dash, phân biệt với account group (solid border)
- `strokeColor=#CD2264` — Security/org color
- `container=1` — chứa các buckets bên trong
- `fillColor=none` — transparent
- Label ở top-left: "SSE-KMS Encryption"
- **KHÔNG PHẢI** account group (không có `grIcon`)

#### Element 2: KMS Dependency Edge (dashed, từ KMS → scope boundary)

```xml
<!-- KMS → Encryption Scope: dependency edge (encrypts relationship) -->
<mxCell id="e-kms-scope" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#C7131F;dashed=1;dashPattern=5 5;endArrow=classic;endFill=1;startArrow=none;startFill=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="kms-icon" target="kms-scope">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Đặc điểm:**
- Target = scope container (NOT individual buckets) — 1 edge covers all
- `dashed=1;dashPattern=5 5` — matches scope boundary dash pattern
- `strokeColor=#C7131F` — Security category
- `strokeWidth=1` — thin, dependency (not data flow)
- **⚠️ ARROW DIRECTION MANDATORY**: `endArrow=classic;endFill=1` trỏ VÀO scope/target. `startArrow=none` phía KMS. KHÔNG được đảo ngược — KMS là source (provider), resource là target (consumer of encryption).

**Khác với E4 (generic dependency):**
- E4 = strokeColor varies, dashPattern default
- E17 = strokeColor luôn `#C7131F`, dashPattern `5 5` (long dash, matches scope box)
- E17 target luôn là scope container, không phải individual resource

**Placement:**
- KMS icon: đặt trong source account (Security Account) hoặc ở level diagram root
- Scope container: bao quanh NHÓM resources cần encrypt (thường trong Log Archive Account)
- Edge: horizontal hoặc vertical tuỳ layout, cross-account

---

### 16.6 — Rule #2 Clarification: Cross-Boundary

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

### 16.7 — Cross-Account Log Aggregation Pattern (composite)

**Pattern tổng hợp** cho Log Aggregation diagrams — kết hợp Case 12 + Case 3b + E12b + E16 + E17.

**Layout structure (from production):**

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ┌── Member Accounts ──────┐    ┌── Log Archive Account ─────────┐ │
│  │ [VPC]→[DNS]→[TGW]→[██] ─┼───→│  [Bucket: Network]             │ │
│  └─────────────────────────┘    │         │ (E16 dashed pink)     │ │
│                                  │         ▼                       │ │
│  ┌── Security Account ────┐    │  ┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐      │ │
│  │ [GD]                    │    │  ╎ SSE-KMS Encryption    ╎      │ │
│  │  ↓ (E12b)              │    │  ╎                       ╎      │ │
│  │ [SH]→[Firehose] ───────┼─┬──│──╎→[Bucket: Security]   ╎      │ │
│  │ [KMS]╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌─┼─╌──│──╎  (E17 scope)        ╎      │ │
│  └─────────────────────────┘ │  │  ╎         │            ╎      │ │
│                              │  │  ╎         ▼            ╎      │ │
│  ┌── Audit Account ───────┐ │  │  ╎  [Bucket: CloudTrail]╎      │ │
│  │ [CT Trail]──────────────┼─┤  │  ╎         │            ╎      │ │
│  │ [Config Bucket]─────────┼─┘  │  ╎         ▼            ╎      │ │
│  └─────────────────────────┘    │  ╎  [Bucket: Config]    ╎      │ │
│                                  │  └╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘      │ │
│                                  └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

**Edge types used in this pattern:**

| Connection | Edge Type | Color | Style |
|---|---|---|---|
| VPC → DNS → TGW (intra-account chain) | **E12b variant** (chain steps) | `#8C4FFF` (Networking) | solid, strokeWidth=2 |
| TGW → Aggregation Connector (intra) | E12b | `#8C4FFF` | solid, strokeWidth=2 |
| Connector → Network Bucket (cross-acct) | Case 3b Variant B single output | `#8C4FFF` | solid, strokeWidth=2 |
| GuardDuty → Security Hub (intra-account) | **E12b** | `#C7131F` (Security) | solid, strokeWidth=2 |
| Security Hub → Firehose (intra-account) | **E12b** | `#C7131F` | solid, strokeWidth=2 |
| Firehose → Security Bucket (cross-acct) | **Case 12** trunk | `#C7131F` | solid, strokeWidth=2 |
| Firehose → CloudTrail Bucket (cross-acct) | **Case 12** trunk branch | `#C7131F` | solid, strokeWidth=2 |
| Trail/Config → respective Buckets (cross-acct) | **Case 12** trunk branch | `#CD2264` | solid, strokeWidth=2 |
| KMS → Encryption Scope (dependency) | **E17** | `#C7131F` | dashed, dashPattern=5 5, strokeWidth=1 |
| Bucket → Bucket (vertical ordering) | **E16** | `#CD2264` (org pink) | dashed, dashPattern=3 3, strokeWidth=1, có arrowhead |

**Spacing for this pattern:**
- Left column (source accounts): x=50 to x=450
- Trunk corridor gap: x=450 to x=580
- Right column (Log Archive + buckets): x=600 to x=900
- Vertical gap between account containers: 40-60px
- Vertical gap between buckets: 140-180px (includes label + E16 arrow space)
- KMS scope dashed box: bao quanh all buckets trong Log Archive, padding 20px


  Edge exits/enters container boundary?
  ├─ Source HOẶC target trong container đó → OK (allowed)
  └─ NEITHER source nor target trong container → VIOLATION (route around)
```

---

### 16.8 — GuardDuty → Security Hub (MANDATORY connection in Security diagrams)

**⚠️ CRITICAL RULE**: Trong MỌI Security Logging / Security Admin diagram, GuardDuty **PHẢI** có edge đến Security Hub. Đây là AWS best practice — GuardDuty gửi findings đến Security Hub để tổng hợp, KHÔNG gửi thẳng sang S3/Firehose.

**Mandatory flow:**
```
GuardDuty ──(E12b)──→ Security Hub ──→ EventBridge ──→ Kinesis Firehose ──→ S3 Bucket
```

**⛔ FORBIDDEN:**
```
GuardDuty ──────────────────────────────────────────────────────────→ S3 Bucket   (missing Security Hub)
GuardDuty ─────────────────────────────────────→ Kinesis Firehose                 (missing Security Hub)
```

**Edge spec (GuardDuty → Security Hub):**
```xml
<mxCell id="e-gd-sh" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#C7131F;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="i-guardduty" target="i-security-hub">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Kiểm tra khi validate:**
1. Tìm GuardDuty cell trong diagram
2. Verify CÓ edge với `source="guardduty-id"`
3. Verify edge đó `target="security-hub-id"` (KHÔNG phải Firehose, KHÔNG phải S3)

---

### 16.9 — Fan-in Entry Point Stagger (N sources → 1 target, same entry side)

**Vấn đề**: Khi N edges cùng enter một target từ CÙNG 1 phía (vd: cả 3 sources đều vào từ bên trái), tất cả dùng `entryX=0;entryY=0.5` → chồng chất tại 1 điểm trên target icon, bị merge thành 1 đường.

**Giải pháp: Stagger entryY theo số lượng sources:**

| Sources (N) | entryY values |
|---|---|
| 2 | 0.3, 0.7 |
| 3 | 0.2, 0.5, 0.8 |
| 4 | 0.2, 0.4, 0.6, 0.8 |
| 5+ | chia đều trong [0.1, 0.9] |

**Ví dụ — 3 sources vào Logging Bucket từ trái:**
```xml
<!-- Source A → Bucket: entryY=0.2 (upper left) -->
<mxCell id="e-a-bucket" style="edgeStyle=orthogonalEdgeStyle;...;entryX=0;entryY=0.2;entryDx=0;entryDy=0;" ...>

<!-- Source B → Bucket: entryY=0.5 (mid left) -->
<mxCell id="e-b-bucket" style="edgeStyle=orthogonalEdgeStyle;...;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" ...>

<!-- Source C → Bucket: entryY=0.8 (lower left) -->
<mxCell id="e-c-bucket" style="edgeStyle=orthogonalEdgeStyle;...;entryX=0;entryY=0.8;entryDx=0;entryDy=0;" ...>
```

**Khi KHÔNG cần stagger:**
- Sources đến từ các phía KHÁC NHAU (top / bottom / left / right) → mỗi phía tự nhiên phân tán
- Chỉ stagger khi 2+ sources vào từ CÙNG 1 phía của target

**Kết hợp với Junction Point (Case 3b):**
- Nếu N sources dùng Junction Point merge trước → chỉ CÓ 1 edge vào target → KHÔNG cần stagger
- Stagger chỉ áp dụng khi mỗi source có edge RIÊNG đến target
