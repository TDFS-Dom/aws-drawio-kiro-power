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
