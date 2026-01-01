# AWS Cheatsheet 🚀

## Core Services Overview 🏗️

### Compute Services 💻
- **EC2** ⚡ - Virtual servers in the cloud
- **Lambda** 🔥 - Serverless compute (pay per execution)
- **ECS** 🐳 - Container orchestration service
- **EKS** ☸️ - Managed Kubernetes service
- **Fargate** 🚢 - Serverless containers
- **Batch** 📊 - Batch computing jobs
- **Elastic Beanstalk** 🌱 - Easy app deployment

### Storage Services 💾
- **S3** 🪣 - Object storage (99.999999999% durability)
- **EBS** 💿 - Block storage for EC2
- **EFS** 📁 - Managed file system
- **FSx** 🗂️ - High-performance file systems
- **Storage Gateway** 🌉 - Hybrid cloud storage
- **Glacier** 🧊 - Long-term archival storage

### Database Services 🗄️
- **RDS** 🐘 - Managed relational databases
- **DynamoDB** ⚡ - NoSQL database (single-digit ms latency)
- **ElastiCache** 🚀 - In-memory caching (Redis/Memcached)
- **DocumentDB** 📄 - MongoDB-compatible
- **Neptune** 🌊 - Graph database
- **Redshift** 📈 - Data warehouse
- **Aurora** 🌅 - MySQL/PostgreSQL compatible

## Networking & Content Delivery 🌐

### Core Networking 🔗
- **VPC** 🏠 - Virtual private cloud
- **Route 53** 🗺️ - DNS service
- **CloudFront** 🌍 - CDN (Content Delivery Network)
- **API Gateway** 🚪 - Managed API service
- **Direct Connect** 🔌 - Dedicated network connection
- **VPN** 🔒 - Site-to-site VPN connections

### Load Balancing ⚖️
- **ALB** 🎯 - Application Load Balancer (Layer 7)
- **NLB** 🏃 - Network Load Balancer (Layer 4)
- **CLB** 🔄 - Classic Load Balancer (Legacy)

## Security & Identity 🔐

### Identity Management 👤
- **IAM** 🆔 - Identity and Access Management
- **Cognito** 🧠 - User authentication service
- **SSO** 🔑 - Single Sign-On
- **Directory Service** 📋 - Managed Active Directory

### Security Services 🛡️
- **WAF** 🔥 - Web Application Firewall
- **Shield** 🛡️ - DDoS protection
- **GuardDuty** 👁️ - Threat detection
- **Inspector** 🔍 - Security assessment
- **Secrets Manager** 🤐 - Manage secrets securely
- **KMS** 🔐 - Key Management Service

## Monitoring & Management 📊

### Monitoring 👀
- **CloudWatch** 📈 - Monitoring and observability
- **X-Ray** 🔍 - Distributed tracing
- **CloudTrail** 👣 - API call logging
- **Config** ⚙️ - Resource configuration tracking

### Management Tools 🛠️
- **CloudFormation** 📋 - Infrastructure as Code
- **CDK** 🏗️ - Cloud Development Kit
- **Systems Manager** 🎛️ - Operational insights
- **OpsWorks** 👨‍🍳 - Configuration management

## Analytics & Machine Learning 🤖

### Analytics 📊
- **Kinesis** 🌊 - Real-time data streaming
- **EMR** 🐘 - Big data processing (Hadoop/Spark)
- **Athena** 🔍 - Serverless query service
- **QuickSight** 📊 - Business intelligence
- **Glue** 🔗 - ETL service

### Machine Learning 🧠
- **SageMaker** 🤖 - ML platform
- **Rekognition** 👁️ - Image/video analysis
- **Comprehend** 📝 - Natural language processing
- **Polly** 🗣️ - Text-to-speech
- **Lex** 💬 - Chatbot service

## Developer Tools 👨‍💻

### CI/CD Pipeline 🔄
- **CodeCommit** 📝 - Git repositories
- **CodeBuild** 🔨 - Build service
- **CodeDeploy** 🚀 - Deployment service
- **CodePipeline** 🔗 - CI/CD pipeline
- **CodeStar** ⭐ - Unified development

### Development 💻
- **Cloud9** ☁️ - Cloud IDE
- **CLI** 💻 - Command line interface
- **SDK** 📚 - Software development kits

## Messaging & Integration 📨

### Messaging 💌
- **SQS** 📬 - Message queuing service
- **SNS** 📢 - Notification service
- **SES** 📧 - Email service
- **EventBridge** 🌉 - Event bus service

### Integration 🔗
- **Step Functions** 🪜 - Workflow orchestration
- **AppSync** 🔄 - GraphQL service
- **MQ** 📨 - Managed message broker

## Cost Management 💰

### Pricing Models 💳
- **On-Demand** ⚡ - Pay as you use
- **Reserved** 💾 - 1-3 year commitments (up to 75% savings)
- **Spot** 🎯 - Bid for unused capacity (up to 90% savings)
- **Savings Plans** 💰 - Flexible pricing model

### Cost Tools 📊
- **Cost Explorer** 🔍 - Analyze spending
- **Budgets** 💰 - Set cost alerts
- **Trusted Advisor** 💡 - Cost optimization recommendations

## Best Practices 🌟

### Security 🔒
- Enable MFA for root account 🔐
- Use IAM roles instead of access keys 🆔
- Encrypt data at rest and in transit 🔐
- Regular security audits 🔍

### Performance ⚡
- Use CloudFront for global content delivery 🌍
- Implement auto-scaling 📈
- Choose right instance types 💻
- Monitor with CloudWatch 📊

### Cost Optimization 💰
- Use Reserved Instances for predictable workloads 💾
- Implement lifecycle policies for S3 🪣
- Right-size your resources 📏
- Use Spot Instances for fault-tolerant workloads 🎯

### Reliability 🛡️
- Design for failure 💥
- Use multiple AZs 🌐
- Implement backup strategies 💾
- Test disaster recovery 🚨

## Common CLI Commands 💻

### EC2 Commands ⚡
```bash
# List instances
aws ec2 describe-instances

# Start instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Stop instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```

### S3 Commands 🪣
```bash
# List buckets
aws s3 ls

# Copy file to S3
aws s3 cp file.txt s3://bucket-name/

# Sync directory
aws s3 sync ./local-folder s3://bucket-name/folder/
```

### Lambda Commands 🔥
```bash
# List functions
aws lambda list-functions

# Invoke function
aws lambda invoke --function-name my-function output.txt
```

## Region & Availability Zones 🌍

### Key Concepts 🗺️
- **Region** 🌎 - Geographic area with multiple AZs
- **AZ** 🏢 - Isolated data center within region
- **Edge Location** 📍 - CloudFront cache location

### Popular Regions 🌟
- **us-east-1** 🇺🇸 - N. Virginia (cheapest, most services)
- **us-west-2** 🇺🇸 - Oregon
- **eu-west-1** 🇪🇺 - Ireland
- **ap-southeast-1** 🇸🇬 - Singapore

## Certification Paths 🎓

### Associate Level 📚
- **Cloud Practitioner** ☁️ - Foundational
- **Solutions Architect** 🏗️ - Most popular
- **Developer** 👨‍💻 - Development focused
- **SysOps Administrator** ⚙️ - Operations focused

### Professional Level 🎯
- **Solutions Architect Professional** 🏆
- **DevOps Engineer Professional** 🔧

### Specialty 🎨
- **Security** 🔒
- **Machine Learning** 🤖
- **Data Analytics** 📊
- **Database** 🗄️

## Quick Reference 📋

### Instance Types 💻
- **t3/t4g** 💡 - Burstable (general purpose)
- **m5/m6i** ⚖️ - Balanced (general purpose)
- **c5/c6i** ⚡ - Compute optimized
- **r5/r6i** 🧠 - Memory optimized
- **i3/i4i** 💾 - Storage optimized

### Storage Classes 🪣
- **Standard** ⚡ - Frequently accessed
- **IA** 🔄 - Infrequently accessed
- **Glacier** 🧊 - Archive (minutes to hours)
- **Deep Archive** ❄️ - Long-term archive (12+ hours)

### Database Engines 🗄️
- **MySQL** 🐬 - Open source relational
- **PostgreSQL** 🐘 - Advanced open source
- **Oracle** 🏛️ - Enterprise database
- **SQL Server** 🪟 - Microsoft database
- **Aurora** 🌅 - AWS managed (MySQL/PostgreSQL)

---

*Remember: AWS is constantly evolving! 🚀 Always check the latest documentation for updates.*