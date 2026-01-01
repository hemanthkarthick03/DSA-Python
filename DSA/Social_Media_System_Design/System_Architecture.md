# System Architecture - Social Media Platform (SDE 1 Level)

## High-Level Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐
│   Mobile App    │    │    Web App      │
│   (iOS/Android) │    │   (React/Vue)   │
└─────────────────┘    └─────────────────┘
         │                       │
         └───────────┬───────────┘
                     │
              ┌─────────────┐
              │    CDN      │
              │ (CloudFront)│
              └─────────────┘
                     │
              ┌─────────────┐
              │Load Balancer│
              │   (AWS ALB) │
              └─────────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │   Server 1  │ │   Server 2  │ │   Server 3  │
  │ Spring Boot │ │ Spring Boot │ │ Spring Boot │
  └─────────────┘ └─────────────┘ └─────────────┘
         │           │           │
         └───────────┼───────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │ PostgreSQL  │ │    Redis    │ │   AWS S3    │
  │  (Primary)  │ │   (Cache)   │ │  (Photos)   │
  └─────────────┘ └─────────────┘ └─────────────┘
         │
  ┌─────────────┐
  │ PostgreSQL  │
  │ (Read Replica)│
  └─────────────┘
```

## Component Details

### 1. Client Layer
```
Mobile Applications:
- Native iOS/Android apps
- Photo capture and upload
- Offline capability for viewing cached content
- Push notifications (future enhancement)

Web Application:
- Responsive web interface
- Photo upload via browser
- Real-time feed updates
- Admin interface for basic management
```

### 2. Load Balancer (AWS Application Load Balancer)
```
Responsibilities:
- Distribute incoming requests across multiple servers
- Health checks for server availability
- SSL termination
- Basic DDoS protection

Configuration:
- Round-robin load balancing
- Health check endpoint: /health
- Sticky sessions not required (stateless design)
```

### 3. Application Servers (Spring Boot)
```java
// Main Application Structure
@SpringBootApplication
public class SocialMediaApplication {
    
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
    
    @Bean
    public RedisTemplate<String, Object> redisTemplate() {
        // Redis configuration for caching
        return new RedisTemplate<>();
    }
    
    public static void main(String[] args) {
        SpringApplication.run(SocialMediaApplication.class, args);
    }
}

// Core Controllers
@RestController
@RequestMapping("/api/v1")
public class SocialMediaController {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private PostService postService;
    
    @Autowired
    private FeedService feedService;
    
    // API endpoints implementation
}
```

### 4. Database Layer (PostgreSQL)

#### Primary Database
```sql
-- Core tables for SDE 1 level
CREATE DATABASE social_media;

-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts table
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    photo_url VARCHAR(500) NOT NULL,
    caption TEXT,
    like_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Follows table (social graph)
CREATE TABLE follows (
    follower_id INTEGER REFERENCES users(user_id),
    following_id INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, following_id)
);

-- Likes table
CREATE TABLE likes (
    user_id INTEGER REFERENCES users(user_id),
    post_id INTEGER REFERENCES posts(post_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, post_id)
);

-- Comments table
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(post_id),
    user_id INTEGER REFERENCES users(user_id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Basic indexes for performance
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);
CREATE INDEX idx_follows_follower ON follows(follower_id);
CREATE INDEX idx_follows_following ON follows(following_id);
CREATE INDEX idx_likes_post_id ON likes(post_id);
CREATE INDEX idx_comments_post_id ON comments(post_id);
```

#### Read Replica
```
Purpose: Handle read-heavy operations
- User profile queries
- Feed generation queries
- Post browsing
- Search operations

Configuration:
- Asynchronous replication from primary
- Read-only access
- Automatic failover to primary if needed
```

### 5. Caching Layer (Redis)
```
Cache Strategy:
- User profiles (TTL: 1 hour)
- Popular posts (TTL: 30 minutes)
- User feeds (TTL: 15 minutes)
- Like counts (TTL: 5 minutes)

Cache Patterns:
- Cache-aside for user data
- Write-through for like counts
- Cache warming for popular content
```

### 6. File Storage (AWS S3)
```
Photo Storage Strategy:
- Original photos in S3
- Multiple sizes (thumbnail, medium, large)
- CDN integration for fast delivery
- Lifecycle policies for cost optimization

Directory Structure:
/photos/
  /original/
    /{user_id}/
      /{post_id}/
        /photo.jpg
  /thumbnails/
    /{user_id}/
      /{post_id}/
        /thumb.jpg
```

## Data Flow Diagrams

### 1. User Registration Flow
```
User → Load Balancer → App Server → Validate Input → Hash Password → 
PostgreSQL → Cache User Data → Return Success Response
```

### 2. Photo Upload Flow
```
User → Load Balancer → App Server → Validate Photo → Resize Images → 
S3 Upload → Save Metadata to PostgreSQL → Invalidate Cache → 
Return Success Response
```

### 3. Feed Generation Flow
```
User Request → Load Balancer → App Server → Check Cache → 
(Cache Miss) → Query Following List → Query Posts from Read Replica → 
Sort by Timestamp → Cache Result → Return Feed
```

### 4. Like Post Flow
```
User → Load Balancer → App Server → Validate Request → 
Update PostgreSQL → Update Cache → Return Success Response
```

## Service Layer Architecture

### Core Services (SDE 1 Level)
```java
// User Service
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private RedisTemplate redisTemplate;
    
    public UserDto createUser(CreateUserRequest request) {
        // Implementation
    }
    
    public UserDto getUserById(Long userId) {
        // Check cache first, then database
    }
    
    public UserDto updateUser(Long userId, UpdateUserRequest request) {
        // Implementation with cache invalidation
    }
}

// Post Service
@Service
public class PostService {
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private S3Service s3Service;
    
    public PostDto createPost(CreatePostRequest request, MultipartFile photo) {
        // Upload photo to S3, save metadata to database
    }
    
    public List<PostDto> getUserPosts(Long userId, int page, int size) {
        // Paginated user posts
    }
    
    public PostDto likePost(Long postId, Long userId) {
        // Handle like/unlike logic
    }
}

// Feed Service
@Service
public class FeedService {
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private FollowRepository followRepository;
    
    public List<PostDto> getUserFeed(Long userId, int page, int size) {
        // Generate chronological feed from followed users
    }
}
```

## Scaling Strategy (SDE 1 Level)

### Immediate Scaling Solutions
```
1. Horizontal Scaling:
   - Add more application servers behind load balancer
   - Database read replicas for read-heavy operations
   - Redis cluster for distributed caching

2. Vertical Scaling:
   - Increase server resources (CPU, RAM)
   - Optimize database configuration
   - Tune JVM settings for Spring Boot

3. Content Delivery:
   - CDN for photo delivery
   - Image compression and multiple sizes
   - Browser caching headers
```

### Performance Optimizations
```
Database Optimizations:
- Proper indexing on frequently queried columns
- Connection pooling (HikariCP)
- Query optimization and EXPLAIN analysis
- Pagination for large result sets

Application Optimizations:
- Response caching for static content
- Async processing for non-critical operations
- Connection pooling for external services
- Proper error handling and timeouts

Caching Strategy:
- Cache frequently accessed user profiles
- Cache popular posts and feeds
- Cache like counts and follower counts
- Implement cache warming for popular content
```

## Security Architecture

### Basic Security Measures (SDE 1 Level)
```java
// Authentication & Authorization
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Bean
    public JwtAuthenticationFilter jwtAuthenticationFilter() {
        return new JwtAuthenticationFilter();
    }
    
    // Basic security configuration
}

// Input Validation
@RestController
public class UserController {
    
    @PostMapping("/register")
    public ResponseEntity<UserDto> registerUser(
            @Valid @RequestBody CreateUserRequest request) {
        // Validation handled by @Valid annotation
    }
}

// File Upload Security
@Component
public class FileUploadValidator {
    
    private static final List<String> ALLOWED_TYPES = 
        Arrays.asList("image/jpeg", "image/png");
    
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
    
    public void validateFile(MultipartFile file) {
        // Validate file type and size
    }
}
```

## Monitoring and Logging

### Basic Monitoring (SDE 1 Level)
```java
// Health Check Endpoint
@RestController
public class HealthController {
    
    @Autowired
    private DatabaseHealthIndicator databaseHealth;
    
    @Autowired
    private RedisHealthIndicator redisHealth;
    
    @GetMapping("/health")
    public ResponseEntity<HealthStatus> health() {
        // Return system health status
    }
}

// Basic Metrics
@Component
public class MetricsCollector {
    
    private final MeterRegistry meterRegistry;
    
    public void recordUserRegistration() {
        meterRegistry.counter("user.registrations").increment();
    }
    
    public void recordPostCreation() {
        meterRegistry.counter("post.creations").increment();
    }
}

// Logging Configuration
logging:
  level:
    com.socialmedia: INFO
    org.springframework.web: DEBUG
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/social-media.log
```

## Deployment Architecture

### Simple Deployment Strategy
```yaml
# Docker Compose for local development
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: social_media
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### AWS Deployment (Production)
```
Infrastructure Components:
- EC2 instances for application servers
- RDS PostgreSQL for database
- ElastiCache Redis for caching
- S3 for photo storage
- CloudFront CDN for content delivery
- Application Load Balancer for traffic distribution

Deployment Process:
1. Build application JAR
2. Create Docker image
3. Deploy to EC2 instances
4. Update load balancer targets
5. Run database migrations
6. Verify health checks
```

## Trade-offs and Design Decisions

### Key Design Decisions for SDE 1 Level

1. **Monolithic vs Microservices**
   - **Chosen**: Monolithic Spring Boot application
   - **Reason**: Simpler to develop, deploy, and debug for small team
   - **Trade-off**: Less scalable than microservices, but appropriate for initial scale

2. **SQL vs NoSQL Database**
   - **Chosen**: PostgreSQL (SQL)
   - **Reason**: Strong consistency, ACID properties, familiar to most developers
   - **Trade-off**: May need to consider NoSQL for specific use cases as scale increases

3. **Synchronous vs Asynchronous Processing**
   - **Chosen**: Mostly synchronous with some async for non-critical operations
   - **Reason**: Simpler to implement and debug
   - **Trade-off**: May impact performance for heavy operations

4. **Caching Strategy**
   - **Chosen**: Simple cache-aside pattern with Redis
   - **Reason**: Easy to implement and understand
   - **Trade-off**: Not the most efficient for all use cases, but good starting point

## Next Steps

1. **Database Design**: Detailed schema with relationships and constraints
2. **API Design**: RESTful endpoints with request/response specifications
3. **Implementation**: Core service logic and business rules
4. **Testing Strategy**: Unit tests and integration tests
5. **Deployment Guide**: Step-by-step deployment instructions

This architecture provides a solid foundation for an SDE 1 level system design interview while maintaining simplicity and focusing on core concepts.