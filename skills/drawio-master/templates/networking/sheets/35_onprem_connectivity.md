# Sheet 35: Onprem connectivity

> Source: `ACB_Networking_diagrams .drawio` — sheet `Onprem connectivity`
> Copy style strings EXACTLY when generating this pattern.

**Elements**: 4 containers, 7 icons, 19 edges, 12 other

## Containers

**ACB Prod** (150x350)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_corporate_data_center;strokeColor=#7D8998;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#5A6C86;dashed=0;
```

**Network Account** (260x240)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#232F3E;dashed=0;
```

**<b><font style="color: light-dark(rgb(0, 0, 0), rgb(51, 0, 0** (440x160)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```

**tgw-subnet** (130x100)
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;
```

## Icons

**On-Premises<div>Firewall</div>** (59.09x50)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.generic_firewall;
```

**Servers** (45x78)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.traditional_server;
```

**AWS&nbsp;<div>Transit Gateway</div>** (78x78)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;labelPosition=center;
```

**TGW ENI** (40x40)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_interface;labelPosition=center;
```

**Workloads** (40x40)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#ED7100;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.instance2;
```

**DX** (45x45)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.direct_connect;labelPosition=center;
```

**VPN<div>Site to Site</div>** (45x45)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.site_to_site_vpn;
```

## Edges

**(4)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fillColor=#d5e8d4;strokeColor=#82b366;strokeWidth=2;fontColor=#97D077;
```

**(1)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF0000;strokeWidth=2;fontColor=#FF0000;
```

**zEKU1RoBySWI8pBhNCNk-18**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontColor=#3333FF;strokeColor=#3333FF;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-19**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#FF8000;
```

**vZ1-TSr21kNSaVNcxARY-8**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;dashed=1;
```

**vZ1-TSr21kNSaVNcxARY-9**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#97D077;strokeWidth=2;
```

**2MjKqOyjpFSPKDkhmqqn-15**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF0000;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-12**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#3333FF;
```

**(3)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#97D077;strokeWidth=2;fontColor=#97D077;
```

**(1)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontColor=#FF8000;strokeColor=#FF8000;strokeWidth=2;
```

**(3)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#3333FF;strokeWidth=2;fontColor=#3333FF;
```

**zEKU1RoBySWI8pBhNCNk-17**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF8000;strokeWidth=2;
```

**OINCT9MZDNsgrTDfKALy-22**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;
```

**zEKU1RoBySWI8pBhNCNk-4**
```
edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;html=1;rounded=0;fontSize=12;endArrow=none;endFill=0;strokeColor=#FF0000;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-6**
```
edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;html=1;rounded=0;fontSize=12;endArrow=none;endFill=0;strokeColor=#82B366;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-8**
```
edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;html=1;rounded=0;fontSize=12;endArrow=none;endFill=0;strokeColor=#3333FF;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-22**
```
edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;html=1;rounded=0;fontSize=12;endArrow=none;endFill=0;strokeColor=#FF8000;strokeWidth=2;
```

**zEKU1RoBySWI8pBhNCNk-26**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF8000;strokeWidth=2;fontColor=#FF8000;
```

**(3)**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF8000;strokeWidth=2;fontColor=#FF8000;exitX=0.25;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;
```

## Other Shapes

**(1)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];
```

**(4)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontColor=#FF8000;
```

**(1)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontColor=#97D077;
```

**(5)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontColor=#FF9933;
```

**(5)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontColor=#3333FF;
```

**(4)** ()
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontColor=#FF0000;
```

**<b>LEGENDS</b>** (60x30)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=16;
```

**zEKU1RoBySWI8pBhNCNk-3** (343x59)
```
rounded=0;whiteSpace=wrap;html=1;fillColor=#CCCCCC;
```

**<font color="#ff0000"><b>Primary</b></font><div><font color=** (124x30)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=9;
```

**<b>Primary</b><div><b>ACB's ELZ</b></div><div><b>to Onprem</** (124x30)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=9;fontColor=#82B366;
```

**<b><font>&nbsp;Backup</font></b><div><b><font>Onprem to&nbsp** (124x30)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=9;fontColor=#3333FF;
```

**<b><font>&nbsp;Backup</font></b><div><b><font>ACB's ELZ&nbsp** (124x30)
```
text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=9;fontColor=#FF8000;
```
