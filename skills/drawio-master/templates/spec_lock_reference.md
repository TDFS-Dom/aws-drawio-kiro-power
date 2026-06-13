# spec_lock — {project_name}

> Machine-readable execution contract. Executor re-reads this before generating XML.
> On divergence with design_spec.md, this file wins.

## canvas

| key | value |
|-----|-------|
| pageWidth | {W} |
| pageHeight | {H} |
| grid | 1 |
| gridSize | 10 |
| shadow | 0 |
| dx | {dx} |
| dy | {dy} |

## template

| key | value |
|-----|-------|
| id | {ou-hierarchy / security-iam / networking / aft-pipeline} |
| file | {template filename} |

## containers

| type | grIcon | strokeColor | fillColor | fontColor | dashed | fontSize |
|------|--------|-------------|-----------|-----------|--------|----------|
| account | mxgraph.aws4.group_account | #CD2264 | none | #CD2264 | 0 | 16 |
| region | mxgraph.aws4.group_region | #00A4A6 | none | #147EBA | 1 | 12 |
| vpc | mxgraph.aws4.group_vpc2 | #00CC00 | none | #AAB7B8 | 0 | 15 |
| on_premise | mxgraph.aws4.group_corporate_data_center | #7D8998 | none | #5A6C86 | 0 | 16 |
| ou_boundary | — | #5A6C86 | none | #5A6C86 | 1 | — |

## icons

| service | shape | fillColor | gradientColor | strokeColor | size |
|---------|-------|-----------|---------------|-------------|------|
| {service_name} | mxgraph.aws4.{shape} | #{hex} | #{hex or —} | #ffffff | {WxH} |

## edges

| id | type | strokeColor | strokeWidth | endArrow | dashed | label |
|----|------|-------------|-------------|----------|--------|-------|
| {id} | {connection type} | #{hex} | {N} | {classic/none} | {0/1} | {text} |

## env_colors

| env | color |
|-----|-------|
| Prod | rgb(0,204,0) |
| NonProd | rgb(0,0,255) |
| Standard | #232F3E |
