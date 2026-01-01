# API Design - Social Media Platform (SDE 1 Level)

## API Overview

### Base URL
```
Production: https://api.socialmedia.com/v1
Development: http://localhost:8080/api/v1
```

### Authentication
```
Type: JWT Bearer Token
Header: Authorization: Bearer <token>
Token Expiry: 24 hours
Refresh Token: 7 days
```

### Response Format
```json
{
  "success": true,
  "data": {},
  "message": "Operation completed successfully",
  "timestamp": "2024-01-15T10:30:00Z",
  "errors": []
}
```

### Error Response Format
```json
{
  "success": false,
  "data": null,
  "message": "Validation failed",
  "timestamp": "2024-01-15T10:30:00Z",
  "errors": [
    {
      "field": "email",
      "message": "Email format is invalid"
    }
  ]
}
```

## Authentication APIs

### 1. User Registration
```http
POST /api/v1/auth/register
Content-Type: application/json

Request Body:
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "fullName": "John Doe"
}

Response (201 Created):
{
  "success": true,
  "data": {
    "userId": 123,
    "username": "john_doe",
    "email": "john@example.com",
    "fullName": "John Doe",
    "profilePictureUrl": null,
    "bio": null,
    "isVerified": false,
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "message": "User registered successfully"
}

Error Responses:
400 Bad Request - Validation errors
409 Conflict - Username or email already exists
```

### 2. User Login
```http
POST /api/v1/auth/login
Content-Type: application/json

Request Body:
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}

Response (200 OK):
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "tokenType": "Bearer",
    "expiresIn": 86400,
    "user": {
      "userId": 123,
      "username": "john_doe",
      "email": "john@example.com",
      "fullName": "John Doe",
      "profilePictureUrl": null,
      "bio": null,
      "isVerified": false
    }
  },
  "message": "Login successful"
}

Error Responses:
400 Bad Request - Invalid credentials
401 Unauthorized - Account locked or inactive
```

### 3. Refresh Token
```http
POST /api/v1/auth/refresh
Content-Type: application/json

Request Body:
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Response (200 OK):
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "tokenType": "Bearer",
    "expiresIn": 86400
  },
  "message": "Token refreshed successfully"
}
```

### 4. Logout
```http
POST /api/v1/auth/logout
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": null,
  "message": "Logged out successfully"
}
```

## User Management APIs

### 1. Get User Profile
```http
GET /api/v1/users/{userId}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "userId": 123,
    "username": "john_doe",
    "fullName": "John Doe",
    "bio": "Photography enthusiast and coffee lover",
    "profilePictureUrl": "https://cdn.example.com/profiles/123.jpg",
    "isVerified": false,
    "postCount": 25,
    "followerCount": 150,
    "followingCount": 75,
    "isFollowedByCurrentUser": false,
    "createdAt": "2024-01-15T10:30:00Z"
  }
}

Error Responses:
404 Not Found - User not found
403 Forbidden - Private profile
```

### 2. Update User Profile
```http
PUT /api/v1/users/{userId}
Authorization: Bearer <token>
Content-Type: application/json

Request Body:
{
  "fullName": "John Smith",
  "bio": "Updated bio text",
  "profilePictureUrl": "https://cdn.example.com/profiles/123_new.jpg"
}

Response (200 OK):
{
  "success": true,
  "data": {
    "userId": 123,
    "username": "john_doe",
    "fullName": "John Smith",
    "bio": "Updated bio text",
    "profilePictureUrl": "https://cdn.example.com/profiles/123_new.jpg",
    "isVerified": false,
    "updatedAt": "2024-01-15T11:30:00Z"
  },
  "message": "Profile updated successfully"
}

Error Responses:
400 Bad Request - Validation errors
403 Forbidden - Cannot update other user's profile
```

### 3. Search Users
```http
GET /api/v1/users/search?q={query}&limit={limit}&offset={offset}
Authorization: Bearer <token>

Parameters:
- q: Search query (username or full name)
- limit: Number of results (default: 20, max: 50)
- offset: Pagination offset (default: 0)

Response (200 OK):
{
  "success": true,
  "data": {
    "users": [
      {
        "userId": 123,
        "username": "john_doe",
        "fullName": "John Doe",
        "profilePictureUrl": "https://cdn.example.com/profiles/123.jpg",
        "isVerified": false,
        "isFollowedByCurrentUser": false
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 1,
      "hasMore": false
    }
  }
}
```

## Post Management APIs

### 1. Create Post
```http
POST /api/v1/posts
Authorization: Bearer <token>
Content-Type: multipart/form-data

Form Data:
- photo: [image file] (required)
- caption: "Beautiful sunset today! #sunset #photography" (optional)

Response (201 Created):
{
  "success": true,
  "data": {
    "postId": 456,
    "userId": 123,
    "username": "john_doe",
    "userProfilePicture": "https://cdn.example.com/profiles/123.jpg",
    "photoUrl": "https://cdn.example.com/posts/456/photo.jpg",
    "thumbnailUrl": "https://cdn.example.com/posts/456/thumb.jpg",
    "caption": "Beautiful sunset today! #sunset #photography",
    "likeCount": 0,
    "commentCount": 0,
    "isLikedByCurrentUser": false,
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "message": "Post created successfully"
}

Error Responses:
400 Bad Request - Invalid file format or size
413 Payload Too Large - File size exceeds limit
```

### 2. Get Post Details
```http
GET /api/v1/posts/{postId}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "postId": 456,
    "userId": 123,
    "username": "john_doe",
    "userFullName": "John Doe",
    "userProfilePicture": "https://cdn.example.com/profiles/123.jpg",
    "isUserVerified": false,
    "photoUrl": "https://cdn.example.com/posts/456/photo.jpg",
    "thumbnailUrl": "https://cdn.example.com/posts/456/thumb.jpg",
    "caption": "Beautiful sunset today! #sunset #photography",
    "likeCount": 25,
    "commentCount": 5,
    "isLikedByCurrentUser": true,
    "createdAt": "2024-01-15T10:30:00Z"
  }
}

Error Responses:
404 Not Found - Post not found or deleted
```

### 3. Get User Posts
```http
GET /api/v1/users/{userId}/posts?limit={limit}&offset={offset}
Authorization: Bearer <token>

Parameters:
- limit: Number of posts (default: 20, max: 50)
- offset: Pagination offset (default: 0)

Response (200 OK):
{
  "success": true,
  "data": {
    "posts": [
      {
        "postId": 456,
        "photoUrl": "https://cdn.example.com/posts/456/photo.jpg",
        "thumbnailUrl": "https://cdn.example.com/posts/456/thumb.jpg",
        "caption": "Beautiful sunset today!",
        "likeCount": 25,
        "commentCount": 5,
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 25,
      "hasMore": true
    }
  }
}
```

### 4. Delete Post
```http
DELETE /api/v1/posts/{postId}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": null,
  "message": "Post deleted successfully"
}

Error Responses:
404 Not Found - Post not found
403 Forbidden - Cannot delete other user's post
```

## Social Interaction APIs

### 1. Like Post
```http
POST /api/v1/posts/{postId}/like
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "postId": 456,
    "likeCount": 26,
    "isLikedByCurrentUser": true
  },
  "message": "Post liked successfully"
}

Error Responses:
404 Not Found - Post not found
409 Conflict - Post already liked
```

### 2. Unlike Post
```http
DELETE /api/v1/posts/{postId}/like
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "postId": 456,
    "likeCount": 25,
    "isLikedByCurrentUser": false
  },
  "message": "Post unliked successfully"
}

Error Responses:
404 Not Found - Post not found or not liked
```

### 3. Get Post Likes
```http
GET /api/v1/posts/{postId}/likes?limit={limit}&offset={offset}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "likes": [
      {
        "userId": 789,
        "username": "jane_smith",
        "fullName": "Jane Smith",
        "profilePictureUrl": "https://cdn.example.com/profiles/789.jpg",
        "isVerified": false,
        "likedAt": "2024-01-15T11:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 25,
      "hasMore": true
    }
  }
}
```

## Comment APIs

### 1. Add Comment
```http
POST /api/v1/posts/{postId}/comments
Authorization: Bearer <token>
Content-Type: application/json

Request Body:
{
  "content": "Great photo! Love the colors."
}

Response (201 Created):
{
  "success": true,
  "data": {
    "commentId": 789,
    "postId": 456,
    "userId": 123,
    "username": "john_doe",
    "userProfilePicture": "https://cdn.example.com/profiles/123.jpg",
    "content": "Great photo! Love the colors.",
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "message": "Comment added successfully"
}

Error Responses:
400 Bad Request - Empty or invalid content
404 Not Found - Post not found
```

### 2. Get Post Comments
```http
GET /api/v1/posts/{postId}/comments?limit={limit}&offset={offset}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "comments": [
      {
        "commentId": 789,
        "userId": 123,
        "username": "john_doe",
        "userFullName": "John Doe",
        "userProfilePicture": "https://cdn.example.com/profiles/123.jpg",
        "content": "Great photo! Love the colors.",
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 5,
      "hasMore": false
    }
  }
}
```

### 3. Delete Comment
```http
DELETE /api/v1/comments/{commentId}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": null,
  "message": "Comment deleted successfully"
}

Error Responses:
404 Not Found - Comment not found
403 Forbidden - Cannot delete other user's comment
```

## Social Graph APIs

### 1. Follow User
```http
POST /api/v1/users/{userId}/follow
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "userId": 456,
    "isFollowing": true,
    "followerCount": 151
  },
  "message": "User followed successfully"
}

Error Responses:
404 Not Found - User not found
409 Conflict - Already following user
400 Bad Request - Cannot follow yourself
```

### 2. Unfollow User
```http
DELETE /api/v1/users/{userId}/follow
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "userId": 456,
    "isFollowing": false,
    "followerCount": 150
  },
  "message": "User unfollowed successfully"
}

Error Responses:
404 Not Found - User not found or not following
```

### 3. Get User Followers
```http
GET /api/v1/users/{userId}/followers?limit={limit}&offset={offset}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "followers": [
      {
        "userId": 789,
        "username": "jane_smith",
        "fullName": "Jane Smith",
        "profilePictureUrl": "https://cdn.example.com/profiles/789.jpg",
        "isVerified": false,
        "isFollowedByCurrentUser": true,
        "followedAt": "2024-01-10T10:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 150,
      "hasMore": true
    }
  }
}
```

### 4. Get User Following
```http
GET /api/v1/users/{userId}/following?limit={limit}&offset={offset}
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": {
    "following": [
      {
        "userId": 456,
        "username": "mike_wilson",
        "fullName": "Mike Wilson",
        "profilePictureUrl": "https://cdn.example.com/profiles/456.jpg",
        "isVerified": true,
        "followedAt": "2024-01-12T10:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total": 75,
      "hasMore": true
    }
  }
}
```

## Feed APIs

### 1. Get User Feed
```http
GET /api/v1/feed?limit={limit}&offset={offset}
Authorization: Bearer <token>

Parameters:
- limit: Number of posts (default: 20, max: 50)
- offset: Pagination offset (default: 0)

Response (200 OK):
{
  "success": true,
  "data": {
    "posts": [
      {
        "postId": 456,
        "userId": 123,
        "username": "john_doe",
        "userFullName": "John Doe",
        "userProfilePicture": "https://cdn.example.com/profiles/123.jpg",
        "isUserVerified": false,
        "photoUrl": "https://cdn.example.com/posts/456/photo.jpg",
        "thumbnailUrl": "https://cdn.example.com/posts/456/thumb.jpg",
        "caption": "Beautiful sunset today! #sunset #photography",
        "likeCount": 25,
        "commentCount": 5,
        "isLikedByCurrentUser": true,
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "limit": 20,
      "offset": 0,
      "hasMore": true
    }
  }
}
```

### 2. Refresh Feed
```http
POST /api/v1/feed/refresh
Authorization: Bearer <token>

Response (200 OK):
{
  "success": true,
  "data": null,
  "message": "Feed refreshed successfully"
}
```

## File Upload APIs

### 1. Upload Profile Picture
```http
POST /api/v1/users/{userId}/profile-picture
Authorization: Bearer <token>
Content-Type: multipart/form-data

Form Data:
- image: [image file] (required)

Response (200 OK):
{
  "success": true,
  "data": {
    "profilePictureUrl": "https://cdn.example.com/profiles/123_new.jpg"
  },
  "message": "Profile picture updated successfully"
}

Error Responses:
400 Bad Request - Invalid file format
413 Payload Too Large - File size exceeds limit
```

## Rate Limiting

### Rate Limit Headers
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642248000
```

### Rate Limits by Endpoint
```
Authentication:
- Login: 5 requests per 15 minutes per IP
- Register: 3 requests per hour per IP

Posts:
- Create post: 10 requests per hour per user
- Like/Unlike: 100 requests per minute per user

Comments:
- Add comment: 30 requests per hour per user

Social:
- Follow/Unfollow: 50 requests per hour per user

General:
- API calls: 1000 requests per hour per user
```

## Error Codes

### HTTP Status Codes
```
200 OK - Request successful
201 Created - Resource created successfully
400 Bad Request - Invalid request data
401 Unauthorized - Authentication required
403 Forbidden - Access denied
404 Not Found - Resource not found
409 Conflict - Resource already exists
413 Payload Too Large - File size exceeds limit
422 Unprocessable Entity - Validation failed
429 Too Many Requests - Rate limit exceeded
500 Internal Server Error - Server error
503 Service Unavailable - Service temporarily unavailable
```

### Custom Error Codes
```json
{
  "success": false,
  "data": null,
  "message": "Validation failed",
  "errorCode": "VALIDATION_ERROR",
  "errors": [
    {
      "field": "email",
      "code": "INVALID_FORMAT",
      "message": "Email format is invalid"
    }
  ]
}
```

## API Versioning

### Version Strategy
```
Current Version: v1
URL Pattern: /api/v1/...
Header: Accept: application/vnd.socialmedia.v1+json

Future Versions:
- v2: /api/v2/...
- Backward compatibility maintained for 1 year
- Deprecation notices in response headers
```

## API Documentation

### OpenAPI/Swagger Specification
```yaml
openapi: 3.0.0
info:
  title: Social Media API
  version: 1.0.0
  description: API for social media platform
servers:
  - url: https://api.socialmedia.com/v1
    description: Production server
  - url: http://localhost:8080/api/v1
    description: Development server

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

This API design provides a comprehensive set of endpoints for the social media platform while maintaining simplicity appropriate for an SDE 1 level interview. The APIs follow RESTful principles, include proper error handling, and support pagination and rate limiting.