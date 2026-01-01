# Social Media System Design - Amazon SDE 1 Interview

## Problem Statement

**Interviewer**: "Design a simplified social media platform similar to Instagram that allows users to share photos, follow other users, and view a personalized feed. Focus on the core functionality and basic scalability considerations appropriate for an SDE 1 level."

---

## Interview Context

### Role: Amazon SDE 1 (0-2 years experience)
### Duration: 45 minutes
### Focus Areas:
- Basic system design principles
- Simple database design
- API design fundamentals
- Basic caching concepts
- Understanding of load balancing
- Simple scaling strategies

### What Amazon Expects from SDE 1:
- Clear thinking process
- Basic understanding of system components
- Ability to design simple, working solutions
- Understanding of trade-offs at a basic level
- Good communication skills
- Customer-focused approach

---

## Simplified Requirements (SDE 1 Level)

### Core Features to Design:
1. **User Management**
   - User registration and login
   - Basic user profiles
   - Profile pictures

2. **Photo Sharing**
   - Upload photos with captions
   - View individual posts
   - Basic photo storage

3. **Social Features**
   - Follow/unfollow other users
   - Like posts
   - Basic commenting

4. **Feed Generation**
   - Simple timeline of followed users' posts
   - Chronological ordering

### Scale Expectations (Simplified):
- **Users**: 10 million total users
- **Daily Active Users**: 1 million
- **Posts per day**: 1 million
- **Photos**: Average 2MB per photo
- **Read/Write Ratio**: 10:1 (read-heavy)

### Performance Requirements:
- **Feed loading**: < 2 seconds
- **Photo upload**: < 5 seconds
- **Basic interactions**: < 1 second
- **Availability**: 99% (not 99.99% like senior roles)

---

## Interview Flow Structure

### Phase 1: Requirements Clarification (10 minutes)
**Expected Questions from Candidate:**
- What are the main features we need to support?
- How many users are we expecting?
- What types of content (just photos or videos too)?
- Do we need real-time features?
- Any specific technology preferences?

### Phase 2: High-Level Design (15 minutes)
**Expected Components:**
- Web/Mobile clients
- Load balancer
- Application servers
- Database
- File storage for photos
- Basic caching

### Phase 3: Database Design (10 minutes)
**Expected Tables:**
- Users table
- Posts table
- Follows table
- Likes table
- Comments table (if time permits)

### Phase 4: API Design (5 minutes)
**Basic APIs:**
- User registration/login
- Create post
- Get user feed
- Follow/unfollow user
- Like/unlike post

### Phase 5: Basic Scaling Discussion (5 minutes)
**Simple Scaling Concepts:**
- Database read replicas
- CDN for photos
- Basic caching strategies
- Load balancing

---

## Success Criteria for SDE 1

### Technical Understanding:
- [ ] Can identify main system components
- [ ] Understands basic database relationships
- [ ] Can design simple REST APIs
- [ ] Knows when to use caching
- [ ] Understands load balancing concept

### Communication:
- [ ] Asks clarifying questions
- [ ] Explains thinking process clearly
- [ ] Can discuss basic trade-offs
- [ ] Shows customer focus
- [ ] Manages time reasonably well

### Problem-Solving:
- [ ] Starts with simple solution
- [ ] Builds incrementally
- [ ] Identifies obvious bottlenecks
- [ ] Suggests reasonable solutions
- [ ] Shows learning mindset

---

## Common Mistakes to Avoid (SDE 1 Level)

### Over-Engineering:
- ❌ Starting with microservices
- ❌ Complex caching strategies
- ❌ Advanced database sharding
- ❌ Multiple programming languages

### Under-Engineering:
- ❌ Single server for everything
- ❌ No consideration for file storage
- ❌ Ignoring basic performance
- ❌ No thought about scaling

### Communication Issues:
- ❌ Not asking clarifying questions
- ❌ Jumping to implementation details
- ❌ Not explaining reasoning
- ❌ Getting stuck on one component

---

## Amazon Leadership Principles (SDE 1 Focus)

### Customer Obsession:
- Start with user needs
- Simple, intuitive design
- Fast loading times
- Reliable photo uploads

### Ownership:
- Think about the full user journey
- Consider basic error handling
- Plan for simple monitoring

### Invent and Simplify:
- Keep the design simple
- Avoid unnecessary complexity
- Focus on core features first

### Bias for Action:
- Start with MVP approach
- Plan for iterative improvements
- Make reasonable assumptions to move forward

---

## Next Steps

1. **Requirements Analysis** - Detailed functional and non-functional requirements
2. **System Architecture** - High-level component design
3. **Database Design** - Schema and relationships
4. **API Design** - RESTful endpoints
5. **Basic Implementation** - Core service logic
6. **Scaling Strategy** - Simple performance improvements

This problem is designed to test fundamental system design skills while keeping complexity appropriate for an entry-level role at Amazon.