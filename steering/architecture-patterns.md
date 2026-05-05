# AWS Architecture Diagram Patterns

Common layouts for AWS architecture diagrams.

## Table of Contents

1. [Cloud Architecture](#cloud-architecture)
2. [DRaaS / Replication](#draas-replication)
3. [Microservices](#microservices)
4. [Network Topology](#network-topology)
5. [CI/CD Pipeline](#cicd-pipeline)

---

## Cloud Architecture

### Three-Zone Layout (Source → Platform → Destination)

Best for: Migration, DR, data flow diagrams

```
┌─────────────┐   ┌─────────────────┐   ┌─────────────┐
│   SOURCE    │   │    PLATFORM     │   │ DESTINATION │
│  (Left)     │──►│    (Center)     │──►│   (Right)   │
│             │   │                 │   │             │
└─────────────┘   └─────────────────┘   └─────────────┘
```

**XML Pattern:**
```xml
<!-- Left Zone -->
<mxCell id="zone-left" value="" style="rounded=1;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1">
  <mxGeometry x="40" y="100" width="300" height="400" as="geometry" />
</mxCell>

<!-- Center Zone (use brand primary from steering/branding.md) -->
<mxCell id="zone-center" value="" style="rounded=1;fillColor=#0066CC;strokeColor=#0066CC;" vertex="1" parent="1">
  <mxGeometry x="380" y="100" width="300" height="400" as="geometry" />
</mxCell>

<!-- Right Zone -->
<mxCell id="zone-right" value="" style="rounded=1;fillColor=#e8f5e9;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="720" y="100" width="300" height="400" as="geometry" />
</mxCell>
```

### Layered Stack (Top to Bottom)

Best for: Application architecture, OSI model, tech stacks

```
┌────────────────────────────────────┐
│         Presentation Layer          │
├────────────────────────────────────┤
│          Application Layer          │
├────────────────────────────────────┤
│           Service Layer             │
├────────────────────────────────────┤
│            Data Layer               │
└────────────────────────────────────┘
```

**Spacing:** 80-100px height per layer, 20px gap between layers

---

## DRaaS / Replication

### DR Flow Pattern

```
┌──────────────┐                      ┌──────────────┐
│  PRODUCTION  │    ═══════════►      │   DR SITE    │
│   (Active)   │    Replication       │  (Standby)   │
│      🟢      │                      │      ⚪      │
└──────────────┘                      └──────────────┘
        │                                    │
        │         ┌──────────────┐           │
        └────────►│ Orchestrator │◄──────────┘
                  │   Platform   │
                  └──────────────┘
```

**Key Elements:**
- Status indicators (ellipse with green/grey fill)
- Flex arrows for replication flow
- Dashed arrows for failover paths
- Central orchestrator platform

### Failover/Failback Section

Place at bottom of diagram with dashed border:

```xml
<mxCell id="failover-section" value="" style="rounded=1;fillColor=#fff5f5;strokeColor=#b85450;strokeWidth=2;dashed=1;" vertex="1" parent="1">
  <mxGeometry x="40" y="600" width="1000" height="150" as="geometry" />
</mxCell>
```

---

## Microservices

### Service Mesh Pattern

```
        ┌─────────┐
        │ Gateway │
        └────┬────┘
             │
    ┌────────┼────────┐
    │        │        │
┌───▼──┐ ┌──▼───┐ ┌──▼───┐
│Svc A │ │Svc B │ │Svc C │
└───┬──┘ └──┬───┘ └──┬───┘
    │       │        │
    └───────┼────────┘
            │
       ┌────▼────┐
       │ Message │
       │  Queue  │
       └────┬────┘
            │
       ┌────▼────┐
       │Database │
       └─────────┘
```

**Colors by function:**
- Gateway/API: Yellow (`#fff2cc`)
- Services: Blue (`#dae8fc`)
- Queue/Messaging: Orange (`#ffe6cc`)
- Database: Red (`#f8cecc`)

---

## Network Topology

### Hub and Spoke

```
                    ┌──────────┐
           ┌────────│  Spoke 1 │
           │        └──────────┘
           │
      ┌────▼────┐   ┌──────────┐
      │   HUB   │───│  Spoke 2 │
      └────┬────┘   └──────────┘
           │
           │        ┌──────────┐
           └────────│  Spoke 3 │
                    └──────────┘
```

### VPC/Subnet Layout

```xml
<!-- VPC Container -->
<mxCell id="vpc" value="VPC 10.0.0.0/16" style="swimlane;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="600" height="400" as="geometry" />
</mxCell>

<!-- Public Subnet -->
<mxCell id="public-subnet" value="Public Subnet 10.0.1.0/24" style="swimlane;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="120" y="150" width="260" height="150" as="geometry" />
</mxCell>

<!-- Private Subnet -->
<mxCell id="private-subnet" value="Private Subnet 10.0.2.0/24" style="swimlane;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
  <mxGeometry x="420" y="150" width="260" height="150" as="geometry" />
</mxCell>
```

---

## CI/CD Pipeline

### Linear Pipeline

```
┌──────┐   ┌───────┐   ┌──────┐   ┌────────┐   ┌────────┐
│ Code │──►│ Build │──►│ Test │──►│ Deploy │──►│ Monitor│
└──────┘   └───────┘   └──────┘   └────────┘   └────────┘
```

**Stage colors (left to right):**
1. Code: Blue
2. Build: Yellow
3. Test: Orange
4. Deploy: Green
5. Monitor: Purple

### Pipeline with Environments

```
                    ┌─────────────────────────────────────┐
                    │              Pipeline               │
┌──────┐   ┌───────┐│  ┌─────┐   ┌─────┐   ┌──────────┐ │
│ Code │──►│ Build │├─►│ Dev │──►│ UAT │──►│Production│ │
└──────┘   └───────┘│  └─────┘   └─────┘   └──────────┘ │
                    └─────────────────────────────────────┘
```

---

## Tips for Complex AWS Diagrams

1. **Group by account** — Use account containers as primary grouping
2. **Consistent spacing** — 20-40px between elements, 60-100px between accounts
3. **Flow direction** — Pick one (L→R or T→B) and stick with it
4. **Color coding** — Use AWS category colors, max 5-6 with legend
5. **Labels on arrows** — Use for protocol/port/action descriptions
6. **Status indicators** — Small circles (green=active, grey=standby)
7. **Multi-AZ** — Always show AZ boundaries for production workloads
