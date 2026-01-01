# System Design Round Examples & FAQs for Amazon Interviews

A comprehensive collection of real system design interview examples, frequently asked questions, and important topics with detailed solutions.

---

## Table of Contents
1. [System Design Round Structure](#system-design-round-structure)
2. [Complete Interview Examples](#complete-interview-examples)
3. [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs)
4. [Important Topics & Patterns](#important-topics--patterns)
5. [Amazon-Specific Examples](#amazon-specific-examples)
6. [Common Follow-up Questions](#common-follow-up-questions)
7. [Evaluation Criteria](#evaluation-criteria)

---

## System Design Round Structure

### Typical 45-60 Minute Interview Flow
```
Phase 1: Requirements Gathering (10-15 min)
├── Clarifying questions
├── Functional requirements
├── Non-functional requirements
└── Scale estimation

Phase 2: High-Level Design (15-20 min)
├── System architecture
├── Major components
├── Data flow
└── Technology choices

Phase 3: Detailed Design (15-20 min)
├── Database schema
├── API design
├── Critical algorithms
└── Component deep-dive

Phase 4: Scale & Optimize (10-15 min)
├── Bottleneck identification
├── Scaling strategies
├── Trade-off discussions
└── Monitoring & reliability
```

---

## Complete Interview Examples

### Example 1: Design a URL Shortener (like bit.ly)

#### Phase 1: Requirements Gathering (12 minutes)

**Interviewer**: "Design a URL shortener service like bit.ly"

**Candidate Response**:
"Let me ask some clarifying questions to better understand the requirements:

1. **Scale**: How many URLs do we expect to shorten per day?
2. **Features**: Do we need analytics, custom aliases, expiration?
3. **Users**: Is this for general public or internal use?
4. **Performance**: What's the expected read/write ratio?
5. **Reliability**: What's the uptime requirement?"

**Interviewer Answers**:
- 100M URLs shortened per day
- Basic analytics (click count), no custom aliases initially
- Public service like bit.ly
- Read/write ratio is 100:1 (heavy read)
- 99.9% uptime required

**Requirements Summary**:
```
Functional Requirements:
✓ Shorten long URLs to short URLs
✓ Redirect short URLs to original URLs
✓ Basic analytics (click tracking)
✓ URL expiration (default 1 year)

Non-Functional Requirements:
✓ 100M URLs/day = 1,157 URLs/second
✓ 10B redirects/day = 115,740 redirects/second
✓ 99.9% availability
✓ <100ms redirect latency
✓ 5 years of data retention

Scale Estimation:
✓ Storage: 100M URLs/day × 500 bytes × 365 days = 18.25 TB/year
✓ Bandwidth: 115,740 QPS peak traffic
✓ Cache: 20% of URLs generate 80% of traffic
```

#### Phase 2: High-Level Design (18 minutes)

**System Architecture**:
```
[Client] → [Load Balancer] → [API Gateway] → [URL Service]
                                                    ↓
[Cache Layer (Redis)] ← [Database (Cassandra)] ← [Analytics Service]
                                                    ↓
                                            [Message Queue]
```

**Component Explanation**:
"Let me walk through the high-level architecture:

1. **Load Balancer**: Distributes traffic across multiple servers
2. **API Gateway**: Handles rate limiting, authentication, routing
3. **URL Service**: Core business logic for shortening and redirecting
4. **Database**: Stores URL mappings (Cassandra for high write throughput)
5. **Cache**: Redis for frequently accessed URLs
6. **Analytics Service**: Tracks clicks asynchronously
7. **Message Queue**: Decouples analytics from main flow"

**Data Flow**:
```
URL Shortening Flow:
1. User submits long URL
2. Generate unique short code
3. Store mapping in database
4. Return short URL

URL Redirect Flow:
1. User clicks short URL
2. Check cache for mapping
3. If not in cache, query database
4. Redirect to original URL
5. Async: Send click event to analytics
```

#### Phase 3: Detailed Design (15 minutes)

**Database Schema**:
```sql
-- URL mappings table (Cassandra)
CREATE TABLE url_mappings (
    short_code TEXT PRIMARY KEY,
    original_url TEXT,
    user_id BIGINT,
    created_at TIMESTAMP,
    expires_at TIMESTAMP,
    is_active BOOLEAN
);

-- Analytics table
CREATE TABLE url_analytics (
    short_code TEXT,
    click_timestamp TIMESTAMP,
    user_ip TEXT,
    user_agent TEXT,
    referrer TEXT,
    PRIMARY KEY (short_code, click_timestamp)
);
```

**Short Code Generation Algorithm**:
```python
import hashlib
import base62

class URLShortener:
    def __init__(self):
        self.counter = 0
        self.base_url = "https://short.ly/"
    
    def generate_short_code(self, original_url, user_id):
        # Method 1: Hash-based (can have collisions)
        hash_input = f"{original_url}{user_id}{time.time()}"
        hash_value = hashlib.md5(hash_input.encode()).hexdigest()
        return base62.encode(int(hash_value[:8], 16))[:7]
    
    def generate_short_code_counter(self):
        # Method 2: Counter-based (guaranteed unique)
        self.counter += 1
        return base62.encode(self.counter)
    
    def shorten_url(self, original_url, user_id=None):
        short_code = self.generate_short_code(original_url, user_id)
        
        # Check for collision and retry if needed
        while self.code_exists(short_code):
            short_code = self.generate_short_code(original_url, user_id)
        
        # Store in database
        self.store_mapping(short_code, original_url, user_id)
        
        return f"{self.base_url}{short_code}"
```

**API Design**:
```http
# Shorten URL
POST /api/v1/shorten
Content-Type: application/json
{
  "url": "https://example.com/very/long/url",
  "user_id": 12345,
  "expires_in": 31536000  // 1 year in seconds
}

Response:
{
  "short_url": "https://short.ly/abc123",
  "short_code": "abc123",
  "expires_at": "2025-01-01T00:00:00Z"
}

# Redirect (handled by web server)
GET /abc123
Response: 302 Redirect to original URL

# Analytics
GET /api/v1/analytics/abc123
Response:
{
  "short_code": "abc123",
  "total_clicks": 1547,
  "clicks_today": 23,
  "top_referrers": ["google.com", "facebook.com"],
  "click_history": [...]
}
```