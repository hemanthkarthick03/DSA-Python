# Quick Start Guide - Social Media App

```text
📦 Complete Setup Package
Configuration Files Created:
📋 Setup_Guide.md - Comprehensive setup instructions
🔧 pom.xml - Maven configuration with all dependencies
🐳 docker-compose.yml - Complete Docker setup with PostgreSQL, Redis, and app
📦 Dockerfile - Optimized multi-stage Docker build
⚙️ application.properties - Full Spring Boot configuration
🚀 Quick_Start.md - Get running in under 5 minutes
🚀 Three Ways to Run the Code
Option 1: Super Quick Start (Recommended)
# 1. Create project directory
mkdir social-media-app && cd social-media-app

# 2. Copy all files from Social_Media_System_Design folder

# 3. Start everything with Docker
docker-compose up -d

# 4. Test the application
curl http://localhost:8080/actuator/health
Option 2: Manual Setup
# 1. Install prerequisites
# - Java 11+, Maven 3.6+, PostgreSQL 12+, Redis 6+

# 2. Setup database
sudo -u postgres createdb social_media

# 3. Build and run
mvn clean package
java -jar target/social-media-app-1.0.0.jar
Option 3: IDE Development
Import Maven project in IntelliJ/Eclipse
Start PostgreSQL and Redis locally
Run SocialMediaApplication.java main class
🧪 Test the Running Application
Health Check
curl http://localhost:8080/actuator/health
# Returns: {"status":"UP"}
Register User
curl -X POST http://localhost:8080/api/v1/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com", 
    "password": "password123",
    "fullName": "Test User"
  }'
Create Post
curl -X POST http://localhost:8080/api/v1/posts \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "photoUrl": "https://picsum.photos/800/600",
    "caption": "My first post! 🎉"
  }'
Get Feed
curl -X GET http://localhost:8080/api/v1/feed \
  -H "X-User-Id: 1"
🔧 Key Features Included
Production-Ready Setup:
✅ Multi-stage Docker build for optimized images
✅ Health checks for all services
✅ Connection pooling with HikariCP
✅ Redis clustering support
✅ Comprehensive logging configuration
✅ Metrics and monitoring with Actuator
✅ API documentation with Swagger/OpenAPI
Development Tools:
✅ Hot reload with Spring DevTools
✅ pgAdmin for database management
✅ Redis Commander for cache management
✅ Swagger UI for API testing
✅ Comprehensive error handling
Configuration Profiles:
✅ dev - Local development
✅ docker - Docker containers
✅ prod - Production deployment
🎯 Access Points
Once running, you can access:

API Base: http://localhost:8080/api/v1
Swagger UI: http://localhost:8080/swagger-ui.html
Health Check: http://localhost:8080/actuator/health
pgAdmin: http://localhost:5050 (with tools profile)
Redis Commander: http://localhost:8081 (with tools profile)
🐛 Troubleshooting Included
The setup guide includes solutions for:

Port conflicts
Database connection issues
Redis connection problems
Memory optimization
Performance tuning
Common Docker issues
📊 Perfect for Interviews
This setup is ideal for Amazon SDE interviews because:

Quick Demo: Start in under 5 minutes
Complete Functionality: All features working
Production Quality: Real-world configuration
Easy Testing: Sample data and API calls included
Monitoring: Health checks and metrics
Scalable: Docker-based deployment ready
```

Get the Social Media System Design application running in under 5 minutes!

## 🚀 Super Quick Start (Docker)

### Prerequisites
- Docker and Docker Compose installed
- 4GB+ RAM available
- Ports 8080, 5432, 6379 available

### 1. Clone/Download the Project
```bash
# Create project directory
mkdir social-media-app
cd social-media-app

# Copy all the files from Social_Media_System_Design folder here
```

### 2. Start Everything with One Command
```bash
docker-compose up -d
```

### 3. Wait for Services to Start (2-3 minutes)
```bash
# Check if all services are running
docker-compose ps

# Check application logs
docker-compose logs -f app
```

### 4. Test the Application
```bash
# Health check
curl http://localhost:8080/actuator/health

# Should return: {"status":"UP"}
```

### 5. Access the Application
- **API Base URL**: http://localhost:8080/api/v1
- **Swagger UI**: http://localhost:8080/swagger-ui.html
- **Health Check**: http://localhost:8080/actuator/health

---

## 🧪 Test the APIs

### Register a New User
```bash
curl -X POST http://localhost:8080/api/v1/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "fullName": "Test User"
  }'
```

### Create a Post
```bash
curl -X POST http://localhost:8080/api/v1/posts \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "photoUrl": "https://picsum.photos/800/600",
    "thumbnailUrl": "https://picsum.photos/200/200",
    "caption": "My first post! 🎉"
  }'
```

### Get User Feed
```bash
curl -X GET http://localhost:8080/api/v1/feed \
  -H "X-User-Id: 1"
```

---

## 🛠️ Manual Setup (Alternative)

### Prerequisites
- Java 11+
- Maven 3.6+
- PostgreSQL 12+
- Redis 6+

### 1. Setup Database
```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Create database
sudo -u postgres createdb social_media
sudo -u postgres createuser app_user
sudo -u postgres psql -c "ALTER USER app_user WITH PASSWORD 'app_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE social_media TO app_user;"
```

### 2. Setup Redis
```bash
# Install Redis
sudo apt install redis-server

# Start Redis
sudo systemctl start redis-server
```

### 3. Build and Run Application
```bash
# Build the application
mvn clean package

# Run the application
java -jar target/social-media-app-1.0.0.jar
```

---

## 📊 Monitoring and Management

### Database Management (pgAdmin)
```bash
# Start pgAdmin (optional)
docker-compose --profile tools up pgadmin -d

# Access at: http://localhost:5050
# Email: admin@socialmedia.com
# Password: admin123
```

### Redis Management
```bash
# Start Redis Commander (optional)
docker-compose --profile tools up redis-commander -d

# Access at: http://localhost:8081
```

### Application Metrics
- **Health**: http://localhost:8080/actuator/health
- **Metrics**: http://localhost:8080/actuator/metrics
- **Info**: http://localhost:8080/actuator/info

---

## 🔧 Configuration

### Environment Variables
```bash
# Database
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/social_media
SPRING_DATASOURCE_USERNAME=app_user
SPRING_DATASOURCE_PASSWORD=app_password

# Redis
SPRING_REDIS_HOST=localhost
SPRING_REDIS_PORT=6379

# Application
SPRING_PROFILES_ACTIVE=dev
SERVER_PORT=8080
```

### Custom Configuration
Edit `application.properties` to customize:
- Database connection settings
- Redis configuration
- Logging levels
- Cache TTL values
- File upload limits

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Check what's using port 8080
sudo lsof -i :8080

# Kill the process
sudo kill -9 <PID>

# Or change port in application.properties
server.port=8081
```

#### 2. Database Connection Failed
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Check if database exists
psql -h localhost -U app_user -d social_media -c "\l"

# Reset database if needed
docker-compose down -v
docker-compose up postgres -d
```

#### 3. Redis Connection Failed
```bash
# Check Redis status
redis-cli ping

# Should return: PONG

# Restart Redis if needed
docker-compose restart redis
```

#### 4. Application Won't Start
```bash
# Check application logs
docker-compose logs app

# Common fixes:
# - Ensure database is running
# - Ensure Redis is running
# - Check Java version (needs 11+)
# - Check available memory
```

### Performance Issues

#### 1. Slow Database Queries
```sql
-- Check slow queries
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 10;

-- Add missing indexes
CREATE INDEX CONCURRENTLY idx_posts_user_created ON posts(user_id, created_at DESC);
```

#### 2. High Memory Usage
```bash
# Adjust JVM settings
export JAVA_OPTS="-Xms256m -Xmx512m"

# Or in docker-compose.yml
environment:
  - JAVA_OPTS=-Xms256m -Xmx512m
```

---

## 📝 Sample Data

### Create Sample Users
```bash
# User 1
curl -X POST http://localhost:8080/api/v1/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "email": "alice@example.com", "password": "password123", "fullName": "Alice Johnson"}'

# User 2
curl -X POST http://localhost:8080/api/v1/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "bob", "email": "bob@example.com", "password": "password123", "fullName": "Bob Smith"}'
```

### Create Sample Posts
```bash
# Alice's post
curl -X POST http://localhost:8080/api/v1/posts \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "photoUrl": "https://picsum.photos/800/600?random=1", "caption": "Beautiful sunset! 🌅"}'

# Bob's post
curl -X POST http://localhost:8080/api/v1/posts \
  -H "Content-Type: application/json" \
  -d '{"userId": 2, "photoUrl": "https://picsum.photos/800/600?random=2", "caption": "Coffee time ☕"}'
```

### Create Relationships
```bash
# Alice follows Bob
curl -X POST http://localhost:8080/api/v1/users/2/follow \
  -H "X-User-Id: 1"

# Bob follows Alice
curl -X POST http://localhost:8080/api/v1/users/1/follow \
  -H "X-User-Id: 2"
```

---

## 🚦 Health Checks

### Application Health
```bash
curl http://localhost:8080/actuator/health
```

### Database Health
```bash
# Check database connection
psql -h localhost -U app_user -d social_media -c "SELECT 1;"
```

### Redis Health
```bash
# Check Redis connection
redis-cli ping
```

### Full System Check
```bash
#!/bin/bash
echo "Checking system health..."

# Check application
if curl -f http://localhost:8080/actuator/health > /dev/null 2>&1; then
    echo "✅ Application: UP"
else
    echo "❌ Application: DOWN"
fi

# Check database
if psql -h localhost -U app_user -d social_media -c "SELECT 1;" > /dev/null 2>&1; then
    echo "✅ Database: UP"
else
    echo "❌ Database: DOWN"
fi

# Check Redis
if redis-cli ping > /dev/null 2>&1; then
    echo "✅ Redis: UP"
else
    echo "❌ Redis: DOWN"
fi
```

---

## 🎯 Next Steps

1. **Explore APIs**: Use Swagger UI at http://localhost:8080/swagger-ui.html
2. **Add Features**: Extend the codebase with new functionality
3. **Performance Testing**: Use tools like JMeter or k6
4. **Security**: Implement JWT authentication
5. **Monitoring**: Add Prometheus and Grafana
6. **Deployment**: Deploy to AWS, GCP, or Azure

---

## 📚 Additional Resources

- **API Documentation**: http://localhost:8080/swagger-ui.html
- **Database Schema**: See `Database_Design.md`
- **Architecture**: See `System_Architecture.md`
- **Interview Guide**: See `Interview_Discussion.md`

---

**🎉 Congratulations! Your Social Media System Design is now running!**

The application is ready for demonstration, testing, and further development. Perfect for Amazon SDE interviews and learning system design concepts.