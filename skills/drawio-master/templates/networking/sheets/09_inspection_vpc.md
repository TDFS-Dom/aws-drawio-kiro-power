# Sheet 9: Inspection VPC

> Source: `ACB_Networking_diagrams .drawio` — sheet `Inspection VPC`
> Copy style strings EXACTLY when generating this pattern.

**Elements**: 4 containers, 9 icons, 6 edges, 6 other

## Containers

**Inspection VPC** (1080x730)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

**Availability Zone** (320x570)
```
fillColor=none;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#147EBA;whiteSpace=wrap;html=1;
```

**mgmt-subnet-2** (130x110)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

**mgmt-subnet-3** (130x110)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#006EAF;fillColor=#CCCCCC;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

## Icons

**EN-1** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;
```

**Palo Alto<div>Ingress</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#ED7100;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.instance2;
```

**TGW<div>ENI</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=right;
```

**GWLB<div>Ingress</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.gateway_load_balancer;labelPosition=center;
```

**GWLB<br>Endpoint** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=right;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.endpoints;labelPosition=left;
```

**Transit Gateway** (78x78)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;
```

**EN-1** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#808080;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;
```

**TGW<div>ENI</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#808080;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=right;
```

**GWLB<br>Endpoint** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#808080;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=right;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.endpoints;labelPosition=left;
```

## Edges

**CWZydYkUblhC1WrD9l9W-26**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;dashed=1;strokeColor=#999999;
```

**CWZydYkUblhC1WrD9l9W-27**
```
edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;dashed=1;strokeColor=#999999;
```

**CWZydYkUblhC1WrD9l9W-28**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;dashed=1;endArrow=none;endFill=0;strokeColor=#999999;
```

**CWZydYkUblhC1WrD9l9W-61**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;endArrow=none;endFill=0;
```

**CWZydYkUblhC1WrD9l9W-65**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;dashed=1;endArrow=none;endFill=0;strokeColor=#B3B3B3;
```

**CWZydYkUblhC1WrD9l9W-66**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;dashed=1;endArrow=none;endFill=0;strokeColor=#B3B3B3;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;
```

## Other Shapes

**CWZydYkUblhC1WrD9l9W-8** (470x570)
```
group
```

**Management subnet route table** (220x80)
```
shape=table;startSize=20;container=1;collapsible=0;childLayout=tableLayout;fillColor=#b1ddf0;strokeColor=#10739e;fontStyle=1
```

**CWZydYkUblhC1WrD9l9W-68** (220x30)
```
shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;strokeColor=inherit;top=0;left=0;bottom=0;right=0;collapsible=0;dropTarget=0;fillColor=none;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;
```

**<b>CIDR Range</b>** (110x30)
```
shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;strokeColor=inherit;overflow=hidden;fillColor=none;top=0;left=0;bottom=0;right=0;pointerEvents=1;
```

**10.4.0.0/22** (110x30)
```
shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;strokeColor=inherit;overflow=hidden;fillColor=none;top=0;left=0;bottom=0;right=0;pointerEvents=1;align=center;fontSize=14;
```

**GWLB Endpoint subnet route table** (220x100)
```
shape=table;startSize=30;container=1;collapsible=0;childLayout=tableLayout;fillColor=#B1DDF0;fontStyle=1
```
