# How to Run the Social Media System Design Code

This guide will help you set up and run the complete Social Media platform locally for testing and demonstration purposes.

## Prerequisites

### Required Software
- **Java 11 or higher** (OpenJDK recommended)
- **Maven 3.6+** (for dependency management)
- **PostgreSQL 12+** (database)
- **Redis 6+** (caching)
- **Git** (version control)
- **IDE** (IntelliJ IDEA, Eclipse, or VS Code)

### Optional Tools
- **Docker & Docker Compose** (for easy setup)
- **Postman** (for API testing)
- **pgAdmin** (PostgreSQL GUI)

---

## Quick Start with Docker (Recommended)

### Step 1: Create Project Structure
```bash
mkdir social-media-app
cd social-media-app
```

### Step 2: Create Docker Compose File
Create `docker-compose.yml` in the project root:

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:13
    container_name: social_media_db
    environment:
      POSTGRES_DB: social_media
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - social_media_network

  redis:
    image: redis:6-alpine
    container_name: social_media_redis
    ports:
      - "6379:6379"
    networks:
      - social_media_network

  app:
    build: .
    container_name: social_media_app
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      - SPRING_DATASOURCE_URL=jdbc:postgresql://postgres:5432/social_media
      - SPRING_DATASOURCE_USERNAME=app_user
      - SPRING_DATASOURCE_PASSWORD=app_password
      - SPRING_REDIS_HOST=redis
      - SPRING_REDIS_PORT=6379
    depends_on:
      - postgres
      - redis
    networks:
      - social_media_network

volumes:
  postgres_data:

networks:
  social_media_network:
    driver: bridge
```

### Step 3: Start Services
```bash
# Start database and Redis only (for development)
docker-compose up postgres redis -d

# Or start all services including the app
docker-compose up -d
```

---

## Manual Setup (Step by Step)

### Step 1: Set Up Database

#### Install PostgreSQL
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# macOS with Homebrew
brew install postgresql
brew services start postgresql

# Windows - Download from https://www.postgresql.org/download/
```

#### Create Database and User
```bash
# Connect to PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE social_media;
CREATE USER app_user WITH PASSWORD 'app_password';
GRANT ALL PRIVILEGES ON DATABASE social_media TO app_user;
\q
```

#### Initialize Database Schema
```bash
# Connect to the database
psql -h localhost -U app_user -d social_media

# Run the schema creation script (copy from Database_Design.md)
```

### Step 2: Set Up Redis

#### Install Redis
```bash
# Ubuntu/Debian
sudo apt install redis-server

# macOS with Homebrew
brew install redis
brew services start redis

# Windows - Download from https://redis.io/download
```

#### Start Redis
```bash
redis-server
```

### Step 3: Set Up Java Application

#### Create Maven Project Structure
```
social-media-app/
├── src/
│   └── main/
│       ├── java/
│       │   └── com/
│       │       └── socialmedia/
│       │           ├── SocialMediaApplication.java
│       │           ├── entity/
│       │           ├── repository/
│       │           ├── service/
│       │           ├── controller/
│       │           ├── dto/
│       │           └── exception/
│       └── resources/
│           ├── application.properties
│           └── application-docker.properties
├── pom.xml
├── Dockerfile
└── docker-compose.yml
```

---

## Configuration Files

### 1. Maven Configuration (pom.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.0</version>
        <relativePath/>
    </parent>

    <groupId>com.socialmedia</groupId>
    <artifactId>social-media-app</artifactId>
    <version>1.0.0</version>
    <name>Social Media App</name>
    <description>Social Media Platform for Amazon SDE Interview</description>

    <properties>
        <java.version>11</java.version>
    </properties>

    <dependencies>
        <!-- Spring Boot Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <!-- Database -->
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Redis -->
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
        </dependency>

        <!-- JSON Processing -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </dependency>

        <!-- Testing -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <!-- Development Tools -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

### 2. Application Properties
Create `src/main/resources/application.properties`:
```properties
# Server Configuration
server.port=8080
server.servlet.context-path=/

# Database Configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/social_media
spring.datasource.username=app_user
spring.datasource.password=app_password
spring.datasource.driver-class-name=org.postgresql.Driver

# JPA Configuration
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.properties.hibernate.format_sql=true

# Redis Configuration
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.timeout=2000ms
spring.redis.jedis.pool.max-active=8
spring.redis.jedis.pool.max-idle=8
spring.redis.jedis.pool.min-idle=0

# Logging Configuration
logging.level.com.socialmedia=DEBUG
logging.level.org.springframework.web=INFO
logging.pattern.console=%d{yyyy-MM-dd HH:mm:ss} - %msg%n

# File Upload Configuration
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=10MB

# Security Configuration (for development)
spring.security.user.name=admin
spring.security.user.password=admin123
```

Create `src/main/resources/application-docker.properties`:
```properties
# Docker-specific configuration
spring.datasource.url=jdbc:postgresql://postgres:5432/social_media
spring.redis.host=redis
logging.level.com.socialmedia=INFO
```

### 3. Dockerfile
```dockerfile
FROM openjdk:11-jre-slim

WORKDIR /app

COPY target/social-media-app-1.0.0.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Running the Application

### Option 1: Using Docker Compose (Easiest)
```bash
# Clone or create the project
git clone <your-repo> social-media-app
cd social-media-app

# Build and start all services
docker-compose up --build

# The application will be available at http://localhost:8080
```

### Option 2: Manual Setup
```bash
# 1. Start PostgreSQL and Redis
sudo systemctl start postgresql
sudo systemctl start redis

# 2. Create database schema
psql -h localhost -U app_user -d social_media -f init.sql

# 3. Build the application
mvn clean package

# 4. Run the application
java -jar target/social-media-app-1.0.0.jar

# Or run with Maven
mvn spring-boot:run
```

### Option 3: IDE Setup
1. **Import Project**: Open your IDE and import the Maven project
2. **Configure Database**: Ensure PostgreSQL is running with correct credentials
3. **Configure Redis**: Ensure Redis is running on localhost:6379
4. **Run Application**: Run the `SocialMediaApplication.java` main class

---

## Testing the Application

### 1. Health Check
```bash
curl http://localhost:8080/actuator/health
```

### 2. API Testing with cURL

#### Register a User
```bash
curl -X POST http://localhost:8080/api/v1/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123",
    "fullName": "John Doe"
  }'
```

#### Get User Profile
```bash
curl -X GET http://localhost:8080/api/v1/users/1
```

#### Create a Post
```bash
curl -X POST http://localhost:8080/api/v1/posts \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "photoUrl": "https://example.com/photo.jpg",
    "caption": "My first post!"
  }'
```

#### Get User Feed
```bash
curl -X GET http://localhost:8080/api/v1/feed \
  -H "X-User-Id: 1"
```

### 3. Database Verification
```bash
# Connect to database
psql -h localhost -U app_user -d social_media

# Check tables
\dt

# Check users
SELECT * FROM users;

# Check posts
SELECT * FROM posts;
```

### 4. Redis Verification
```bash
# Connect to Redis
redis-cli

# Check cached data
KEYS *
GET user:1
```

---

## Troubleshooting

### Common Issues

#### 1. Database Connection Error
```
Error: FATAL: password authentication failed for user "app_user"
```
**Solution**: 
- Check PostgreSQL is running: `sudo systemctl status postgresql`
- Verify user credentials: `psql -h localhost -U app_user -d social_media`
- Reset password if needed

#### 2. Redis Connection Error
```
Error: Could not connect to Redis at localhost:6379
```
**Solution**:
- Check Redis is running: `redis-cli ping`
- Start Redis: `sudo systemctl start redis`

#### 3. Port Already in Use
```
Error: Port 8080 is already in use
```
**Solution**:
- Change port in `application.properties`: `server.port=8081`
- Or kill process using port: `sudo lsof -t -i:8080 | xargs kill -9`

#### 4. Maven Build Errors
```
Error: Could not resolve dependencies
```
**Solution**:
- Clean Maven cache: `mvn clean`
- Update dependencies: `mvn dependency:resolve`
- Check internet connection

### Performance Optimization

#### 1. Database Indexing
```sql
-- Add indexes for better performance
CREATE INDEX CONCURRENTLY idx_posts_user_created ON posts(user_id, created_at DESC);
CREATE INDEX CONCURRENTLY idx_follows_follower ON follows(follower_id);
CREATE INDEX CONCURRENTLY idx_likes_post ON likes(post_id);
```

#### 2. Redis Configuration
```properties
# Optimize Redis for development
spring.redis.jedis.pool.max-active=20
spring.redis.jedis.pool.max-idle=10
spring.redis.jedis.pool.min-idle=5
```

#### 3. JVM Tuning
```bash
# Run with optimized JVM settings
java -Xms512m -Xmx1024m -jar target/social-media-app-1.0.0.jar
```

---

## Development Workflow

### 1. Making Changes
```bash
# Make code changes
# Rebuild application
mvn clean package

# Restart application
docker-compose restart app
# Or if running manually
java -jar target/social-media-app-1.0.0.jar
```

### 2. Database Migrations
```bash
# Create migration script
# Apply to database
psql -h localhost -U app_user -d social_media -f migration.sql
```

### 3. Testing Changes
```bash
# Run unit tests
mvn test

# Run integration tests
mvn verify

# Manual API testing with Postman or cURL
```

---

## Production Deployment

### 1. Environment Variables
```bash
export SPRING_PROFILES_ACTIVE=production
export SPRING_DATASOURCE_URL=jdbc:postgresql://prod-db:5432/social_media
export SPRING_DATASOURCE_USERNAME=prod_user
export SPRING_DATASOURCE_PASSWORD=secure_password
export SPRING_REDIS_HOST=prod-redis
```

### 2. Build for Production
```bash
# Build optimized JAR
mvn clean package -Pprod

# Build Docker image
docker build -t social-media-app:latest .
```

### 3. Deploy
```bash
# Deploy with Docker
docker run -d \
  --name social-media-app \
  -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=production \
  social-media-app:latest
```

This setup guide provides everything needed to run the Social Media System Design code locally or in production. The Docker approach is recommended for quick setup and testing.