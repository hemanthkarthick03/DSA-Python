# Interview Discussion Guide - Social Media Platform (SDE 1 Level)

## Complete Interview Walkthrough

### Phase 1: Requirements Gathering (10-15 minutes)

#### Interviewer Opening
**"Design a social media platform similar to Instagram that allows users to share photos, follow other users, and view a personalized feed."**

#### Expected Candidate Response Process

**Step 1: Clarifying Questions**
```
Candidate should ask:
✅ "What are the core features we need to support?"
✅ "How many users are we expecting to handle?"
✅ "What types of content - just photos or videos too?"
✅ "Do we need real-time features like live updates?"
✅ "Any specific technology constraints or preferences?"
✅ "What are the performance requirements?"
```

**Step 2: Requirements Summary**
```
Candidate should summarize:
✅ Core features: User profiles, photo sharing, following, feed, likes, comments
✅ Scale: 10M total users, 1M DAU, 1M posts/day
✅ Performance: <2s feed loading, <1s interactions
✅ Content: Photos only (2MB average size)
✅ Read/Write ratio: 10:1 (read-heavy)
```

#### Interviewer Evaluation Criteria
- [ ] **Asks relevant clarifying questions** (not just technical details)
- [ ] **Focuses on user needs first** (customer obsession)
- [ ] **Considers scale appropriately** (not over-engineering for SDE 1)
- [ ] **Summarizes requirements clearly** (communication skills)

---

### Phase 2: High-Level Architecture (15-20 minutes)

#### Expected Architecture Components

**Step 1: Basic System Diagram**
```
Candidate should draw:
┌─────────────┐    ┌─────────────┐
│   Clients   │    │   Clients   │
│(Mobile/Web) │    │(Mobile/Web) │
└─────────────┘    └─────────────┘
        │                   │
        └───────────┬───────┘
                    │
            ┌───────────────┐
            │Load Balancer  │
            └───────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
 ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
 │App Server 1 │ │App Server 2 │ │App Server 3 │
 └─────────────┘ └─────────────┘ └─────────────┘
        │           │           │
        └───────────┼───────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
┌─────────┐  ┌─────────────┐  ┌─────────┐
│Database │  │    Cache    │  │File     │
│(Primary)│  │   (Redis)   │  │Storage  │
└─────────┘  └─────────────┘  │  (S3)   │
    │                         └─────────┘
┌─────────┐
│Database │
│(Replica)│
└─────────┘
```

**Step 2: Component Explanation**
```
Candidate should explain:
✅ Load Balancer: Distributes traffic, handles SSL
✅ App Servers: Business logic, stateless design
✅ Database: PostgreSQL for structured data
✅ Cache: Redis for frequently accessed data
✅ File Storage: S3 for photos with CDN
✅ Read Replica: Handle read-heavy operations
```

#### Common Interview Questions & Expected Answers

**Q: "Why did you choose PostgreSQL over NoSQL?"**
```
Expected Answer:
✅ "For SDE 1 level, SQL provides ACID guarantees and strong consistency"
✅ "Our data has clear relationships (users, posts, follows)"
✅ "Team familiarity and easier debugging"
✅ "Can scale with read replicas for our current needs"
✅ "Would consider NoSQL for specific use cases as we grow"
```

**Q: "How would you handle photo storage?"**
```
Expected Answer:
✅ "Store photos in S3 for durability and scalability"
✅ "Generate multiple sizes (thumbnail, medium, large)"
✅ "Use CloudFront CDN for fast global delivery"
✅ "Store metadata (URLs, sizes) in database"
✅ "Implement lifecycle policies for cost optimization"
```

**Q: "What about caching strategy?"**
```
Expected Answer:
✅ "Cache user profiles (1 hour TTL)"
✅ "Cache popular posts and feeds (30 min TTL)"
✅ "Cache-aside pattern for most data"
✅ "Write-through for like counts"
✅ "Redis cluster for high availability"
```

#### Interviewer Evaluation Criteria
- [ ] **Draws clear, logical architecture** (technical understanding)
- [ ] **Explains component choices** (reasoning ability)
- [ ] **Considers basic scalability** (appropriate for level)
- [ ] **Shows understanding of trade-offs** (system thinking)

---

### Phase 3: Database Design (10-12 minutes)

#### Expected Database Schema

**Step 1: Core Tables**
```sql
Candidate should design:

Users Table:
- user_id (PK)
- username (unique)
- email (unique)
- password_hash
- full_name
- bio
- profile_picture_url
- created_at

Posts Table:
- post_id (PK)
- user_id (FK)
- photo_url
- caption
- like_count
- comment_count
- created_at

Follows Table:
- follower_id (FK)
- following_id (FK)
- created_at
- PK (follower_id, following_id)

Likes Table:
- user_id (FK)
- post_id (FK)
- created_at
- PK (user_id, post_id)
```

**Step 2: Relationships**
```
Candidate should explain:
✅ Users 1:N Posts (one user has many posts)
✅ Users M:N Users (many-to-many follows)
✅ Users M:N Posts (many-to-many likes)
✅ Proper foreign key constraints
✅ Composite primary keys where appropriate
```

#### Common Interview Questions & Expected Answers

**Q: "How would you generate the user feed?"**
```
Expected Answer:
✅ "Query follows table to get users I follow"
✅ "Get recent posts from those users"
✅ "Order by created_at DESC"
✅ "Use pagination with LIMIT/OFFSET"
✅ "Cache results for active users"

SQL Example:
SELECT p.*, u.username, u.profile_picture_url
FROM posts p
JOIN users u ON p.user_id = u.user_id
WHERE p.user_id IN (
    SELECT following_id 
    FROM follows 
    WHERE follower_id = ?
)
ORDER BY p.created_at DESC
LIMIT 20 OFFSET 0;
```

**Q: "What indexes would you add?"**
```
Expected Answer:
✅ "Index on posts(user_id, created_at) for user timelines"
✅ "Index on follows(follower_id) for feed generation"
✅ "Index on likes(post_id) for like counts"
✅ "Unique indexes on username and email"
✅ "Consider composite indexes for common queries"
```

**Q: "How would you handle like counts?"**
```
Expected Answer:
✅ "Store denormalized like_count in posts table"
✅ "Update via database triggers or application logic"
✅ "Cache frequently accessed counts"
✅ "Consider eventual consistency for better performance"
✅ "Batch updates for high-traffic posts"
```

#### Interviewer Evaluation Criteria
- [ ] **Designs normalized schema** (database fundamentals)
- [ ] **Identifies key relationships** (data modeling)
- [ ] **Considers indexing strategy** (performance awareness)
- [ ] **Handles denormalization appropriately** (trade-off understanding)

---

### Phase 4: API Design (5-8 minutes)

#### Expected API Endpoints

**Step 1: Core APIs**
```
Candidate should identify:

Authentication:
✅ POST /api/v1/auth/register
✅ POST /api/v1/auth/login
✅ POST /api/v1/auth/logout

User Management:
✅ GET /api/v1/users/{id}
✅ PUT /api/v1/users/{id}
✅ GET /api/v1/users/search

Posts:
✅ POST /api/v1/posts
✅ GET /api/v1/posts/{id}
✅ GET /api/v1/users/{id}/posts

Social:
✅ POST /api/v1/users/{id}/follow
✅ DELETE /api/v1/users/{id}/follow
✅ POST /api/v1/posts/{id}/like
✅ DELETE /api/v1/posts/{id}/like

Feed:
✅ GET /api/v1/feed
```

**Step 2: Request/Response Format**
```json
Candidate should show understanding:

POST /api/v1/posts
{
  "caption": "Beautiful sunset!",
  "photo": "base64_or_multipart"
}

Response:
{
  "success": true,
  "data": {
    "postId": 123,
    "photoUrl": "https://cdn.example.com/photo.jpg",
    "caption": "Beautiful sunset!",
    "likeCount": 0,
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

#### Common Interview Questions & Expected Answers

**Q: "How would you handle authentication?"**
```
Expected Answer:
✅ "JWT tokens for stateless authentication"
✅ "Store tokens in HTTP-only cookies or Authorization header"
✅ "Token expiration and refresh mechanism"
✅ "Password hashing with bcrypt"
✅ "Rate limiting for login attempts"
```

**Q: "What about file uploads?"**
```
Expected Answer:
✅ "Multipart form data for photo uploads"
✅ "Validate file type and size on server"
✅ "Upload directly to S3 with pre-signed URLs"
✅ "Generate thumbnails asynchronously"
✅ "Return photo URLs in response"
```

#### Interviewer Evaluation Criteria
- [ ] **Designs RESTful APIs** (API design principles)
- [ ] **Considers authentication** (security awareness)
- [ ] **Handles file uploads appropriately** (practical understanding)
- [ ] **Shows consistent response format** (API design consistency)

---

### Phase 5: Scaling Discussion (5-10 minutes)

#### Expected Scaling Solutions

**Step 1: Immediate Bottlenecks**
```
Candidate should identify:
✅ Database becomes bottleneck with more users
✅ Photo storage and delivery costs increase
✅ Feed generation becomes slow
✅ Cache hit ratio decreases
✅ Single points of failure
```

**Step 2: Scaling Solutions**
```
Candidate should propose:

Database Scaling:
✅ Add more read replicas
✅ Implement connection pooling
✅ Optimize queries and add indexes
✅ Consider database partitioning

Application Scaling:
✅ Add more app servers
✅ Implement auto-scaling
✅ Use container orchestration
✅ Optimize application code

Caching:
✅ Implement Redis cluster
✅ Add application-level caching
✅ Use CDN for static content
✅ Cache feed data more aggressively

Storage:
✅ Use S3 with CloudFront CDN
✅ Implement image compression
✅ Use multiple storage classes
✅ Implement lifecycle policies
```

#### Common Interview Questions & Expected Answers

**Q: "What if a celebrity user posts and has millions of followers?"**
```
Expected Answer (SDE 1 Level):
✅ "This is the 'celebrity problem' in social media"
✅ "Pre-computing feeds won't work for millions of followers"
✅ "Use pull model for celebrity posts (generate on demand)"
✅ "Cache celebrity posts more aggressively"
✅ "Consider async processing for feed updates"
✅ "May need to rethink architecture for this scale"
```

**Q: "How would you monitor the system?"**
```
Expected Answer:
✅ "Monitor API response times and error rates"
✅ "Track database query performance"
✅ "Monitor cache hit ratios"
✅ "Set up alerts for system health"
✅ "Log important business metrics (posts, likes, follows)"
✅ "Use tools like CloudWatch, Grafana, or similar"
```

**Q: "What about data consistency?"**
```
Expected Answer:
✅ "Strong consistency for user data and authentication"
✅ "Eventual consistency acceptable for likes and follows"
✅ "Use database transactions for critical operations"
✅ "Consider message queues for async operations"
✅ "Implement retry mechanisms for failed operations"
```

#### Interviewer Evaluation Criteria
- [ ] **Identifies realistic bottlenecks** (system understanding)
- [ ] **Proposes appropriate solutions** (scaling knowledge)
- [ ] **Considers trade-offs** (engineering judgment)
- [ ] **Shows awareness of complexity** (appropriate for SDE 1)

---

## Amazon Leadership Principles Integration

### Customer Obsession
**How to demonstrate:**
- Start design with user experience considerations
- Prioritize fast loading times and reliable uploads
- Consider mobile-first design
- Plan for accessibility features
- Focus on core user needs before advanced features

**Example responses:**
- "Users expect their photos to upload quickly, so we'll optimize the upload process"
- "Feed loading should be under 2 seconds for good user experience"
- "We should handle network failures gracefully for mobile users"

### Ownership
**How to demonstrate:**
- Think about operational aspects (monitoring, logging)
- Consider error handling and recovery
- Plan for maintenance and updates
- Think about the full user journey
- Consider long-term sustainability

**Example responses:**
- "We need proper logging to debug issues quickly"
- "Let's add health check endpoints for monitoring"
- "We should plan for database backups and recovery"

### Invent and Simplify
**How to demonstrate:**
- Start with simple solutions
- Avoid over-engineering
- Question complex requirements
- Focus on MVP first
- Choose proven technologies

**Example responses:**
- "Let's start with a monolithic architecture for simplicity"
- "We can use PostgreSQL instead of multiple databases initially"
- "Simple chronological feed ordering is good enough to start"

### Bias for Action
**How to demonstrate:**
- Make reasonable assumptions to move forward
- Propose MVP approach
- Plan for iterative improvements
- Don't get stuck on perfect solutions
- Show willingness to adapt

**Example responses:**
- "Let's assume users primarily use mobile and optimize for that"
- "We can start with basic features and add advanced ones later"
- "I'll design for the stated requirements and we can adjust as needed"

---

## Common Mistakes and How to Avoid Them

### Technical Mistakes

**❌ Over-Engineering**
```
Mistake: Starting with microservices, complex caching, sharding
Better: Monolithic app, simple caching, single database with replicas
```

**❌ Under-Engineering**
```
Mistake: Single server, no caching, no consideration for scale
Better: Load balancer, basic caching, read replicas
```

**❌ Wrong Technology Choices**
```
Mistake: NoSQL for everything, complex message queues
Better: SQL for structured data, simple async processing
```

### Communication Mistakes

**❌ Not Asking Questions**
```
Mistake: Jumping into design without clarification
Better: Ask about scale, features, constraints, priorities
```

**❌ Silent Thinking**
```
Mistake: Drawing diagrams without explanation
Better: Explain reasoning for each component and choice
```

**❌ Getting Stuck**
```
Mistake: Spending too much time on one component
Better: Move forward, note areas to revisit if time permits
```

### Process Mistakes

**❌ Poor Time Management**
```
Mistake: Spending 30 minutes on database design
Better: Allocate time appropriately across all phases
```

**❌ Ignoring Requirements**
```
Mistake: Designing for different scale or features
Better: Stick to stated requirements, note assumptions
```

---

## Success Indicators

### Technical Competency
- [ ] Designs working system architecture
- [ ] Shows understanding of basic scalability
- [ ] Makes reasonable technology choices
- [ ] Considers data consistency and performance
- [ ] Identifies obvious bottlenecks

### Communication Skills
- [ ] Asks clarifying questions
- [ ] Explains reasoning clearly
- [ ] Manages time appropriately
- [ ] Handles feedback well
- [ ] Shows structured thinking

### Amazon Culture Fit
- [ ] Demonstrates customer focus
- [ ] Shows ownership thinking
- [ ] Keeps solutions simple
- [ ] Shows bias for action
- [ ] Learns from feedback

### Problem-Solving Approach
- [ ] Breaks down complex problem
- [ ] Builds solution incrementally
- [ ] Considers trade-offs
- [ ] Adapts to new information
- [ ] Shows engineering judgment

---

## Follow-up Questions for Deeper Assessment

### If Candidate Finishes Early
1. "How would you implement the recommendation algorithm for the feed?"
2. "What if we wanted to add video support?"
3. "How would you handle content moderation?"
4. "What about implementing direct messaging?"
5. "How would you design the mobile app architecture?"

### If Candidate Struggles
1. "Let's focus on just the core user registration and login flow"
2. "What's the simplest way to store user posts?"
3. "How would you show a user their own posts?"
4. "What database tables would you need for basic functionality?"

### For Strong Candidates
1. "How would you handle eventual consistency in the system?"
2. "What's your strategy for database migrations?"
3. "How would you implement A/B testing for new features?"
4. "What about implementing real-time notifications?"
5. "How would you design for multiple regions?"

---

## Interviewer Notes Template

```
Candidate: _______________
Date: _______________
Position: SDE 1

Requirements Gathering (10-15 min):
□ Asked clarifying questions
□ Understood scale requirements
□ Focused on user needs
□ Summarized requirements clearly
Score: ___/10

High-Level Design (15-20 min):
□ Drew clear architecture diagram
□ Explained component choices
□ Considered basic scalability
□ Showed system thinking
Score: ___/10

Database Design (10-12 min):
□ Designed appropriate schema
□ Identified key relationships
□ Considered indexing
□ Handled denormalization
Score: ___/10

API Design (5-8 min):
□ Designed RESTful APIs
□ Considered authentication
□ Handled file uploads
□ Consistent response format
Score: ___/10

Scaling Discussion (5-10 min):
□ Identified bottlenecks
□ Proposed scaling solutions
□ Considered trade-offs
□ Appropriate complexity
Score: ___/10

Communication:
□ Clear explanations
□ Good time management
□ Handled feedback well
□ Structured approach
Score: ___/10

Leadership Principles:
□ Customer obsession
□ Ownership thinking
□ Simplicity focus
□ Bias for action
Score: ___/10

Overall Recommendation:
□ Strong Hire
□ Hire
□ No Hire
□ Strong No Hire

Comments:
_________________________________
_________________________________
```

This interview guide provides a comprehensive framework for conducting and evaluating social media system design interviews at the SDE 1 level, ensuring consistency and fairness while testing the appropriate depth of knowledge for the role.