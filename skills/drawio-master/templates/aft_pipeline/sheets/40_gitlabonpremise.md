# Sheet 40: GitLabOnpremise

> Source: `AFT.drawio` — sheet `GitLabOnpremise`
> Copy style strings EXACTLY when generating this pattern.

**Elements**: 4 containers, 5 icons, 5 edges, 1 other

## Containers

**AWS Cloud** (810x630)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud;stroke=#232F3D;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;spacingTop=4;dashed=0;
```

**ACB AFT Management Account** (780x550)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;stroke=#CD2264;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;spacingTop=4;dashed=0;strokeColor=#CD2264;
```

**AFT VPC: 10.4.14.0/24** (460x390)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc;stroke=#248814;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;spacingTop=4;dashed=0;strokeColor=#8C4FFF;
```

**EC2 Self-Hosted GitLab** (410x167.34375)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_ec2_instance_contents;strokeColor=#D86613;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#D86613;dashed=0;
```

## Icons

**<b>Private Hosted Zone</b><br>gitlab.acb.internal<br>→ EC2 P** (50x50)
```
outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.route_53;
```

**aft-account-<br>request<br>Pipeline** (40x40)
```
outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codepipeline;
```

**<span style="color: rgb(35, 47, 62); font-size: 9px;">aft-ac** (40x40)
```
shape=image;html=1;verticalAlign=top;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;imageAspect=0;aspect=fixed;image=https://icons.diagrams.net/icon-cache1/Socialcones-2932/Gitlab-794.svg
```

**ENI** (48.4375x48.4375)
```
outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_network_interface;labelBackgroundColor=default;
```

**CodeConnection** (48.4375x48.4375)
```
outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codestar;labelBackgroundColor=default;
```

## Edges

**DNS Resolution**
```
html=1;exitX=0;exitY=0.5;entryX=0.75;entryY=0;endArrow=classic;endFill=1;strokeColor=#8C4FFF;fontSize=10;dashed=1;labelBackgroundColor=#FFFFFF;entryDx=0;entryDy=0;
```

**1P4zMxV0E-U4-9Dy38CU-113**
```
edgeStyle=orthogonalEdgeStyle;html=1;entryX=0;entryY=0.5;endArrow=classic;endFill=1;strokeColor=#C7131F;fontSize=9;
```

**1P4zMxV0E-U4-9Dy38CU-114**
```
edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;endFill=1;strokeColor=#C7131F;fontSize=9;
```

**(1) Mount endpoint to VPC**
```
edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;endFill=1;strokeColor=#232F3E;fontSize=10;labelBackgroundColor=#FFFFFF;
```

**(2) Network Traffic<br>(3) Local VPC routing<br>HTTPS :443 S**
```
edgeStyle=orthogonalEdgeStyle;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=classic;endFill=1;strokeColor=#232F3E;fontSize=10;labelBackgroundColor=#FFFFFF;
```

## Other Shapes

**<i>Temporary Phase: No Transit Gateway required.<br>When Dir** (220x50)
```
text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=#D6B656;fillColor=#FFF2CC;fontSize=10;fontColor=#232F3E;rounded=1;
```
