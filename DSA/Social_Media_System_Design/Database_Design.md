# Database Design - Social Media Platform (SDE 1 Level)

## Database Schema Overview

### Entity Relationship Diagram
```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    USERS    │       │    POSTS    │       │   FOLLOWS   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ user_id (PK)│◄──────┤ user_id (FK)│       │follower_id  │
│ username    │       │ post_id (PK)│       │following_id │
│ email       │       │ photo_url   │       │ created_at  │
│ password_hash│      │ caption     │       └─────────────┘
│ full_name   │       │ like_count  │              │
│ bio         │       │ created_at  │              │
│ profile_pic │       └─────────────┘              │
│ created_at  │              │                     │
└─────────────┘              │                     │
       │                     │                     │
       │              ┌─────────────┐       ┌─────────────┐
       │              │    LIKES    │       │  COMMENTS   │
       │              ├─────────────┤       ├─────────────┤
       └──────────────┤ user_id (FK)│       │comment_id   │
                      │ post_id (FK)│       │ post_id (FK)│
                      │ created_at  │       │ user_id (FK)│
                      └─────────────┘       │ content     │
                                           │ created_at  │
                                           └─────────────┘
```

## Table Definitions

### 1. Users Table
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(500),
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Constraints
ALTER TABLE users ADD CONSTRAINT chk_username_length 
    CHECK (LENGTH(username) >= 3 AND LENGTH(username) <= 50);
ALTER TABLE users ADD CONSTRAINT chk_email_format 
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
```

### 2. Posts Table
```sql
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    photo_url VARCHAR(500) NOT NULL,
    thumbnail_url VARCHAR(500),
    caption TEXT,
    like_count INTEGER DEFAULT 0,
    comment_count INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);
CREATE INDEX idx_posts_user_created ON posts(user_id, created_at DESC);
CREATE INDEX idx_posts_like_count ON posts(like_count DESC);

-- Constraints
ALTER TABLE posts ADD CONSTRAINT chk_like_count_positive 
    CHECK (like_count >= 0);
ALTER TABLE posts ADD CONSTRAINT chk_comment_count_positive 
    CHECK (comment_count >= 0);
ALTER TABLE posts ADD CONSTRAINT chk_caption_length 
    CHECK (LENGTH(caption) <= 2200);
```

### 3. Follows Table (Social Graph)
```sql
CREATE TABLE follows (
    follower_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    following_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, following_id)
);

-- Indexes for performance
CREATE INDEX idx_follows_follower ON follows(follower_id);
CREATE INDEX idx_follows_following ON follows(following_id);
CREATE INDEX idx_follows_created_at ON follows(created_at);

-- Constraints
ALTER TABLE follows ADD CONSTRAINT chk_no_self_follow 
    CHECK (follower_id != following_id);
```

### 4. Likes Table
```sql
CREATE TABLE likes (
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES posts(post_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, post_id)
);

-- Indexes for performance
CREATE INDEX idx_likes_post_id ON likes(post_id);
CREATE INDEX idx_likes_user_id ON likes(user_id);
CREATE INDEX idx_likes_created_at ON likes(created_at);
```

### 5. Comments Table
```sql
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL REFERENCES posts(post_id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_comments_post_id ON comments(post_id);
CREATE INDEX idx_comments_user_id ON comments(user_id);
CREATE INDEX idx_comments_created_at ON comments(created_at);
CREATE INDEX idx_comments_post_created ON comments(post_id, created_at);

-- Constraints
ALTER TABLE comments ADD CONSTRAINT chk_content_not_empty 
    CHECK (LENGTH(TRIM(content)) > 0);
ALTER TABLE comments ADD CONSTRAINT chk_content_length 
    CHECK (LENGTH(content) <= 500);
```

## Database Functions and Triggers

### 1. Update Timestamp Trigger
```sql
-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply trigger to relevant tables
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_posts_updated_at 
    BEFORE UPDATE ON posts 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_comments_updated_at 
    BEFORE UPDATE ON comments 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 2. Like Count Management
```sql
-- Function to increment like count
CREATE OR REPLACE FUNCTION increment_like_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE posts 
    SET like_count = like_count + 1 
    WHERE post_id = NEW.post_id;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Function to decrement like count
CREATE OR REPLACE FUNCTION decrement_like_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE posts 
    SET like_count = like_count - 1 
    WHERE post_id = OLD.post_id;
    RETURN OLD;
END;
$$ language 'plpgsql';

-- Triggers for like count management
CREATE TRIGGER trigger_increment_like_count
    AFTER INSERT ON likes
    FOR EACH ROW EXECUTE FUNCTION increment_like_count();

CREATE TRIGGER trigger_decrement_like_count
    AFTER DELETE ON likes
    FOR EACH ROW EXECUTE FUNCTION decrement_like_count();
```

### 3. Comment Count Management
```sql
-- Function to increment comment count
CREATE OR REPLACE FUNCTION increment_comment_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE posts 
    SET comment_count = comment_count + 1 
    WHERE post_id = NEW.post_id;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Function to decrement comment count
CREATE OR REPLACE FUNCTION decrement_comment_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE posts 
    SET comment_count = comment_count - 1 
    WHERE post_id = OLD.post_id;
    RETURN OLD;
END;
$$ language 'plpgsql';

-- Triggers for comment count management
CREATE TRIGGER trigger_increment_comment_count
    AFTER INSERT ON comments
    FOR EACH ROW EXECUTE FUNCTION increment_comment_count();

CREATE TRIGGER trigger_decrement_comment_count
    AFTER DELETE ON comments
    FOR EACH ROW EXECUTE FUNCTION decrement_comment_count();
```

## Common Queries and Performance

### 1. User Feed Query (Most Important)
```sql
-- Get user feed with pagination
SELECT 
    p.post_id,
    p.photo_url,
    p.thumbnail_url,
    p.caption,
    p.like_count,
    p.comment_count,
    p.created_at,
    u.username,
    u.full_name,
    u.profile_picture_url
FROM posts p
JOIN users u ON p.user_id = u.user_id
WHERE p.user_id IN (
    SELECT following_id 
    FROM follows 
    WHERE follower_id = ?
)
AND p.is_active = TRUE
ORDER BY p.created_at DESC
LIMIT ? OFFSET ?;

-- Performance: Uses idx_posts_user_created and idx_follows_follower
-- Expected execution time: < 100ms for typical user
```

### 2. User Profile Query
```sql
-- Get user profile with stats
SELECT 
    u.user_id,
    u.username,
    u.full_name,
    u.bio,
    u.profile_picture_url,
    u.is_verified,
    u.created_at,
    COUNT(DISTINCT p.post_id) as post_count,
    COUNT(DISTINCT f1.following_id) as following_count,
    COUNT(DISTINCT f2.follower_id) as follower_count
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id AND p.is_active = TRUE
LEFT JOIN follows f1 ON u.user_id = f1.follower_id
LEFT JOIN follows f2 ON u.user_id = f2.following_id
WHERE u.user_id = ?
GROUP BY u.user_id;

-- Performance: Uses primary key lookup and indexes
-- Expected execution time: < 50ms
```

### 3. Post Details Query
```sql
-- Get post with user info and interaction status
SELECT 
    p.post_id,
    p.photo_url,
    p.thumbnail_url,
    p.caption,
    p.like_count,
    p.comment_count,
    p.created_at,
    u.username,
    u.full_name,
    u.profile_picture_url,
    u.is_verified,
    CASE WHEN l.user_id IS NOT NULL THEN TRUE ELSE FALSE END as is_liked_by_user
FROM posts p
JOIN users u ON p.user_id = u.user_id
LEFT JOIN likes l ON p.post_id = l.post_id AND l.user_id = ?
WHERE p.post_id = ?
AND p.is_active = TRUE;

-- Performance: Uses primary key lookups
-- Expected execution time: < 20ms
```

### 4. Search Users Query
```sql
-- Search users by username or full name
SELECT 
    user_id,
    username,
    full_name,
    profile_picture_url,
    is_verified
FROM users
WHERE (
    username ILIKE ? 
    OR full_name ILIKE ?
)
AND is_active = TRUE
ORDER BY 
    CASE WHEN username ILIKE ? THEN 1 ELSE 2 END,
    username
LIMIT ?;

-- Performance: Uses idx_users_username for prefix matches
-- Expected execution time: < 200ms
```

## Data Migration Scripts

### Initial Data Setup
```sql
-- Insert sample users for testing
INSERT INTO users (username, email, password_hash, full_name, bio) VALUES
('john_doe', 'john@example.com', '$2a$10$...', 'John Doe', 'Photography enthusiast'),
('jane_smith', 'jane@example.com', '$2a$10$...', 'Jane Smith', 'Travel blogger'),
('mike_wilson', 'mike@example.com', '$2a$10$...', 'Mike Wilson', 'Food lover');

-- Insert sample follows
INSERT INTO follows (follower_id, following_id) VALUES
(1, 2), (1, 3), (2, 1), (2, 3), (3, 1);

-- Insert sample posts
INSERT INTO posts (user_id, photo_url, thumbnail_url, caption) VALUES
(1, 'https://cdn.example.com/photos/1/post1.jpg', 'https://cdn.example.com/thumbs/1/post1.jpg', 'Beautiful sunset today! #sunset #photography'),
(2, 'https://cdn.example.com/photos/2/post1.jpg', 'https://cdn.example.com/thumbs/2/post1.jpg', 'Amazing trip to Paris 🇫🇷 #travel #paris'),
(3, 'https://cdn.example.com/photos/3/post1.jpg', 'https://cdn.example.com/thumbs/3/post1.jpg', 'Homemade pasta for dinner #food #cooking');

-- Insert sample likes
INSERT INTO likes (user_id, post_id) VALUES
(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2);

-- Insert sample comments
INSERT INTO comments (post_id, user_id, content) VALUES
(1, 2, 'Gorgeous shot!'),
(1, 3, 'Love the colors'),
(2, 1, 'Paris is amazing!'),
(3, 1, 'Looks delicious!');
```

## Database Configuration

### Connection Pool Settings
```properties
# application.properties
spring.datasource.url=jdbc:postgresql://localhost:5432/social_media
spring.datasource.username=app_user
spring.datasource.password=app_password
spring.datasource.driver-class-name=org.postgresql.Driver

# HikariCP connection pool settings
spring.datasource.hikari.maximum-pool-size=20
spring.datasource.hikari.minimum-idle=5
spring.datasource.hikari.idle-timeout=300000
spring.datasource.hikari.max-lifetime=600000
spring.datasource.hikari.connection-timeout=20000
spring.datasource.hikari.leak-detection-threshold=60000

# JPA settings
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=false
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.jdbc.batch_size=20
spring.jpa.properties.hibernate.order_inserts=true
spring.jpa.properties.hibernate.order_updates=true
```

### Read Replica Configuration
```java
@Configuration
public class DatabaseConfig {
    
    @Primary
    @Bean(name = "primaryDataSource")
    @ConfigurationProperties("spring.datasource.primary")
    public DataSource primaryDataSource() {
        return DataSourceBuilder.create().build();
    }
    
    @Bean(name = "replicaDataSource")
    @ConfigurationProperties("spring.datasource.replica")
    public DataSource replicaDataSource() {
        return DataSourceBuilder.create().build();
    }
    
    @Bean(name = "primaryEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean primaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("primaryDataSource") DataSource dataSource) {
        return builder
                .dataSource(dataSource)
                .packages("com.socialmedia.entity")
                .persistenceUnit("primary")
                .build();
    }
    
    @Bean(name = "replicaEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean replicaEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("replicaDataSource") DataSource dataSource) {
        return builder
                .dataSource(dataSource)
                .packages("com.socialmedia.entity")
                .persistenceUnit("replica")
                .build();
    }
}
```

## Database Monitoring

### Key Metrics to Monitor
```sql
-- Query performance monitoring
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- Index usage monitoring
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- Table size monitoring
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

## Backup and Recovery Strategy

### Daily Backup Script
```bash
#!/bin/bash
# backup_database.sh

DB_NAME="social_media"
DB_USER="app_user"
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup
pg_dump -h localhost -U $DB_USER -d $DB_NAME > $BACKUP_DIR/social_media_$DATE.sql

# Compress backup
gzip $BACKUP_DIR/social_media_$DATE.sql

# Keep only last 7 days of backups
find $BACKUP_DIR -name "social_media_*.sql.gz" -mtime +7 -delete

echo "Backup completed: social_media_$DATE.sql.gz"
```

### Recovery Procedure
```bash
# Restore from backup
gunzip social_media_20241201_120000.sql.gz
psql -h localhost -U app_user -d social_media < social_media_20241201_120000.sql
```

## Performance Optimization

### Query Optimization Tips
1. **Use EXPLAIN ANALYZE** to understand query execution plans
2. **Add appropriate indexes** for frequently queried columns
3. **Use LIMIT and OFFSET** for pagination
4. **Avoid N+1 queries** by using JOINs or batch loading
5. **Use connection pooling** to manage database connections efficiently

### Scaling Considerations
1. **Read Replicas**: For read-heavy workloads
2. **Partitioning**: For large tables (posts table by date)
3. **Archiving**: Move old data to separate tables
4. **Caching**: Cache frequently accessed data in Redis
5. **Database Sharding**: For extreme scale (future consideration)

This database design provides a solid foundation for the social media platform while maintaining simplicity appropriate for an SDE 1 level interview. The schema is normalized, includes proper constraints and indexes, and can handle the expected scale efficiently.