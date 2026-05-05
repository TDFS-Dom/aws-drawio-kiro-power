# AWS Icons Reference

Draw.io has a built-in shape library for AWS services. This reference covers the mxCell syntax for using official AWS icons.

## Table of Contents

1. [AWS Icons (aws4)](#aws-icons-aws4)
2. [AWS Groups and Containers](#aws-groups-and-containers)
3. [Usage Tips](#usage-tips)

---

## AWS Icons (aws4)

AWS icons use the `mxgraph.aws4` shape library with the `resourceIcon` shape type.

### Base Style Template

```xml
<mxCell id="unique-id" value="Label" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#COLOR;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.SERVICE_NAME;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="78" height="78" as="geometry" />
</mxCell>
```

**CRITICAL**: `strokeColor=#ffffff` is MANDATORY for all AWS icons.

### AWS Service Categories and Colors

| Category | fillColor | Services |
|----------|-----------|----------|
| Compute | #ED7100 | ec2, lambda, ecs, eks, fargate, batch, lightsail |
| Storage | #7AA116 | s3, ebs, efs, fsx, storage_gateway, backup |
| Database | #C925D1 | rds, dynamodb, aurora, elasticache, redshift, neptune, documentdb, keyspaces |
| Networking | #8C4FFF | vpc, cloudfront, route53, api_gateway, elb, direct_connect, transit_gateway, global_accelerator |
| Security | #DD344C | iam, cognito, secrets_manager, kms, waf, shield, guardduty, inspector, macie |
| Management | #E7157B | cloudwatch, cloudformation, systems_manager, config, cloudtrail, organizations, control_tower |
| Analytics | #8C4FFF | kinesis, athena, emr, glue, quicksight, lake_formation, msk |
| Application | #E7157B | sns, sqs, step_functions, eventbridge, appsync |
| Migration | #7AA116 | migration_hub, dms, datasync, transfer_family |
| AI/ML | #01A88D | sagemaker, bedrock, comprehend, rekognition, textract, transcribe |
| Developer Tools | #C925D1 | codecommit, codebuild, codedeploy, codepipeline |
| Containers | #ED7100 | ecr, ecs, eks, fargate, app_runner |

### Common AWS Service Icons

#### Compute
```xml
<!-- EC2 -->
resIcon=mxgraph.aws4.ec2;fillColor=#ED7100

<!-- Lambda -->
resIcon=mxgraph.aws4.lambda;fillColor=#ED7100

<!-- ECS -->
resIcon=mxgraph.aws4.ecs;fillColor=#ED7100

<!-- EKS -->
resIcon=mxgraph.aws4.eks;fillColor=#ED7100

<!-- Fargate -->
resIcon=mxgraph.aws4.fargate;fillColor=#ED7100

<!-- Batch -->
resIcon=mxgraph.aws4.batch;fillColor=#ED7100

<!-- App Runner -->
resIcon=mxgraph.aws4.app_runner;fillColor=#ED7100
```

#### Storage
```xml
<!-- S3 -->
resIcon=mxgraph.aws4.s3;fillColor=#7AA116

<!-- EBS -->
resIcon=mxgraph.aws4.elastic_block_store;fillColor=#7AA116

<!-- EFS -->
resIcon=mxgraph.aws4.elastic_file_system;fillColor=#7AA116

<!-- FSx -->
resIcon=mxgraph.aws4.fsx;fillColor=#7AA116

<!-- Backup -->
resIcon=mxgraph.aws4.backup;fillColor=#7AA116
```

#### Database
```xml
<!-- RDS -->
resIcon=mxgraph.aws4.rds;fillColor=#C925D1

<!-- DynamoDB -->
resIcon=mxgraph.aws4.dynamodb;fillColor=#C925D1

<!-- Aurora -->
resIcon=mxgraph.aws4.aurora;fillColor=#C925D1

<!-- ElastiCache -->
resIcon=mxgraph.aws4.elasticache;fillColor=#C925D1

<!-- Redshift -->
resIcon=mxgraph.aws4.redshift;fillColor=#C925D1

<!-- Neptune -->
resIcon=mxgraph.aws4.neptune;fillColor=#C925D1

<!-- DocumentDB -->
resIcon=mxgraph.aws4.documentdb;fillColor=#C925D1
```

#### Networking
```xml
<!-- VPC -->
resIcon=mxgraph.aws4.vpc;fillColor=#8C4FFF

<!-- CloudFront -->
resIcon=mxgraph.aws4.cloudfront;fillColor=#8C4FFF

<!-- Route 53 -->
resIcon=mxgraph.aws4.route_53;fillColor=#8C4FFF

<!-- API Gateway -->
resIcon=mxgraph.aws4.api_gateway;fillColor=#E7157B

<!-- ELB / ALB -->
resIcon=mxgraph.aws4.elastic_load_balancing;fillColor=#8C4FFF

<!-- Direct Connect -->
resIcon=mxgraph.aws4.direct_connect;fillColor=#8C4FFF

<!-- Transit Gateway -->
resIcon=mxgraph.aws4.transit_gateway;fillColor=#8C4FFF

<!-- Global Accelerator -->
resIcon=mxgraph.aws4.global_accelerator;fillColor=#8C4FFF

<!-- PrivateLink / VPC Endpoint -->
resIcon=mxgraph.aws4.vpc_endpoint;fillColor=#8C4FFF

<!-- NAT Gateway -->
resIcon=mxgraph.aws4.nat_gateway;fillColor=#8C4FFF
```

#### Security & Identity
```xml
<!-- IAM -->
resIcon=mxgraph.aws4.identity_and_access_management;fillColor=#DD344C

<!-- Cognito -->
resIcon=mxgraph.aws4.cognito;fillColor=#DD344C

<!-- Secrets Manager -->
resIcon=mxgraph.aws4.secrets_manager;fillColor=#DD344C

<!-- KMS -->
resIcon=mxgraph.aws4.key_management_service;fillColor=#DD344C

<!-- WAF -->
resIcon=mxgraph.aws4.waf;fillColor=#DD344C

<!-- Shield -->
resIcon=mxgraph.aws4.shield;fillColor=#DD344C

<!-- GuardDuty -->
resIcon=mxgraph.aws4.guardduty;fillColor=#DD344C

<!-- Security Hub -->
resIcon=mxgraph.aws4.security_hub;fillColor=#DD344C

<!-- Inspector -->
resIcon=mxgraph.aws4.inspector;fillColor=#DD344C

<!-- Macie -->
resIcon=mxgraph.aws4.macie;fillColor=#DD344C

<!-- Certificate Manager -->
resIcon=mxgraph.aws4.certificate_manager;fillColor=#DD344C
```

#### Management & Governance
```xml
<!-- CloudWatch -->
resIcon=mxgraph.aws4.cloudwatch;fillColor=#E7157B

<!-- CloudFormation -->
resIcon=mxgraph.aws4.cloudformation;fillColor=#E7157B

<!-- Systems Manager -->
resIcon=mxgraph.aws4.systems_manager;fillColor=#E7157B

<!-- Config -->
resIcon=mxgraph.aws4.config;fillColor=#E7157B

<!-- CloudTrail -->
resIcon=mxgraph.aws4.cloudtrail;fillColor=#E7157B

<!-- Organizations -->
resIcon=mxgraph.aws4.organizations;fillColor=#E7157B

<!-- Control Tower -->
resIcon=mxgraph.aws4.control_tower;fillColor=#E7157B

<!-- Service Catalog -->
resIcon=mxgraph.aws4.service_catalog;fillColor=#E7157B

<!-- Trusted Advisor -->
resIcon=mxgraph.aws4.trusted_advisor;fillColor=#E7157B
```

#### Application Integration
```xml
<!-- SNS -->
resIcon=mxgraph.aws4.sns;fillColor=#E7157B

<!-- SQS -->
resIcon=mxgraph.aws4.sqs;fillColor=#E7157B

<!-- Step Functions -->
resIcon=mxgraph.aws4.step_functions;fillColor=#E7157B

<!-- EventBridge -->
resIcon=mxgraph.aws4.eventbridge;fillColor=#E7157B

<!-- AppSync -->
resIcon=mxgraph.aws4.appsync;fillColor=#E7157B
```

#### Analytics & Data
```xml
<!-- Kinesis -->
resIcon=mxgraph.aws4.kinesis;fillColor=#8C4FFF

<!-- Athena -->
resIcon=mxgraph.aws4.athena;fillColor=#8C4FFF

<!-- Glue -->
resIcon=mxgraph.aws4.glue;fillColor=#8C4FFF

<!-- EMR -->
resIcon=mxgraph.aws4.emr;fillColor=#8C4FFF

<!-- QuickSight -->
resIcon=mxgraph.aws4.quicksight;fillColor=#8C4FFF

<!-- Lake Formation -->
resIcon=mxgraph.aws4.lake_formation;fillColor=#8C4FFF

<!-- MSK (Kafka) -->
resIcon=mxgraph.aws4.managed_streaming_for_kafka;fillColor=#8C4FFF

<!-- OpenSearch -->
resIcon=mxgraph.aws4.elasticsearch_service;fillColor=#8C4FFF
```

#### Migration & Transfer
```xml
<!-- Database Migration Service -->
resIcon=mxgraph.aws4.database_migration_service;fillColor=#7AA116

<!-- DataSync -->
resIcon=mxgraph.aws4.datasync;fillColor=#7AA116

<!-- Migration Hub -->
resIcon=mxgraph.aws4.migration_hub;fillColor=#7AA116

<!-- Transfer Family -->
resIcon=mxgraph.aws4.transfer_family;fillColor=#7AA116
```

#### AI & Machine Learning
```xml
<!-- SageMaker -->
resIcon=mxgraph.aws4.sagemaker;fillColor=#01A88D

<!-- Bedrock (use generic ML if unavailable) -->
resIcon=mxgraph.aws4.machine_learning;fillColor=#01A88D

<!-- Comprehend -->
resIcon=mxgraph.aws4.comprehend;fillColor=#01A88D

<!-- Rekognition -->
resIcon=mxgraph.aws4.rekognition;fillColor=#01A88D

<!-- Textract -->
resIcon=mxgraph.aws4.textract;fillColor=#01A88D
```

#### Developer Tools
```xml
<!-- CodePipeline -->
resIcon=mxgraph.aws4.codepipeline;fillColor=#C925D1

<!-- CodeBuild -->
resIcon=mxgraph.aws4.codebuild;fillColor=#C925D1

<!-- CodeDeploy -->
resIcon=mxgraph.aws4.codedeploy;fillColor=#C925D1

<!-- CodeCommit -->
resIcon=mxgraph.aws4.codecommit;fillColor=#C925D1
```

### Complete AWS Icon Example

```xml
<mxCell id="aws-lambda-1" value="Lambda Function" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
  <mxGeometry x="200" y="200" width="78" height="78" as="geometry" />
</mxCell>
```

---

## AWS Groups and Containers

### AWS Cloud Container

```xml
<mxCell id="aws-cloud" value="AWS Cloud" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud;strokeColor=#AAB7B8;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="600" height="400" as="geometry" />
</mxCell>
```

### Region Container

```xml
<mxCell id="aws-region" value="ap-southeast-1" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#007F7F;dashed=1;" vertex="1" parent="1">
  <mxGeometry x="60" y="80" width="520" height="340" as="geometry" />
</mxCell>
```

### VPC Container

```xml
<mxCell id="aws-vpc" value="VPC 10.0.0.0/16" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="80" y="120" width="460" height="280" as="geometry" />
</mxCell>
```

### Public Subnet

```xml
<mxCell id="public-subnet" value="Public Subnet 10.0.1.0/24" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_public_subnet;strokeColor=#7AA116;fillColor=#E9F3E6;verticalAlign=top;align=left;spacingLeft=30;fontColor=#248814;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="100" y="160" width="200" height="200" as="geometry" />
</mxCell>
```

### Private Subnet

```xml
<mxCell id="private-subnet" value="Private Subnet 10.0.2.0/24" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_private_subnet;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="320" y="160" width="200" height="200" as="geometry" />
</mxCell>
```

### Availability Zone

```xml
<mxCell id="az-1" value="Availability Zone 1" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_availability_zone;strokeColor=#00A4A6;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#007F7F;dashed=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="160" width="200" height="200" as="geometry" />
</mxCell>
```

### Security Group

```xml
<mxCell id="security-group" value="Security Group" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;strokeColor=#DD344C;fillColor=#FFEBEE;verticalAlign=top;align=left;spacingLeft=30;fontColor=#DD344C;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="120" y="200" width="160" height="140" as="geometry" />
</mxCell>
```

### Account Container

```xml
<mxCell id="account" value="Production Account" style="sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=11;fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#FF8F00;fillColor=#FFF8E1;verticalAlign=top;align=left;spacingLeft=30;fontColor=#FF8F00;dashed=0;" vertex="1" parent="1">
  <mxGeometry x="60" y="80" width="400" height="300" as="geometry" />
</mxCell>
```

---

## Usage Tips

### Enabling AWS Library in draw.io

To access AWS icons in draw.io:
1. Click **More Shapes** at bottom of shapes panel
2. Expand **Networking** section
3. Enable **AWS 2019** or **AWS 2021** library
4. Click **Apply**

Or open draw.io with AWS pre-loaded: `https://app.diagrams.net/?libs=aws4`

### Icon Sizing

| Standard Size | Use Case |
|---------------|----------|
| 38-44px | Compact/A4 diagrams (recommended for multi-account) |
| 64x64 | Standard diagrams |
| 78x78 | AWS default (large diagrams) |

### Label Positioning

```xml
<!-- Label below icon (default for AWS) -->
verticalLabelPosition=bottom;verticalAlign=top;

<!-- Label to the right -->
labelPosition=right;align=left;verticalAlign=middle;

<!-- No label (icon only) -->
value=""
```

### Finding Icon Names

If unsure of exact icon name:
1. Open draw.io with AWS library enabled
2. Drag the icon onto canvas
3. Select it and press Ctrl+E (or Cmd+E on Mac) to view style
4. Copy the `resIcon=` value

### Newer Services Without Icons

For services not yet in the draw.io library (Bedrock, Q Developer, Clean Rooms, etc.):
- Use category generic icon: `resIcon=mxgraph.aws4.machine_learning` for AI services
- Or use: `resIcon=mxgraph.aws4.general_AWS_cloud` with clear label
- Add note in Legend: "⚠️ [Service] uses generic icon"
