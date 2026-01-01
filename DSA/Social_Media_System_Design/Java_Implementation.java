// Social Media Platform - Core Java Implementation (SDE 1 Level)
// This file contains the essential Java code for the social media system design interview

package com.socialmedia;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;

// ============================================================================
// MAIN APPLICATION CLASS
// ============================================================================

@SpringBootApplication
public class SocialMediaApplication {
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Bean
    public RedisTemplate<String, Object> redisTemplate() {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(new JedisConnectionFactory());
        return template;
    }
    
    public static void main(String[] args) {
        SpringApplication.run(SocialMediaApplication.class, args);
    }
}

// ============================================================================
// ENTITY CLASSES
// ============================================================================

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;
    
    @Column(unique = true, nullable = false, length = 50)
    private String username;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(nullable = false)
    private String passwordHash;
    
    @Column(length = 100)
    private String fullName;
    
    @Column(columnDefinition = "TEXT")
    private String bio;
    
    @Column(length = 500)
    private String profilePictureUrl;
    
    @Column(nullable = false)
    private Boolean isVerified = false;
    
    @Column(nullable = false)
    private Boolean isActive = true;
    
    @Column(nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
    
    @Column(nullable = false)
    private LocalDateTime updatedAt = LocalDateTime.now();
    
    // Constructors
    public User() {}
    
    public User(String username, String email, String passwordHash, String fullName) {
        this.username = username;
        this.email = email;
        this.passwordHash = passwordHash;
        this.fullName = fullName;
    }
    
    // Getters and Setters
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public String getPasswordHash() { return passwordHash; }
    public void setPasswordHash(String passwordHash) { this.passwordHash = passwordHash; }
    
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    
    public String getBio() { return bio; }
    public void setBio(String bio) { this.bio = bio; }
    
    public String getProfilePictureUrl() { return profilePictureUrl; }
    public void setProfilePictureUrl(String profilePictureUrl) { this.profilePictureUrl = profilePictureUrl; }
    
    public Boolean getIsVerified() { return isVerified; }
    public void setIsVerified(Boolean isVerified) { this.isVerified = isVerified; }
    
    public Boolean getIsActive() { return isActive; }
    public void setIsActive(Boolean isActive) { this.isActive = isActive; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}

@Entity
@Table(name = "posts")
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postId;
    
    @Column(nullable = false)
    private Long userId;
    
    @Column(nullable = false, length = 500)
    private String photoUrl;
    
    @Column(length = 500)
    private String thumbnailUrl;
    
    @Column(columnDefinition = "TEXT")
    private String caption;
    
    @Column(nullable = false)
    private Integer likeCount = 0;
    
    @Column(nullable = false)
    private Integer commentCount = 0;
    
    @Column(nullable = false)
    private Boolean isActive = true;
    
    @Column(nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
    
    @Column(nullable = false)
    private LocalDateTime updatedAt = LocalDateTime.now();
    
    // Constructors
    public Post() {}
    
    public Post(Long userId, String photoUrl, String caption) {
        this.userId = userId;
        this.photoUrl = photoUrl;
        this.caption = caption;
    }
    
    // Getters and Setters
    public Long getPostId() { return postId; }
    public void setPostId(Long postId) { this.postId = postId; }
    
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    
    public String getPhotoUrl() { return photoUrl; }
    public void setPhotoUrl(String photoUrl) { this.photoUrl = photoUrl; }
    
    public String getThumbnailUrl() { return thumbnailUrl; }
    public void setThumbnailUrl(String thumbnailUrl) { this.thumbnailUrl = thumbnailUrl; }
    
    public String getCaption() { return caption; }
    public void setCaption(String caption) { this.caption = caption; }
    
    public Integer getLikeCount() { return likeCount; }
    public void setLikeCount(Integer likeCount) { this.likeCount = likeCount; }
    
    public Integer getCommentCount() { return commentCount; }
    public void setCommentCount(Integer commentCount) { this.commentCount = commentCount; }
    
    public Boolean getIsActive() { return isActive; }
    public void setIsActive(Boolean isActive) { this.isActive = isActive; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}

@Entity
@Table(name = "follows")
public class Follow {
    @EmbeddedId
    private FollowId id;
    
    @Column(nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
    
    // Constructors
    public Follow() {}
    
    public Follow(Long followerId, Long followingId) {
        this.id = new FollowId(followerId, followingId);
    }
    
    // Getters and Setters
    public FollowId getId() { return id; }
    public void setId(FollowId id) { this.id = id; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}

@Embeddable
public class FollowId implements Serializable {
    @Column(name = "follower_id")
    private Long followerId;
    
    @Column(name = "following_id")
    private Long followingId;
    
    // Constructors
    public FollowId() {}
    
    public FollowId(Long followerId, Long followingId) {
        this.followerId = followerId;
        this.followingId = followingId;
    }
    
    // Getters, Setters, equals, hashCode
    public Long getFollowerId() { return followerId; }
    public void setFollowerId(Long followerId) { this.followerId = followerId; }
    
    public Long getFollowingId() { return followingId; }
    public void setFollowingId(Long followingId) { this.followingId = followingId; }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof FollowId)) return false;
        FollowId followId = (FollowId) o;
        return Objects.equals(followerId, followId.followerId) &&
               Objects.equals(followingId, followId.followingId);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(followerId, followingId);
    }
}

@Entity
@Table(name = "likes")
public class Like {
    @EmbeddedId
    private LikeId id;
    
    @Column(nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
    
    // Constructors
    public Like() {}
    
    public Like(Long userId, Long postId) {
        this.id = new LikeId(userId, postId);
    }
    
    // Getters and Setters
    public LikeId getId() { return id; }
    public void setId(LikeId id) { this.id = id; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}

@Embeddable
public class LikeId implements Serializable {
    @Column(name = "user_id")
    private Long userId;
    
    @Column(name = "post_id")
    private Long postId;
    
    // Constructors
    public LikeId() {}
    
    public LikeId(Long userId, Long postId) {
        this.userId = userId;
        this.postId = postId;
    }
    
    // Getters, Setters, equals, hashCode
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    
    public Long getPostId() { return postId; }
    public void setPostId(Long postId) { this.postId = postId; }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof LikeId)) return false;
        LikeId likeId = (LikeId) o;
        return Objects.equals(userId, likeId.userId) &&
               Objects.equals(postId, likeId.postId);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(userId, postId);
    }
}

// ============================================================================
// REPOSITORY INTERFACES
// ============================================================================

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import java.util.Optional;
import java.util.List;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    Optional<User> findByUsername(String username);
    
    Optional<User> findByEmail(String email);
    
    boolean existsByUsername(String username);
    
    boolean existsByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE " +
           "(LOWER(u.username) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "LOWER(u.fullName) LIKE LOWER(CONCAT('%', :query, '%'))) AND " +
           "u.isActive = true")
    Page<User> searchUsers(@Param("query") String query, Pageable pageable);
}

@Repository
public interface PostRepository extends JpaRepository<Post, Long> {
    
    Page<Post> findByUserIdAndIsActiveOrderByCreatedAtDesc(Long userId, Boolean isActive, Pageable pageable);
    
    @Query("SELECT p FROM Post p JOIN User u ON p.userId = u.userId " +
           "WHERE p.userId IN :userIds AND p.isActive = true " +
           "ORDER BY p.createdAt DESC")
    Page<Post> findPostsByUserIds(@Param("userIds") List<Long> userIds, Pageable pageable);
    
    @Query("SELECT COUNT(p) FROM Post p WHERE p.userId = :userId AND p.isActive = true")
    Long countPostsByUserId(@Param("userId") Long userId);
}

@Repository
public interface FollowRepository extends JpaRepository<Follow, FollowId> {
    
    @Query("SELECT f.id.followingId FROM Follow f WHERE f.id.followerId = :userId")
    List<Long> findFollowingIdsByUserId(@Param("userId") Long userId);
    
    @Query("SELECT f.id.followerId FROM Follow f WHERE f.id.followingId = :userId")
    List<Long> findFollowerIdsByUserId(@Param("userId") Long userId);
    
    @Query("SELECT COUNT(f) FROM Follow f WHERE f.id.followerId = :userId")
    Long countFollowingByUserId(@Param("userId") Long userId);
    
    @Query("SELECT COUNT(f) FROM Follow f WHERE f.id.followingId = :userId")
    Long countFollowersByUserId(@Param("userId") Long userId);
    
    boolean existsById(FollowId id);
}

@Repository
public interface LikeRepository extends JpaRepository<Like, LikeId> {
    
    @Query("SELECT COUNT(l) FROM Like l WHERE l.id.postId = :postId")
    Long countLikesByPostId(@Param("postId") Long postId);
    
    boolean existsById(LikeId id);
    
    @Query("SELECT l.id.userId FROM Like l WHERE l.id.postId = :postId")
    List<Long> findUserIdsByPostId(@Param("postId") Long postId);
}

// ============================================================================
// SERVICE CLASSES
// ============================================================================

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import java.util.concurrent.TimeUnit;

@Service
@Transactional
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private FollowRepository followRepository;
    
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    private static final String USER_CACHE_PREFIX = "user:";
    private static final int CACHE_TTL_HOURS = 1;
    
    public UserDto createUser(CreateUserRequest request) {
        // Validate input
        if (userRepository.existsByUsername(request.getUsername())) {
            throw new UserAlreadyExistsException("Username already exists");
        }
        
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new UserAlreadyExistsException("Email already exists");
        }
        
        // Create user
        User user = new User();
        user.setUsername(request.getUsername());
        user.setEmail(request.getEmail());
        user.setPasswordHash(passwordEncoder.encode(request.getPassword()));
        user.setFullName(request.getFullName());
        
        User savedUser = userRepository.save(user);
        
        // Cache user data
        cacheUser(savedUser);
        
        return convertToDto(savedUser);
    }
    
    public UserDto getUserById(Long userId) {
        // Check cache first
        String cacheKey = USER_CACHE_PREFIX + userId;
        UserDto cachedUser = (UserDto) redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedUser != null) {
            return cachedUser;
        }
        
        // Fetch from database
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        UserDto userDto = convertToDto(user);
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, userDto, CACHE_TTL_HOURS, TimeUnit.HOURS);
        
        return userDto;
    }
    
    public UserDto updateUser(Long userId, UpdateUserRequest request) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        // Update fields
        if (request.getFullName() != null) {
            user.setFullName(request.getFullName());
        }
        if (request.getBio() != null) {
            user.setBio(request.getBio());
        }
        if (request.getProfilePictureUrl() != null) {
            user.setProfilePictureUrl(request.getProfilePictureUrl());
        }
        
        user.setUpdatedAt(LocalDateTime.now());
        User updatedUser = userRepository.save(user);
        
        // Invalidate cache
        String cacheKey = USER_CACHE_PREFIX + userId;
        redisTemplate.delete(cacheKey);
        
        return convertToDto(updatedUser);
    }
    
    public Page<UserDto> searchUsers(String query, int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        Page<User> users = userRepository.searchUsers(query, pageable);
        
        return users.map(this::convertToDto);
    }
    
    private void cacheUser(User user) {
        String cacheKey = USER_CACHE_PREFIX + user.getUserId();
        UserDto userDto = convertToDto(user);
        redisTemplate.opsForValue().set(cacheKey, userDto, CACHE_TTL_HOURS, TimeUnit.HOURS);
    }
    
    private UserDto convertToDto(User user) {
        UserDto dto = new UserDto();
        dto.setUserId(user.getUserId());
        dto.setUsername(user.getUsername());
        dto.setEmail(user.getEmail());
        dto.setFullName(user.getFullName());
        dto.setBio(user.getBio());
        dto.setProfilePictureUrl(user.getProfilePictureUrl());
        dto.setIsVerified(user.getIsVerified());
        dto.setCreatedAt(user.getCreatedAt());
        
        // Add counts
        dto.setPostCount(postRepository.countPostsByUserId(user.getUserId()));
        dto.setFollowerCount(followRepository.countFollowersByUserId(user.getUserId()));
        dto.setFollowingCount(followRepository.countFollowingByUserId(user.getUserId()));
        
        return dto;
    }
}

@Service
@Transactional
public class PostService {
    
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private LikeRepository likeRepository;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    private static final String POST_CACHE_PREFIX = "post:";
    private static final int CACHE_TTL_MINUTES = 30;
    
    public PostDto createPost(CreatePostRequest request) {
        // Validate user exists
        User user = userRepository.findById(request.getUserId())
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        // Create post
        Post post = new Post();
        post.setUserId(request.getUserId());
        post.setPhotoUrl(request.getPhotoUrl());
        post.setThumbnailUrl(request.getThumbnailUrl());
        post.setCaption(request.getCaption());
        
        Post savedPost = postRepository.save(post);
        
        // Cache the post
        cachePost(savedPost);
        
        return convertToDto(savedPost, user);
    }
    
    public PostDto getPost(Long postId) {
        // Check cache first
        String cacheKey = POST_CACHE_PREFIX + postId;
        PostDto cachedPost = (PostDto) redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedPost != null) {
            return cachedPost;
        }
        
        // Fetch from database
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new PostNotFoundException("Post not found"));
        
        User user = userRepository.findById(post.getUserId())
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        PostDto postDto = convertToDto(post, user);
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, postDto, CACHE_TTL_MINUTES, TimeUnit.MINUTES);
        
        return postDto;
    }
    
    public Page<PostDto> getUserPosts(Long userId, int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        Page<Post> posts = postRepository.findByUserIdAndIsActiveOrderByCreatedAtDesc(userId, true, pageable);
        
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        return posts.map(post -> convertToDto(post, user));
    }
    
    public PostDto likePost(Long postId, Long userId) {
        // Check if post exists
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new PostNotFoundException("Post not found"));
        
        // Check if already liked
        LikeId likeId = new LikeId(userId, postId);
        if (likeRepository.existsById(likeId)) {
            throw new PostAlreadyLikedException("Post already liked");
        }
        
        // Create like
        Like like = new Like(userId, postId);
        likeRepository.save(like);
        
        // Update like count
        post.setLikeCount(post.getLikeCount() + 1);
        postRepository.save(post);
        
        // Invalidate cache
        String cacheKey = POST_CACHE_PREFIX + postId;
        redisTemplate.delete(cacheKey);
        
        return getPost(postId);
    }
    
    public PostDto unlikePost(Long postId, Long userId) {
        // Check if post exists
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new PostNotFoundException("Post not found"));
        
        // Check if liked
        LikeId likeId = new LikeId(userId, postId);
        if (!likeRepository.existsById(likeId)) {
            throw new PostNotLikedException("Post not liked");
        }
        
        // Remove like
        likeRepository.deleteById(likeId);
        
        // Update like count
        post.setLikeCount(Math.max(0, post.getLikeCount() - 1));
        postRepository.save(post);
        
        // Invalidate cache
        String cacheKey = POST_CACHE_PREFIX + postId;
        redisTemplate.delete(cacheKey);
        
        return getPost(postId);
    }
    
    private void cachePost(Post post) {
        User user = userRepository.findById(post.getUserId()).orElse(null);
        if (user != null) {
            String cacheKey = POST_CACHE_PREFIX + post.getPostId();
            PostDto postDto = convertToDto(post, user);
            redisTemplate.opsForValue().set(cacheKey, postDto, CACHE_TTL_MINUTES, TimeUnit.MINUTES);
        }
    }
    
    private PostDto convertToDto(Post post, User user) {
        PostDto dto = new PostDto();
        dto.setPostId(post.getPostId());
        dto.setUserId(post.getUserId());
        dto.setUsername(user.getUsername());
        dto.setUserFullName(user.getFullName());
        dto.setUserProfilePicture(user.getProfilePictureUrl());
        dto.setIsUserVerified(user.getIsVerified());
        dto.setPhotoUrl(post.getPhotoUrl());
        dto.setThumbnailUrl(post.getThumbnailUrl());
        dto.setCaption(post.getCaption());
        dto.setLikeCount(post.getLikeCount());
        dto.setCommentCount(post.getCommentCount());
        dto.setCreatedAt(post.getCreatedAt());
        
        return dto;
    }
}

@Service
@Transactional
public class SocialService {
    
    @Autowired
    private FollowRepository followRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    public FollowDto followUser(Long followerId, Long followingId) {
        // Validate users exist
        if (!userRepository.existsById(followerId)) {
            throw new UserNotFoundException("Follower not found");
        }
        
        if (!userRepository.existsById(followingId)) {
            throw new UserNotFoundException("User to follow not found");
        }
        
        // Check if already following
        FollowId followId = new FollowId(followerId, followingId);
        if (followRepository.existsById(followId)) {
            throw new AlreadyFollowingException("Already following user");
        }
        
        // Create follow relationship
        Follow follow = new Follow(followerId, followingId);
        followRepository.save(follow);
        
        FollowDto dto = new FollowDto();
        dto.setFollowerId(followerId);
        dto.setFollowingId(followingId);
        dto.setIsFollowing(true);
        dto.setFollowedAt(follow.getCreatedAt());
        
        return dto;
    }
    
    public void unfollowUser(Long followerId, Long followingId) {
        FollowId followId = new FollowId(followerId, followingId);
        
        if (!followRepository.existsById(followId)) {
            throw new NotFollowingException("Not following user");
        }
        
        followRepository.deleteById(followId);
    }
    
    public List<Long> getFollowing(Long userId) {
        return followRepository.findFollowingIdsByUserId(userId);
    }
    
    public List<Long> getFollowers(Long userId) {
        return followRepository.findFollowerIdsByUserId(userId);
    }
    
    public boolean isFollowing(Long followerId, Long followingId) {
        FollowId followId = new FollowId(followerId, followingId);
        return followRepository.existsById(followId);
    }
}

@Service
public class FeedService {
    
    @Autowired
    private PostRepository postRepository;
    
    @Autowired
    private SocialService socialService;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    private static final String FEED_CACHE_PREFIX = "feed:";
    private static final int CACHE_TTL_MINUTES = 15;
    
    public Page<PostDto> getUserFeed(Long userId, int page, int size) {
        // Check cache first
        String cacheKey = FEED_CACHE_PREFIX + userId + ":" + page + ":" + size;
        Page<PostDto> cachedFeed = (Page<PostDto>) redisTemplate.opsForValue().get(cacheKey);
        
        if (cachedFeed != null) {
            return cachedFeed;
        }
        
        // Get users that this user follows
        List<Long> followingIds = socialService.getFollowing(userId);
        
        if (followingIds.isEmpty()) {
            return Page.empty();
        }
        
        // Get posts from followed users
        Pageable pageable = PageRequest.of(page, size);
        Page<Post> posts = postRepository.findPostsByUserIds(followingIds, pageable);
        
        // Convert to DTOs
        Page<PostDto> feedPosts = posts.map(post -> {
            User user = userRepository.findById(post.getUserId()).orElse(null);
            return convertToDto(post, user);
        });
        
        // Cache the result
        redisTemplate.opsForValue().set(cacheKey, feedPosts, CACHE_TTL_MINUTES, TimeUnit.MINUTES);
        
        return feedPosts;
    }
    
    private PostDto convertToDto(Post post, User user) {
        // Same conversion logic as PostService
        PostDto dto = new PostDto();
        dto.setPostId(post.getPostId());
        dto.setUserId(post.getUserId());
        dto.setUsername(user != null ? user.getUsername() : "unknown");
        dto.setUserFullName(user != null ? user.getFullName() : "Unknown User");
        dto.setUserProfilePicture(user != null ? user.getProfilePictureUrl() : null);
        dto.setIsUserVerified(user != null ? user.getIsVerified() : false);
        dto.setPhotoUrl(post.getPhotoUrl());
        dto.setThumbnailUrl(post.getThumbnailUrl());
        dto.setCaption(post.getCaption());
        dto.setLikeCount(post.getLikeCount());
        dto.setCommentCount(post.getCommentCount());
        dto.setCreatedAt(post.getCreatedAt());
        
        return dto;
    }
}

// ============================================================================
// CONTROLLER CLASSES
// ============================================================================

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.data.domain.Page;
import javax.validation.Valid;

@RestController
@RequestMapping("/api/v1/users")
@CrossOrigin(origins = "*")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping("/register")
    public ResponseEntity<ApiResponse<UserDto>> registerUser(
            @Valid @RequestBody CreateUserRequest request) {
        
        UserDto user = userService.createUser(request);
        
        ApiResponse<UserDto> response = new ApiResponse<>(
            true, user, "User registered successfully", null
        );
        
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }
    
    @GetMapping("/{userId}")
    public ResponseEntity<ApiResponse<UserDto>> getUser(@PathVariable Long userId) {
        UserDto user = userService.getUserById(userId);
        
        ApiResponse<UserDto> response = new ApiResponse<>(
            true, user, null, null
        );
        
        return ResponseEntity.ok(response);
    }
    
    @PutMapping("/{userId}")
    public ResponseEntity<ApiResponse<UserDto>> updateUser(
            @PathVariable Long userId,
            @Valid @RequestBody UpdateUserRequest request) {
        
        UserDto user = userService.updateUser(userId, request);
        
        ApiResponse<UserDto> response = new ApiResponse<>(
            true, user, "User updated successfully", null
        );
        
        return ResponseEntity.ok(response);
    }
    
    @GetMapping("/search")
    public ResponseEntity<ApiResponse<Page<UserDto>>> searchUsers(
            @RequestParam String q,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        
        Page<UserDto> users = userService.searchUsers(q, page, size);
        
        ApiResponse<Page<UserDto>> response = new ApiResponse<>(
            true, users, null, null
        );
        
        return ResponseEntity.ok(response);
    }
}

@RestController
@RequestMapping("/api/v1/posts")
@CrossOrigin(origins = "*")
public class PostController {
    
    @Autowired
    private PostService postService;
    
    @PostMapping
    public ResponseEntity<ApiResponse<PostDto>> createPost(
            @Valid @RequestBody CreatePostRequest request) {
        
        PostDto post = postService.createPost(request);
        
        ApiResponse<PostDto> response = new ApiResponse<>(
            true, post, "Post created successfully", null
        );
        
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }
    
    @GetMapping("/{postId}")
    public ResponseEntity<ApiResponse<PostDto>> getPost(@PathVariable Long postId) {
        PostDto post = postService.getPost(postId);
        
        ApiResponse<PostDto> response = new ApiResponse<>(
            true, post, null, null
        );
        
        return ResponseEntity.ok(response);
    }
    
    @PostMapping("/{postId}/like")
    public ResponseEntity<ApiResponse<PostDto>> likePost(
            @PathVariable Long postId,
            @RequestHeader("X-User-Id") Long userId) {
        
        PostDto post = postService.likePost(postId, userId);
        
        ApiResponse<PostDto> response = new ApiResponse<>(
            true, post, "Post liked successfully", null
        );
        
        return ResponseEntity.ok(response);
    }
    
    @DeleteMapping("/{postId}/like")
    public ResponseEntity<ApiResponse<PostDto>> unlikePost(
            @PathVariable Long postId,
            @RequestHeader("X-User-Id") Long userId) {
        
        PostDto post = postService.unlikePost(postId, userId);
        
        ApiResponse<PostDto> response = new ApiResponse<>(
            true, post, "Post unliked successfully", null
        );
        
        return ResponseEntity.ok(response);
    }
}

@RestController
@RequestMapping("/api/v1")
@CrossOrigin(origins = "*")
public class SocialController {
    
    @Autowired
    private SocialService socialService;
    
    @PostMapping("/users/{userId}/follow")
    public ResponseEntity<ApiResponse<FollowDto>> followUser(
            @PathVariable Long userId,
            @RequestHeader("X-User-Id") Long followerId) {
        
        FollowDto follow = socialService.followUser(followerId, userId);
        
        ApiResponse<FollowDto> response = new ApiResponse<>(
            true, follow, "User followed successfully", null
        );
        
        return ResponseEntity.ok(response);
    }
    
    @DeleteMapping("/users/{userId}/follow")
    public ResponseEntity<ApiResponse<String>> unfollowUser(
            @PathVariable Long userId,
            @RequestHeader("X-User-Id") Long followerId) {
        
        socialService.unfollowUser(followerId, userId);
        
        ApiResponse<String> response = new ApiResponse<>(
            true, null, "User unfollowed successfully", null
        );
        
        return ResponseEntity.ok(response);
    }
}

@RestController
@RequestMapping("/api/v1/feed")
@CrossOrigin(origins = "*")
public class FeedController {
    
    @Autowired
    private FeedService feedService;
    
    @GetMapping
    public ResponseEntity<ApiResponse<Page<PostDto>>> getUserFeed(
            @RequestHeader("X-User-Id") Long userId,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        
        Page<PostDto> feed = feedService.getUserFeed(userId, page, size);
        
        ApiResponse<Page<PostDto>> response = new ApiResponse<>(
            true, feed, null, null
        );
        
        return ResponseEntity.ok(response);
    }
}

// ============================================================================
// DTO CLASSES
// ============================================================================

public class UserDto {
    private Long userId;
    private String username;
    private String email;
    private String fullName;
    private String bio;
    private String profilePictureUrl;
    private Boolean isVerified;
    private Long postCount;
    private Long followerCount;
    private Long followingCount;
    private LocalDateTime createdAt;
    
    // Constructors, getters, and setters
    public UserDto() {}
    
    // All getters and setters...
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    
    // ... (other getters and setters)
}

public class PostDto {
    private Long postId;
    private Long userId;
    private String username;
    private String userFullName;
    private String userProfilePicture;
    private Boolean isUserVerified;
    private String photoUrl;
    private String thumbnailUrl;
    private String caption;
    private Integer likeCount;
    private Integer commentCount;
    private Boolean isLikedByCurrentUser;
    private LocalDateTime createdAt;
    
    // Constructors, getters, and setters
    public PostDto() {}
    
    // All getters and setters...
    public Long getPostId() { return postId; }
    public void setPostId(Long postId) { this.postId = postId; }
    
    // ... (other getters and setters)
}

public class ApiResponse<T> {
    private boolean success;
    private T data;
    private String message;
    private LocalDateTime timestamp;
    private List<String> errors;
    
    public ApiResponse(boolean success, T data, String message, List<String> errors) {
        this.success = success;
        this.data = data;
        this.message = message;
        this.errors = errors;
        this.timestamp = LocalDateTime.now();
    }
    
    // Getters and setters
    public boolean isSuccess() { return success; }
    public void setSuccess(boolean success) { this.success = success; }
    
    public T getData() { return data; }
    public void setData(T data) { this.data = data; }
    
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    
    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
    
    public List<String> getErrors() { return errors; }
    public void setErrors(List<String> errors) { this.errors = errors; }
}

// ============================================================================
// REQUEST/RESPONSE CLASSES
// ============================================================================

import javax.validation.constraints.*;

public class CreateUserRequest {
    @NotBlank(message = "Username is required")
    @Size(min = 3, max = 50, message = "Username must be between 3 and 50 characters")
    private String username;
    
    @NotBlank(message = "Email is required")
    @Email(message = "Email format is invalid")
    private String email;
    
    @NotBlank(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    private String password;
    
    @Size(max = 100, message = "Full name cannot exceed 100 characters")
    private String fullName;
    
    // Constructors, getters, and setters
    public CreateUserRequest() {}
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
}

public class CreatePostRequest {
    @NotNull(message = "User ID is required")
    private Long userId;
    
    @NotBlank(message = "Photo URL is required")
    private String photoUrl;
    
    private String thumbnailUrl;
    
    @Size(max = 2200, message = "Caption cannot exceed 2200 characters")
    private String caption;
    
    // Constructors, getters, and setters
    public CreatePostRequest() {}
    
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    
    public String getPhotoUrl() { return photoUrl; }
    public void setPhotoUrl(String photoUrl) { this.photoUrl = photoUrl; }
    
    public String getThumbnailUrl() { return thumbnailUrl; }
    public void setThumbnailUrl(String thumbnailUrl) { this.thumbnailUrl = thumbnailUrl; }
    
    public String getCaption() { return caption; }
    public void setCaption(String caption) { this.caption = caption; }
}

// ============================================================================
// EXCEPTION CLASSES
// ============================================================================

public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}

public class UserAlreadyExistsException extends RuntimeException {
    public UserAlreadyExistsException(String message) {
        super(message);
    }
}

public class PostNotFoundException extends RuntimeException {
    public PostNotFoundException(String message) {
        super(message);
    }
}

public class PostAlreadyLikedException extends RuntimeException {
    public PostAlreadyLikedException(String message) {
        super(message);
    }
}

public class PostNotLikedException extends RuntimeException {
    public PostNotLikedException(String message) {
        super(message);
    }
}

public class AlreadyFollowingException extends RuntimeException {
    public AlreadyFollowingException(String message) {
        super(message);
    }
}

public class NotFollowingException extends RuntimeException {
    public NotFollowingException(String message) {
        super(message);
    }
}

// ============================================================================
// GLOBAL EXCEPTION HANDLER
// ============================================================================

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.MethodArgumentNotValidException;
import java.util.List;
import java.util.stream.Collectors;

@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ApiResponse<Object>> handleUserNotFound(UserNotFoundException ex) {
        ApiResponse<Object> response = new ApiResponse<>(
            false, null, ex.getMessage(), null
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
    }
    
    @ExceptionHandler(UserAlreadyExistsException.class)
    public ResponseEntity<ApiResponse<Object>> handleUserAlreadyExists(UserAlreadyExistsException ex) {
        ApiResponse<Object> response = new ApiResponse<>(
            false, null, ex.getMessage(), null
        );
        return ResponseEntity.status(HttpStatus.CONFLICT).body(response);
    }
    
    @ExceptionHandler(PostNotFoundException.class)
    public ResponseEntity<ApiResponse<Object>> handlePostNotFound(PostNotFoundException ex) {
        ApiResponse<Object> response = new ApiResponse<>(
            false, null, ex.getMessage(), null
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<Object>> handleValidationErrors(MethodArgumentNotValidException ex) {
        BindingResult bindingResult = ex.getBindingResult();
        List<String> errors = bindingResult.getFieldErrors().stream()
            .map(error -> error.getField() + ": " + error.getDefaultMessage())
            .collect(Collectors.toList());
        
        ApiResponse<Object> response = new ApiResponse<>(
            false, null, "Validation failed", errors
        );
        
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(response);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Object>> handleGenericException(Exception ex) {
        ApiResponse<Object> response = new ApiResponse<>(
            false, null, "Internal server error", null
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(response);
    }
}

/*
 * This Java implementation provides:
 * 
 * 1. Complete entity classes with JPA annotations
 * 2. Repository interfaces with custom queries
 * 3. Service classes with business logic and caching
 * 4. REST controllers with proper HTTP methods
 * 5. DTO classes for data transfer
 * 6. Request/response classes with validation
 * 7. Exception handling with custom exceptions
 * 8. Global exception handler for consistent error responses
 * 
 * Key Features Implemented:
 * - User registration and management
 * - Post creation and retrieval
 * - Like/unlike functionality
 * - Follow/unfollow functionality
 * - Feed generation
 * - Caching with Redis
 * - Input validation
 * - Error handling
 * - RESTful API design
 * 
 * This implementation is appropriate for an SDE 1 level interview,
 * demonstrating understanding of:
 * - Spring Boot framework
 * - JPA/Hibernate ORM
 * - RESTful API design
 * - Database relationships
 * - Caching strategies
 * - Exception handling
 * - Input validation
 * - Clean code practices
 */