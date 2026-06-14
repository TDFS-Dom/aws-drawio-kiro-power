# Geometry Rules (Extracted from Reference Diagrams)

> Auto-generated from 4 .drawio files. These are ACTUAL measurements, not estimates.
> Use these numbers in SKILL.md for spacing calculations.

## 1. Container Sizes (actual)

Total containers analyzed: 836

| Type | Count | Width (min/avg/max) | Height (min/avg/max) |
|---|---|---|---|
| subnet | 309 | 90 / 149 / 520 | 65 / 112 / 320 |
| vpc | 183 | 120 / 325 / 1220 | 80 / 210 / 730 |
| account | 108 | 160 / 615 / 2110 | 80 / 412 / 1510 |
| dashed_box | 86 | 113 / 377 / 880 | 30 / 319 / 916 |
| other | 85 | 140 / 553 / 1420 | 130 / 352 / 1040 |
| region | 33 | 160 / 493 / 1100 | 160 / 284 / 400 |
| onprem | 32 | 110 / 210 / 500 | 100 / 207 / 520 |

## 2. Icon Sizes (actual)

| Size (WxH) | Count | Usage |
|---|---|---|
| 78x78 | 203 | primary |
| 50x50 | 176 | primary |
| 60x60 | 173 | primary |
| 40x40 | 90 | primary |
| 45x45 | 83 | primary |
| 80x80 | 57 | primary |
| 100x100 | 45 | secondary |
| 30x30 | 31 | secondary |
| 74x78 | 27 | secondary |
| 78x67 | 22 | secondary |
| 78x77 | 15 | secondary |
| 78x44 | 15 | secondary |
| 48x48 | 15 | secondary |
| 50x42 | 9 | rare |
| 75x78 | 8 | rare |

## 3. Spacing Between Icons (actual)

**Horizontal gaps**: min=2, avg=73, median=60, max=190 (n=245)

**Vertical gaps**: min=1, avg=67, median=53, max=255 (n=171)

## 4. Icon-to-Container Padding (actual)

| Edge | Min | Avg | Median | Max | N |
|---|---|---|---|---|---|
| Left | 10 | 70 | 50 | 196 | 397 |
| Top | 6 | 63 | 41 | 199 | 400 |
| Right | 10 | 135 | 81 | 494 | 522 |
| Bottom | 5 | 112 | 50 | 494 | 548 |

## 5. RECOMMENDED VALUES (for SKILL.md)

Based on the actual measurements above:

```
HORIZONTAL_GAP_BETWEEN_ICONS = 60 px (median from 245 measurements)
VERTICAL_GAP_BETWEEN_ICONS   = 53 px (median from 171 measurements)
CONTAINER_TOP_PADDING        = 41 px (median from 400 measurements)
CONTAINER_LEFT_PADDING       = 50 px (median from 397 measurements)
CONTAINER_RIGHT_MARGIN       = 81 px (median)
CONTAINER_BOTTOM_MARGIN      = 50 px (median)
MOST_COMMON_ICON_SIZE        = 78x78 (203x used)
```


---

## 6. LABEL-AWARE SPACING (MANDATORY — AI frequently violates)

> **Research basis**: Failed diagram where 3 icons horizontal with long labels ("VPC Flow Logs", "DNS Query Logs", "TGW Flow Logs") overlapped into unreadable text.

### The Problem

Icons using `verticalLabelPosition=bottom` render a text label BELOW the icon. The label width is determined by text length × font size, NOT by the icon width. When icons are placed horizontally with standard gap (60px), labels overflow into adjacent icons' label space.

### Label Width Estimation

```
label_pixel_width ≈ character_count × 7.2  (for fontSize=12, average character width)
```

| Example Label | Chars | Estimated Width | Icon Width | Overflow? |
|---|---|---|---|---|
| "S3" | 2 | 14px | 78px | ❌ No |
| "KMS" | 3 | 22px | 78px | ❌ No |
| "GuardDuty" | 9 | 65px | 78px | ❌ No |
| "VPC Flow Logs" | 13 | 94px | 78px | ⚠️ Tight |
| "DNS Query Logs" | 14 | 101px | 78px | ✅ YES — overflow 23px |
| "Kinesis Firehose" | 16 | 115px | 78px | ✅ YES — overflow 37px |
| "CT CloudTrail Bucket" | 20 | 144px | 75px | ✅ YES — overflow 69px |

### Rule G-LABEL-1: Minimum horizontal gap MUST account for label width

```
required_gap = max(HORIZONTAL_GAP, (max_label_width - icon_width) + 20px)
```

**Decision matrix:**

| Max label length (chars) | Required horizontal gap | Icon size 78px → center-to-center |
|---|---|---|
| ≤ 10 chars | 60px (standard) | 138px |
| 11-14 chars | 80px | 158px |
| 15-18 chars | 100px | 178px |
| 19+ chars | 120px+ OR use line break `&#xa;` | 198px+ |

### Rule G-LABEL-2: Use line break for long labels

When label exceeds 14 characters, PREFER splitting with `&#xa;` (XML newline):

```xml
<!-- ❌ WRONG — label "CT CloudTrail Bucket" is 20 chars, will overlap neighbors -->
<mxCell value="CT CloudTrail Bucket" .../>

<!-- ✅ CORRECT — split into 2 lines, each ≤14 chars -->
<mxCell value="CT CloudTrail&#xa;Bucket" .../>
```

### Rule G-LABEL-3: Alternative — use smaller icon size for dense horizontal layouts

When 3+ icons must fit in a narrow container (≤300px wide) with long labels:

```
Option A: Reduce icon size from 78x78 → 50x50 or 60x60 + reduce fontSize to 10
Option B: Arrange vertically instead of horizontally (eliminates label overlap)
Option C: Use abbreviated labels ("VPC Flow" instead of "VPC Flow Logs")
```

### Anti-Patterns

#### ❌ AP-G1: Three 78px icons with 14+ char labels in 200px container

```
┌──────────── 200px ────────────┐
│ [78] [78] [78]                │  ← icons fit
│ VPC Flow LogDNS QueryTGW Flow │  ← labels OVERLAP
└───────────────────────────────┘
```

**Fix**: Either widen container to 485px+ OR arrange icons vertically OR abbreviate labels.

#### ❌ AP-G2: Horizontal gap = 10-15px between icons with bottom labels

```
[Icon1][Icon2][Icon3]   ← gap=10px
 LabelLabelLabel         ← impossible to read
```

**Fix**: Minimum gap between icons with `verticalLabelPosition=bottom` = **60px** regardless of icon size. For labels >10 chars, increase to 80-120px per decision matrix above.

### Container Width Calculation WITH labels

```
container_width = left_pad + Σ(icon_widths) + Σ(gaps) + right_pad

WHERE gap = max(60, (max_label_chars - 10) × 7 + 20)

Example: 3 icons (78px each), labels "GuardDuty"(9), "Security Hub"(12), "Kinesis Firehose"(16)
  max_label = 16 chars → gap = max(60, (16-10)*7+20) = max(60, 62) = 62px (round to 65)
  width = 50 + 78 + 65 + 78 + 65 + 78 + 81 = 495px minimum
```
