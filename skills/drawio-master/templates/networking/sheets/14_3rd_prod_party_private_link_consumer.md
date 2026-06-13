# Sheet 14: 3rd prod party private link - consumer

> Source: `ACB_Networking_diagrams .drawio` — sheet `3rd prod party private link - consumer`
> Copy style strings EXACTLY when generating this pattern.

**Elements**: 4 containers, 8 icons, 1 edges, 5 other

## Containers

**3rd Party Prod** (1120x580)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

**Availability Zone** (340x390)
```
fillColor=none;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#147EBA;whiteSpace=wrap;html=1;
```

**tgw-subnet-3** (150x100)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#CCCCCC;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

**tgw-subnet-1** (150x100)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

## Icons

**PrivateLink<div>That Partner Provide</div>** (50x50)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];resIcon=mxgraph.aws4.vpc_privatelink;
```

**AWS<div>Transit Gateway</div>** (50x50)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;
```

**TGW<div>ENI</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#808080;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=right;
```

**Wg7DXOkfGHthTmvbsvKW-9** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#808080;strokeColor=none;dashed=0;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=center;
```

**TGW<div>ENI</div>** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=right;
```

**Wg7DXOkfGHthTmvbsvKW-41** (45x45)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=center;
```

**VPC<div>Endpoints</div>** (50x50)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.endpoints;labelPosition=right;
```

**VPC<div>Endpoints</div>** (50x50)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=middle;verticalAlign=middle;align=right;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.endpoints;labelPosition=left;
```

## Edges

**Wg7DXOkfGHthTmvbsvKW-50**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;dashed=1;dashPattern=8 8;
```

## Other Shapes

**Service subnet route table** (150x185)
```
shape=table;startSize=32;container=1;collapsible=0;childLayout=tableLayout;fillColor=#B1DDF0;strokeColor=light-dark(#000000,#330000);fontStyle=1
```

**Wg7DXOkfGHthTmvbsvKW-15** (150x35)
```
shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;strokeColor=inherit;top=0;left=0;bottom=0;right=0;collapsible=0;dropTarget=0;fillColor=none;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;
```

**<b>CIDR Range</b>** (75x35)
```
shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;strokeColor=inherit;overflow=hidden;fillColor=none;top=0;left=0;bottom=0;right=0;pointerEvents=1;
```

**<span style="font-size: 12px;">10.4.36.0/22</span>** (75x28)
```
shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;strokeColor=inherit;overflow=hidden;fillColor=none;top=0;left=0;bottom=0;right=0;pointerEvents=1;align=center;fontSize=14;
```

**TGW subnet route table** (150x87)
```
shape=table;startSize=32;container=1;collapsible=0;childLayout=tableLayout;fillColor=#b1ddf0;strokeColor=#10739e;fontStyle=1
```
