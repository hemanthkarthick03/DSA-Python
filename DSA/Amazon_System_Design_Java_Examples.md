# Amazon System Design with Java Examples - Social Media Network

Complete system design examples with Java implementations, FAQs, and Amazon-specific scenarios for social media platforms.

---

## Table of Contents
1. [Social Media Network - Complete Example](#social-media-network---complete-example)
2. [Java Implementation Examples](#java-implementation-examples)
3. [Amazon-Specific FAQs](#amazon-specific-faqs)
4. [Important Design Patterns](#important-design-patterns)
5. [Performance Optimization Examples](#performance-optimization-examples)
6. [Interview Scenarios & Solutions](#interview-scenarios--solutions)

---

## Social Media Network - Complete Example

### Problem Statement
**Interviewer**: "Design a social media platform like Facebook that can handle 3 billion users with 500 million daily active users. Focus on core features: user profiles, posts, news feed, and social connections."

### Phase 1: Requirements Analysis (12 minutes)

#### Clarifying Questions & Answers
```
Q: What are the core features we need to support?
A: User registration, posting content, following users, news feed, likes/comments

Q: What's the scale we're targeting?
A: 3B total users, 500M DAU, 100M posts/day, 10B feed requests/day

Q: What types of content should we support?
A: Text posts, images, videos (up to 1GB), links with previews

Q: What are the performance requirements?
A: <200ms for feed loading, <100ms for interactions, 99.99% availability

Q: Any specific constraints or preferences?
A: Use Java/Spring Boot, prefer AWS services, focus on scalability
```

#### Requirements Summary
```java
// Functional Requirements
public class FunctionalRequirements {
    // User Management
    - User registration and authentication
    - Profile creation and management
    - Privacy settings
    
    // Content Management
    - Create posts (text, image, video)
    - Edit/delete posts
    - Content moderation
    
    // Social Features
    - Follow/unfollow users
    - Like/unlike posts
    - Comment on posts
    - Share posts
    
    // News Feed
    - Personalized timeline
    - Real-time updates
    - Content ranking
}

// Non-Functional Requirements
public class NonFunctionalRequirements {
    public static final long TOTAL_USERS = 3_000_000_000L;
    public static final long DAILY_ACTIVE_USERS = 500_000_000L;
    public static final long POSTS_PER_DAY = 100_000_000L;
    public static final long FEED_REQUESTS_PER_DAY = 10_000_000_000L;
    
    public static final int MAX_FEED_LATENCY_MS = 200;
    public static final int MAX_INTERACTION_LATENCY_MS = 100;
    public static final double AVAILABILITY_TARGET = 99.99;
    
    public static final int READ_WRITE_RATIO = 100; // 100:1 read heavy
}
```

### Phase 2: High-Level Architecture (18 minutes)

#### System Architecture Diagram
```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Mobile    │    │   Web App    │    │   Admin Panel   │
│     App     │    │              │    │                 │
└─────────────┘    └──────────────┘    └─────────────────┘
        │                   │                     │
        └───────────────────┼─────────────────────┘
                            │
                    ┌───────────────┐
                    │ Load Balancer │
                    │   (AWS ALB)   │
                    └───────────────┘
                            │
                    ┌───────────────┐
                    │  API Gateway  │
                    │ (Rate Limiting)│
                    └───────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ User Service  │  │ Post Service  │  │ Feed Service  │
│   (Java)      │  │   (Java)      │  │   (Java)      │
└───────────────┘  └───────────────┘  └───────────────┘
        │                   │                   │
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   User DB     │  │   Post DB     │  │   Feed DB     │
│ (PostgreSQL)  │  │ (Cassandra)   │  │ (Cassandra)   │
└───────────────┘  └───────────────┘  └───────────────┘
```

#### Core Java Services Architecture
```java
// Main Application Architecture
@SpringBootApplication
@EnableEurekaClient
@EnableCircuitBreaker
public class SocialMediaApplication {
    
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
    
    @Bean
    public RedisTemplate<String, Object> redisTemplate() {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(jedisConnectionFactory());
        return template;
    }
    
    public static void main(String[] args) {
        SpringApplication.run(SocialMediaApplication.class, args);
    }
}

// Service Discovery Configuration
@Configuration
@EnableEurekaServer
public class ServiceDiscoveryConfig {
    // Eureka server configuration for microservices
}
```

### Phase 3: Detailed Java Implementation (20 minutes)

#### 1. User Service Implementation
```java
// User Entity
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;
    
    @Column(unique = true, nullable = false)
    private String username;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(nullable = false)
    private String passwordHash;
    
    private String firstName;
    private String lastName;
    private String bio;
    private String profilePictureUrl;
    private boolean isVerified;
    
    @Enumerated(EnumType.STRING)
    private PrivacyLevel privacyLevel = PrivacyLevel.PUBLIC;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    private LocalDateTime updatedAt;
    
    // Constructors, getters, setters
}

// User Service
@Service
@Transactional
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    private static final String USER_CACHE_PREFIX = "user:";
    private static final int CACHE_TTL = 3600; // 1 hour
    
    public UserDto createUser(CreateUserRequest request) {
        // Validate input
        validateUserRequest(request);
        
        // Check if user already exists
        if (userRepository.existsByEmail(request.getEmail()) || 
            userRepository.existsByUsername(request.getUsername())) {
            throw new UserAlreadyExistsException("User already exists");
        }
        
        // Create user entity
        User user = new User();
        user.setUsername(request.getUsername());
        user.setEmail(request.getEmail());
        user.setPasswordHash(passwordEncoder.encode(request.getPassword()));
        user.setFirstName(request.getFirstName());
        user.setLastName(request.getLastName());
        
        // Save to database
        User savedUser = userRepository.save(user);
        
        // Cache user data
        cacheUser(savedUser);
        
        // Publish user created event
        publishUserCreatedEvent(savedUser);
        
        return convertToDto(savedUser);
    }
    
    @Cacheable(value = "users", key = "#userId")
    public UserDto getUserById(Long userId) {
        // Try cache first
        String cacheKey = USER_CACHE_PREFIX + userId;
        UserDto cachedUser = (UserDto) redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedUser != null) {
            return cachedUser;
        }
        
        // Fallback to database
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found: " + userId));
        
        UserDto userDto = convertToDto(user);
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, userDto, CACHE_TTL, TimeUnit.SECONDS);
        
        return userDto;
    }
    
    public UserDto updateUser(Long userId, UpdateUserRequest request) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        // Update fields
        if (request.getFirstName() != null) {
            user.setFirstName(request.getFirstName());
        }
        if (request.getLastName() != null) {
            user.setLastName(request.getLastName());
        }
        if (request.getBio() != null) {
            user.setBio(request.getBio());
        }
        
        User updatedUser = userRepository.save(user);
        
        // Invalidate cache
        String cacheKey = USER_CACHE_PREFIX + userId;
        redisTemplate.delete(cacheKey);
        
        return convertToDto(updatedUser);
    }
    
    private void cacheUser(User user) {
        String cacheKey = USER_CACHE_PREFIX + user.getUserId();
        UserDto userDto = convertToDto(user);
        redisTemplate.opsForValue().set(cacheKey, userDto, CACHE_TTL, TimeUnit.SECONDS);
    }
    
    private void publishUserCreatedEvent(User user) {
        UserCreatedEvent event = new UserCreatedEvent(user.getUserId(), user.getUsername());
        // Publish to message queue (Kafka/RabbitMQ)
        eventPublisher.publishEvent(event);
    }
    
    private UserDto convertToDto(User user) {
        return UserDto.builder()
            .userId(user.getUserId())
            .username(user.getUsername())
            .email(user.getEmail())
            .firstName(user.getFirstName())
            .lastName(user.getLastName())
            .bio(user.getBio())
            .profilePictureUrl(user.getProfilePictureUrl())
            .isVerified(user.isVerified())
            .privacyLevel(user.getPrivacyLevel())
            .createdAt(user.getCreatedAt())
            .build();
    }
}

// User Controller
@RestController
@RequestMapping("/api/v1/users")
@Validated
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping("/register")
    public ResponseEntity<ApiResponse<UserDto>> registerUser(
            @Valid @RequestBody CreateUserRequest request) {
        
        UserDto user = userService.createUser(request);
        
        ApiResponse<UserDto> response = ApiResponse.<UserDto>builder()
            .success(true)
            .data(user)
            .message("User created successfully")
            .build();
            
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }
    
    @GetMapping("/{userId}")
    public ResponseEntity<ApiResponse<UserDto>> getUser(@PathVariable Long userId) {
        UserDto user = userService.getUserById(userId);
        
        ApiResponse<UserDto> response = ApiResponse.<UserDto>builder()
            .success(true)
            .data(user)
            .build();
            
        return ResponseEntity.ok(response);
    }
    
    @PutMapping("/{userId}")
    public ResponseEntity<ApiResponse<UserDto>> updateUser(
            @PathVariable Long userId,
            @Valid @RequestBody UpdateUserRequest request) {
        
        UserDto user = userService.updateUser(userId, request);
        
        ApiResponse<UserDto> response = ApiResponse.<UserDto>builder()
            .success(true)
            .data(user)
            .message("User updated successfully")
            .build();
            
        return ResponseEntity.ok(response);
    }
}
```#### 2
. Post Service Implementation
```java
// Post Entity
@Entity
@Table(name = "posts")
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postId;
    
    @Column(nullable = false)
    private Long userId;
    
    @Column(length = 5000)
    private String content;
    
    @ElementCollection
    @CollectionTable(name = "post_media", joinColumns = @JoinColumn(name = "post_id"))
    private List<String> mediaUrls = new ArrayList<>();
    
    @ElementCollection
    @CollectionTable(name = "post_hashtags", joinColumns = @JoinColumn(name = "post_id"))
    private Set<String> hashtags = new HashSet<>();
    
    @ElementCollection
    @CollectionTable(name = "post_mentions", joinColumns = @JoinColumn(name = "post_id"))
    private Set<Long> mentions = new HashSet<>();
    
    @Enumerated(EnumType.STRING)
    private PostType postType = PostType.TEXT;
    
    @Enumerated(EnumType.STRING)
    private PrivacyLevel privacyLevel = PrivacyLevel.PUBLIC;
    
    private Long likeCount = 0L;
    private Long commentCount = 0L;
    private Long shareCount = 0L;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    private LocalDateTime updatedAt;
    
    // Constructors, getters, setters
}

// Post Service with Caching and Performance Optimization
@Service
@Transactional
public class PostService {
    
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    @Autowired
    private S3Service s3Service;
    
    private static final String POST_CACHE_PREFIX = "post:";
    private static final String USER_POSTS_CACHE_PREFIX = "user_posts:";
    private static final int CACHE_TTL = 1800; // 30 minutes
    
    public PostDto createPost(CreatePostRequest request) {
        // Validate user exists
        UserDto user = userService.getUserById(request.getUserId());
        
        // Process media uploads
        List<String> mediaUrls = processMediaUploads(request.getMediaFiles());
        
        // Extract hashtags and mentions
        Set<String> hashtags = extractHashtags(request.getContent());
        Set<Long> mentions = extractMentions(request.getContent());
        
        // Create post entity
        Post post = new Post();
        post.setUserId(request.getUserId());
        post.setContent(request.getContent());
        post.setMediaUrls(mediaUrls);
        post.setHashtags(hashtags);
        post.setMentions(mentions);
        post.setPostType(determinePostType(request));
        post.setPrivacyLevel(request.getPrivacyLevel());
        
        // Save to database
        Post savedPost = postRepository.save(post);
        
        // Cache the post
        cachePost(savedPost);
        
        // Invalidate user's posts cache
        invalidateUserPostsCache(request.getUserId());
        
        // Publish post created event for feed generation
        publishPostCreatedEvent(savedPost);
        
        // Send notifications for mentions
        sendMentionNotifications(savedPost);
        
        return convertToDto(savedPost, user);
    }
    
    @Cacheable(value = "posts", key = "#postId")
    public PostDto getPost(Long postId) {
        String cacheKey = POST_CACHE_PREFIX + postId;
        PostDto cachedPost = (PostDto) redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedPost != null) {
            return cachedPost;
        }
        
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new PostNotFoundException("Post not found: " + postId));
        
        UserDto user = userService.getUserById(post.getUserId());
        PostDto postDto = convertToDto(post, user);
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, postDto, CACHE_TTL, TimeUnit.SECONDS);
        
        return postDto;
    }
    
    public PagedResponse<PostDto> getUserPosts(Long userId, int page, int size) {
        String cacheKey = USER_POSTS_CACHE_PREFIX + userId + ":" + page + ":" + size;
        PagedResponse<PostDto> cachedPosts = (PagedResponse<PostDto>) 
            redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedPosts != null) {
            return cachedPosts;
        }
        
        Pageable pageable = PageRequest.of(page, size, Sort.by("createdAt").descending());
        Page<Post> postsPage = postRepository.findByUserIdOrderByCreatedAtDesc(userId, pageable);
        
        UserDto user = userService.getUserById(userId);
        List<PostDto> postDtos = postsPage.getContent().stream()
            .map(post -> convertToDto(post, user))
            .collect(Collectors.toList());
        
        PagedResponse<PostDto> response = new PagedResponse<>(
            postDtos,
            postsPage.getNumber(),
            postsPage.getSize(),
            postsPage.getTotalElements(),
            postsPage.getTotalPages(),
            postsPage.isLast()
        );
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, response, CACHE_TTL, TimeUnit.SECONDS);
        
        return response;
    }
    
    @Transactional
    public PostDto likePost(Long postId, Long userId) {
        // Check if already liked
        if (isPostLikedByUser(postId, userId)) {
            throw new PostAlreadyLikedException("Post already liked by user");
        }
        
        // Add like record
        PostLike like = new PostLike(postId, userId);
        postLikeRepository.save(like);
        
        // Increment like count atomically
        postRepository.incrementLikeCount(postId);
        
        // Update cache
        updatePostLikeCountInCache(postId, 1);
        
        // Publish like event
        publishPostLikedEvent(postId, userId);
        
        return getPost(postId);
    }
    
    private List<String> processMediaUploads(List<MultipartFile> mediaFiles) {
        if (mediaFiles == null || mediaFiles.isEmpty()) {
            return new ArrayList<>();
        }
        
        return mediaFiles.stream()
            .map(file -> {
                try {
                    // Upload to S3 and return URL
                    return s3Service.uploadFile(file, "posts/media/");
                } catch (Exception e) {
                    throw new MediaUploadException("Failed to upload media", e);
                }
            })
            .collect(Collectors.toList());
    }
    
    private Set<String> extractHashtags(String content) {
        if (content == null) return new HashSet<>();
        
        Pattern hashtagPattern = Pattern.compile("#\\w+");
        Matcher matcher = hashtagPattern.matcher(content);
        
        Set<String> hashtags = new HashSet<>();
        while (matcher.find()) {
            hashtags.add(matcher.group().substring(1).toLowerCase()); // Remove # and lowercase
        }
        
        return hashtags;
    }
    
    private Set<Long> extractMentions(String content) {
        if (content == null) return new HashSet<>();
        
        Pattern mentionPattern = Pattern.compile("@(\\w+)");
        Matcher matcher = mentionPattern.matcher(content);
        
        Set<Long> mentions = new HashSet<>();
        while (matcher.find()) {
            String username = matcher.group(1);
            // Look up user ID by username
            try {
                UserDto user = userService.getUserByUsername(username);
                mentions.add(user.getUserId());
            } catch (UserNotFoundException e) {
                // Ignore invalid mentions
            }
        }
        
        return mentions;
    }
    
    private void publishPostCreatedEvent(Post post) {
        PostCreatedEvent event = PostCreatedEvent.builder()
            .postId(post.getPostId())
            .userId(post.getUserId())
            .content(post.getContent())
            .createdAt(post.getCreatedAt())
            .build();
        
        kafkaTemplate.send("post-created", event);
    }
    
    private PostDto convertToDto(Post post, UserDto user) {
        return PostDto.builder()
            .postId(post.getPostId())
            .userId(post.getUserId())
            .username(user.getUsername())
            .userProfilePicture(user.getProfilePictureUrl())
            .content(post.getContent())
            .mediaUrls(post.getMediaUrls())
            .hashtags(post.getHashtags())
            .mentions(post.getMentions())
            .postType(post.getPostType())
            .privacyLevel(post.getPrivacyLevel())
            .likeCount(post.getLikeCount())
            .commentCount(post.getCommentCount())
            .shareCount(post.getShareCount())
            .createdAt(post.getCreatedAt())
            .updatedAt(post.getUpdatedAt())
            .build();
    }
}

// Post Controller with Rate Limiting
@RestController
@RequestMapping("/api/v1/posts")
@Validated
public class PostController {
    
    @Autowired
    private PostService postService;
    
    @PostMapping
    @RateLimited(requests = 10, window = 3600) // 10 posts per hour
    public ResponseEntity<ApiResponse<PostDto>> createPost(
            @Valid @RequestBody CreatePostRequest request,
            @RequestParam(required = false) List<MultipartFile> mediaFiles) {
        
        request.setMediaFiles(mediaFiles);
        PostDto post = postService.createPost(request);
        
        ApiResponse<PostDto> response = ApiResponse.<PostDto>builder()
            .success(true)
            .data(post)
            .message("Post created successfully")
            .build();
            
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }
    
    @GetMapping("/{postId}")
    public ResponseEntity<ApiResponse<PostDto>> getPost(@PathVariable Long postId) {
        PostDto post = postService.getPost(postId);
        
        ApiResponse<PostDto> response = ApiResponse.<PostDto>builder()
            .success(true)
            .data(post)
            .build();
            
        return ResponseEntity.ok(response);
    }
    
    @GetMapping("/user/{userId}")
    public ResponseEntity<ApiResponse<PagedResponse<PostDto>>> getUserPosts(
            @PathVariable Long userId,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        
        PagedResponse<PostDto> posts = postService.getUserPosts(userId, page, size);
        
        ApiResponse<PagedResponse<PostDto>> response = ApiResponse.<PagedResponse<PostDto>>builder()
            .success(true)
            .data(posts)
            .build();
            
        return ResponseEntity.ok(response);
    }
    
    @PostMapping("/{postId}/like")
    @RateLimited(requests = 100, window = 60) // 100 likes per minute
    public ResponseEntity<ApiResponse<PostDto>> likePost(
            @PathVariable Long postId,
            @RequestHeader("X-User-Id") Long userId) {
        
        PostDto post = postService.likePost(postId, userId);
        
        ApiResponse<PostDto> response = ApiResponse.<PostDto>builder()
            .success(true)
            .data(post)
            .message("Post liked successfully")
            .build();
            
        return ResponseEntity.ok(response);
    }
}
```

#### 3. News Feed Service Implementation
```java
// Feed Service with Push/Pull Hybrid Model
@Service
public class FeedService {
    
    @Autowired
    private PostService postService;
    
    @Autowired
    private SocialGraphService socialGraphService;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    @Autowired
    private FeedRepository feedRepository;
    
    private static final String FEED_CACHE_PREFIX = "feed:";
    private static final int FEED_CACHE_TTL = 1800; // 30 minutes
    private static final int CELEBRITY_FOLLOWER_THRESHOLD = 1_000_000;
    
    public PagedResponse<PostDto> getUserFeed(Long userId, int page, int size) {
        String cacheKey = FEED_CACHE_PREFIX + userId + ":" + page + ":" + size;
        
        // Try cache first
        PagedResponse<PostDto> cachedFeed = (PagedResponse<PostDto>) 
            redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedFeed != null) {
            return cachedFeed;
        }
        
        // Determine feed generation strategy
        PagedResponse<PostDto> feed;
        if (isCelebrityFollower(userId)) {
            feed = generatePullModelFeed(userId, page, size);
        } else if (isActiveUser(userId)) {
            feed = generatePushModelFeed(userId, page, size);
        } else {
            feed = generateHybridModelFeed(userId, page, size);
        }
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, feed, FEED_CACHE_TTL, TimeUnit.SECONDS);
        
        return feed;
    }
    
    // Push Model: Pre-computed feeds for active users
    private PagedResponse<PostDto> generatePushModelFeed(Long userId, int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        Page<FeedItem> feedItems = feedRepository.findByUserIdOrderByCreatedAtDesc(userId, pageable);
        
        List<PostDto> posts = feedItems.getContent().stream()
            .map(item -> postService.getPost(item.getPostId()))
            .collect(Collectors.toList());
        
        return new PagedResponse<>(
            posts,
            feedItems.getNumber(),
            feedItems.getSize(),
            feedItems.getTotalElements(),
            feedItems.getTotalPages(),
            feedItems.isLast()
        );
    }
    
    // Pull Model: Generate feed on demand for celebrity followers
    private PagedResponse<PostDto> generatePullModelFeed(Long userId, int page, int size) {
        // Get users that this user follows
        List<Long> followingIds = socialGraphService.getFollowing(userId);
        
        if (followingIds.isEmpty()) {
            return new PagedResponse<>(new ArrayList<>(), page, size, 0, 0, true);
        }
        
        // Get recent posts from followed users
        Pageable pageable = PageRequest.of(page, size);
        Page<Post> recentPosts = postRepository.findRecentPostsByUserIds(
            followingIds, 
            LocalDateTime.now().minusDays(7), // Last 7 days
            pageable
        );
        
        // Convert to DTOs and rank
        List<PostDto> rankedPosts = recentPosts.getContent().stream()
            .map(post -> {
                UserDto user = userService.getUserById(post.getUserId());
                return postService.convertToDto(post, user);
            })
            .sorted(this::rankPosts)
            .collect(Collectors.toList());
        
        return new PagedResponse<>(
            rankedPosts,
            recentPosts.getNumber(),
            recentPosts.getSize(),
            recentPosts.getTotalElements(),
            recentPosts.getTotalPages(),
            recentPosts.isLast()
        );
    }
    
    // Hybrid Model: Combination of push and pull
    private PagedResponse<PostDto> generateHybridModelFeed(Long userId, int page, int size) {
        List<PostDto> feedPosts = new ArrayList<>();
        
        // Get some posts from pre-computed feed (push)
        PagedResponse<PostDto> pushFeed = generatePushModelFeed(userId, 0, size / 2);
        feedPosts.addAll(pushFeed.getContent());
        
        // Get some recent posts from followed users (pull)
        PagedResponse<PostDto> pullFeed = generatePullModelFeed(userId, 0, size / 2);
        feedPosts.addAll(pullFeed.getContent());
        
        // Merge and rank
        List<PostDto> rankedFeed = feedPosts.stream()
            .distinct()
            .sorted(this::rankPosts)
            .skip(page * size)
            .limit(size)
            .collect(Collectors.toList());
        
        return new PagedResponse<>(rankedFeed, page, size, feedPosts.size(), 
                                 (feedPosts.size() + size - 1) / size, 
                                 (page + 1) * size >= feedPosts.size());
    }
    
    // ML-based post ranking algorithm
    private int rankPosts(PostDto post1, PostDto post2) {
        double score1 = calculatePostScore(post1);
        double score2 = calculatePostScore(post2);
        return Double.compare(score2, score1); // Higher score first
    }
    
    private double calculatePostScore(PostDto post) {
        double score = 0.0;
        
        // Recency factor (newer posts get higher score)
        long hoursOld = ChronoUnit.HOURS.between(post.getCreatedAt(), LocalDateTime.now());
        double recencyScore = Math.max(0, 100 - hoursOld * 2); // Decay over time
        
        // Engagement factor
        double engagementScore = (post.getLikeCount() * 1.0) + 
                               (post.getCommentCount() * 2.0) + 
                               (post.getShareCount() * 3.0);
        
        // Content type factor
        double contentScore = switch (post.getPostType()) {
            case VIDEO -> 10.0;
            case IMAGE -> 5.0;
            case TEXT -> 1.0;
        };
        
        score = (recencyScore * 0.4) + (engagementScore * 0.4) + (contentScore * 0.2);
        
        return score;
    }
    
    // Event handler for new posts
    @EventListener
    @Async
    public void handlePostCreatedEvent(PostCreatedEvent event) {
        // Get followers of the user who created the post
        List<Long> followers = socialGraphService.getFollowers(event.getUserId());
        
        // Add post to followers' feeds (push model)
        for (Long followerId : followers) {
            if (!isCelebrityFollower(followerId)) {
                FeedItem feedItem = new FeedItem();
                feedItem.setUserId(followerId);
                feedItem.setPostId(event.getPostId());
                feedItem.setAuthorId(event.getUserId());
                feedItem.setCreatedAt(event.getCreatedAt());
                
                feedRepository.save(feedItem);
                
                // Invalidate cache
                invalidateFeedCache(followerId);
            }
        }
    }
    
    private boolean isCelebrityFollower(Long userId) {
        List<Long> following = socialGraphService.getFollowing(userId);
        return following.stream()
            .anyMatch(followingId -> {
                int followerCount = socialGraphService.getFollowerCount(followingId);
                return followerCount > CELEBRITY_FOLLOWER_THRESHOLD;
            });
    }
    
    private boolean isActiveUser(Long userId) {
        // Check if user has been active in the last 7 days
        String lastActiveKey = "user:last_active:" + userId;
        String lastActive = (String) redisTemplate.opsForValue().get(lastActiveKey);
        
        if (lastActive == null) {
            return false;
        }
        
        LocalDateTime lastActiveTime = LocalDateTime.parse(lastActive);
        return ChronoUnit.DAYS.between(lastActiveTime, LocalDateTime.now()) <= 7;
    }
    
    private void invalidateFeedCache(Long userId) {
        Set<String> keys = redisTemplate.keys(FEED_CACHE_PREFIX + userId + ":*");
        if (keys != null && !keys.isEmpty()) {
            redisTemplate.delete(keys);
        }
    }
}

// Feed Controller
@RestController
@RequestMapping("/api/v1/feed")
public class FeedController {
    
    @Autowired
    private FeedService feedService;
    
    @GetMapping
    public ResponseEntity<ApiResponse<PagedResponse<PostDto>>> getUserFeed(
            @RequestHeader("X-User-Id") Long userId,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        
        PagedResponse<PostDto> feed = feedService.getUserFeed(userId, page, size);
        
        ApiResponse<PagedResponse<PostDto>> response = ApiResponse.<PagedResponse<PostDto>>builder()
            .success(true)
            .data(feed)
            .build();
            
        return ResponseEntity.ok(response);
    }
    
    @PostMapping("/refresh")
    public ResponseEntity<ApiResponse<String>> refreshFeed(
            @RequestHeader("X-User-Id") Long userId) {
        
        feedService.refreshUserFeed(userId);
        
        ApiResponse<String> response = ApiResponse.<String>builder()
            .success(true)
            .message("Feed refreshed successfully")
            .build();
            
        return ResponseEntity.ok(response);
    }
}
```