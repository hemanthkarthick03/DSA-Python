# 🍃 MongoDB Tricks & Cheatsheet

## Table of Contents
1. [Basic Operations](#basic-operations)
2. [Query Operations](#query-operations)
3. [Aggregation Framework](#aggregation-framework)
4. [Indexing Strategies](#indexing-strategies)
5. [Performance Optimization](#performance-optimization)
6. [Data Modeling Patterns](#data-modeling-patterns)
7. [Advanced Queries](#advanced-queries)
8. [Transactions](#transactions)
9. [Replication & Sharding](#replication--sharding)
10. [Monitoring & Debugging](#monitoring--debugging)
11. [Security Best Practices](#security-best-practices)
12. [Backup & Recovery](#backup--recovery)
13. [Python Integration](#python-integration)
14. [Useful Tricks & Tips](#useful-tricks--tips)

---

## Basic Operations

### Database Operations
```javascript
// Show all databases
show dbs

// Use/create database
use myDatabase

// Show current database
db

// Drop database
db.dropDatabase()

// Show collections
show collections

// Create collection
db.createCollection("users")

// Drop collection
db.users.drop()
```

### CRUD Operations

#### Create (Insert)
```javascript
// Insert one document
db.users.insertOne({
    name: "John Doe",
    email: "john@example.com",
    age: 30,
    createdAt: new Date()
})

// Insert multiple documents
db.users.insertMany([
    { name: "Alice", email: "alice@example.com", age: 25 },
    { name: "Bob", email: "bob@example.com", age: 35 },
    { name: "Charlie", email: "charlie@example.com", age: 28 }
])

// Insert with custom _id
db.users.insertOne({
    _id: "custom_id_123",
    name: "Custom User",
    email: "custom@example.com"
})
```

#### Read (Find)
```javascript
// Find all documents
db.users.find()

// Find with pretty formatting
db.users.find().pretty()

// Find one document
db.users.findOne()

// Find with condition
db.users.find({ age: 30 })

// Find with multiple conditions
db.users.find({ age: 30, name: "John Doe" })

// Find with projection (select specific fields)
db.users.find({}, { name: 1, email: 1, _id: 0 })

// Count documents
db.users.countDocuments()
db.users.countDocuments({ age: { $gte: 25 } })
```

#### Update
```javascript
// Update one document
db.users.updateOne(
    { name: "John Doe" },
    { $set: { age: 31, lastModified: new Date() } }
)

// Update multiple documents
db.users.updateMany(
    { age: { $lt: 30 } },
    { $set: { category: "young" } }
)

// Replace entire document
db.users.replaceOne(
    { name: "John Doe" },
    { name: "John Smith", email: "johnsmith@example.com", age: 32 }
)

// Upsert (update or insert)
db.users.updateOne(
    { email: "newuser@example.com" },
    { $set: { name: "New User", age: 25 } },
    { upsert: true }
)
```

#### Delete
```javascript
// Delete one document
db.users.deleteOne({ name: "John Doe" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 25 } })

// Delete all documents in collection
db.users.deleteMany({})
```

---

## Query Operations

### Comparison Operators
```javascript
// Equal
db.users.find({ age: 30 })

// Not equal
db.users.find({ age: { $ne: 30 } })

// Greater than
db.users.find({ age: { $gt: 25 } })

// Greater than or equal
db.users.find({ age: { $gte: 25 } })

// Less than
db.users.find({ age: { $lt: 35 } })

// Less than or equal
db.users.find({ age: { $lte: 35 } })

// In array
db.users.find({ age: { $in: [25, 30, 35] } })

// Not in array
db.users.find({ age: { $nin: [25, 30, 35] } })
```

### Logical Operators
```javascript
// AND (implicit)
db.users.find({ age: 30, name: "John" })

// AND (explicit)
db.users.find({ $and: [{ age: 30 }, { name: "John" }] })

// OR
db.users.find({ $or: [{ age: 30 }, { name: "John" }] })

// NOT
db.users.find({ age: { $not: { $gt: 30 } } })

// NOR
db.users.find({ $nor: [{ age: 30 }, { name: "John" }] })
```

### Element Operators
```javascript
// Field exists
db.users.find({ email: { $exists: true } })

// Field doesn't exist
db.users.find({ phone: { $exists: false } })

// Type check
db.users.find({ age: { $type: "number" } })
db.users.find({ age: { $type: 16 } }) // 16 = 32-bit integer
```

### Array Operators
```javascript
// Sample data with arrays
db.posts.insertMany([
    { title: "Post 1", tags: ["tech", "mongodb", "database"] },
    { title: "Post 2", tags: ["javascript", "nodejs"] },
    { title: "Post 3", tags: ["python", "mongodb"] }
])

// Match any element in array
db.posts.find({ tags: "mongodb" })

// Match all elements in array
db.posts.find({ tags: { $all: ["mongodb", "tech"] } })

// Array size
db.posts.find({ tags: { $size: 2 } })

// Element match
db.users.find({
    "addresses": {
        $elemMatch: {
            "city": "New York",
            "type": "home"
        }
    }
})
```

### Text Search
```javascript
// Create text index
db.posts.createIndex({ title: "text", content: "text" })

// Text search
db.posts.find({ $text: { $search: "mongodb database" } })

// Text search with score
db.posts.find(
    { $text: { $search: "mongodb" } },
    { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } })
```

### Regular Expressions
```javascript
// Case-insensitive search
db.users.find({ name: /john/i })

// Starts with
db.users.find({ name: /^John/ })

// Ends with
db.users.find({ email: /\.com$/ })

// Contains
db.users.find({ name: /doe/i })

// Using $regex operator
db.users.find({ name: { $regex: "john", $options: "i" } })
```

---

## Aggregation Framework

### Basic Aggregation Pipeline
```javascript
// Sample data
db.orders.insertMany([
    { customer: "Alice", amount: 100, status: "completed", date: new Date("2023-01-15") },
    { customer: "Bob", amount: 150, status: "pending", date: new Date("2023-01-20") },
    { customer: "Alice", amount: 200, status: "completed", date: new Date("2023-02-10") },
    { customer: "Charlie", amount: 75, status: "completed", date: new Date("2023-02-15") }
])

// Basic aggregation
db.orders.aggregate([
    { $match: { status: "completed" } },
    { $group: { _id: "$customer", totalAmount: { $sum: "$amount" } } },
    { $sort: { totalAmount: -1 } }
])
```

### Common Aggregation Stages

#### $match - Filter documents
```javascript
db.orders.aggregate([
    { $match: { amount: { $gte: 100 } } }
])
```

#### $group - Group and accumulate
```javascript
// Group by customer
db.orders.aggregate([
    {
        $group: {
            _id: "$customer",
            totalAmount: { $sum: "$amount" },
            avgAmount: { $avg: "$amount" },
            orderCount: { $sum: 1 },
            maxAmount: { $max: "$amount" },
            minAmount: { $min: "$amount" }
        }
    }
])

// Group by date (year-month)
db.orders.aggregate([
    {
        $group: {
            _id: {
                year: { $year: "$date" },
                month: { $month: "$date" }
            },
            totalSales: { $sum: "$amount" },
            orderCount: { $sum: 1 }
        }
    }
])
```

#### $project - Shape output documents
```javascript
db.orders.aggregate([
    {
        $project: {
            customer: 1,
            amount: 1,
            year: { $year: "$date" },
            month: { $month: "$date" },
            isLargeOrder: { $gte: ["$amount", 150] }
        }
    }
])
```

#### $sort - Sort documents
```javascript
db.orders.aggregate([
    { $sort: { amount: -1, date: 1 } }
])
```

#### $limit and $skip - Pagination
```javascript
db.orders.aggregate([
    { $sort: { date: -1 } },
    { $skip: 10 },
    { $limit: 5 }
])
```

#### $lookup - Join collections
```javascript
// Sample customers collection
db.customers.insertMany([
    { _id: "alice", name: "Alice Johnson", city: "New York" },
    { _id: "bob", name: "Bob Smith", city: "Los Angeles" },
    { _id: "charlie", name: "Charlie Brown", city: "Chicago" }
])

// Join orders with customers
db.orders.aggregate([
    {
        $lookup: {
            from: "customers",
            localField: "customer",
            foreignField: "_id",
            as: "customerInfo"
        }
    },
    {
        $unwind: "$customerInfo"
    },
    {
        $project: {
            amount: 1,
            status: 1,
            customerName: "$customerInfo.name",
            customerCity: "$customerInfo.city"
        }
    }
])
```

#### $unwind - Deconstruct arrays
```javascript
// Sample data with arrays
db.products.insertOne({
    name: "Laptop",
    categories: ["electronics", "computers", "portable"],
    specs: [
        { type: "RAM", value: "16GB" },
        { type: "Storage", value: "512GB SSD" }
    ]
})

// Unwind categories
db.products.aggregate([
    { $unwind: "$categories" },
    { $group: { _id: "$categories", count: { $sum: 1 } } }
])
```

### Advanced Aggregation Operators

#### Conditional Operations
```javascript
db.orders.aggregate([
    {
        $project: {
            customer: 1,
            amount: 1,
            category: {
                $switch: {
                    branches: [
                        { case: { $lt: ["$amount", 100] }, then: "Small" },
                        { case: { $lt: ["$amount", 200] }, then: "Medium" },
                        { case: { $gte: ["$amount", 200] }, then: "Large" }
                    ],
                    default: "Unknown"
                }
            }
        }
    }
])

// Using $cond
db.orders.aggregate([
    {
        $project: {
            customer: 1,
            amount: 1,
            size: {
                $cond: {
                    if: { $gte: ["$amount", 150] },
                    then: "Large",
                    else: "Small"
                }
            }
        }
    }
])
```

#### String Operations
```javascript
db.users.aggregate([
    {
        $project: {
            name: 1,
            email: 1,
            domain: {
                $arrayElemAt: [
                    { $split: ["$email", "@"] },
                    1
                ]
            },
            nameLength: { $strLenCP: "$name" },
            upperName: { $toUpper: "$name" },
            initials: {
                $concat: [
                    { $substr: ["$name", 0, 1] },
                    "."
                ]
            }
        }
    }
])
```

#### Date Operations
```javascript
db.orders.aggregate([
    {
        $project: {
            customer: 1,
            amount: 1,
            date: 1,
            year: { $year: "$date" },
            month: { $month: "$date" },
            dayOfWeek: { $dayOfWeek: "$date" },
            dayOfYear: { $dayOfYear: "$date" },
            quarter: {
                $ceil: { $divide: [{ $month: "$date" }, 3] }
            },
            ageInDays: {
                $divide: [
                    { $subtract: [new Date(), "$date"] },
                    1000 * 60 * 60 * 24
                ]
            }
        }
    }
])
```

---

## Indexing Strategies

### Basic Indexes
```javascript
// Create single field index
db.users.createIndex({ email: 1 })

// Create compound index
db.users.createIndex({ age: 1, name: 1 })

// Create descending index
db.users.createIndex({ createdAt: -1 })

// Create unique index
db.users.createIndex({ email: 1 }, { unique: true })

// Create sparse index (only indexes documents with the field)
db.users.createIndex({ phone: 1 }, { sparse: true })

// Create partial index (with condition)
db.users.createIndex(
    { age: 1 },
    { partialFilterExpression: { age: { $gte: 18 } } }
)
```

### Advanced Indexes
```javascript
// Text index for full-text search
db.posts.createIndex({ title: "text", content: "text" })

// Geospatial index
db.locations.createIndex({ coordinates: "2dsphere" })

// Multikey index (automatically created for arrays)
db.posts.createIndex({ tags: 1 })

// TTL index (Time To Live)
db.sessions.createIndex(
    { createdAt: 1 },
    { expireAfterSeconds: 3600 } // 1 hour
)

// Hashed index (for sharding)
db.users.createIndex({ _id: "hashed" })
```

### Index Management
```javascript
// List all indexes
db.users.getIndexes()

// Get index stats
db.users.aggregate([{ $indexStats: {} }])

// Drop index
db.users.dropIndex({ email: 1 })
db.users.dropIndex("email_1")

// Drop all indexes except _id
db.users.dropIndexes()

// Reindex collection
db.users.reIndex()

// Check if query uses index
db.users.find({ email: "john@example.com" }).explain("executionStats")
```

### Index Optimization Tips
```javascript
// Compound index order matters
// For query: { age: 25, name: "John", city: "NYC" }
// Good: { age: 1, name: 1, city: 1 }
// Bad: { city: 1, name: 1, age: 1 }

// ESR Rule: Equality, Sort, Range
db.users.createIndex({ status: 1, createdAt: -1, age: 1 })

// For query with sort
db.users.find({ status: "active" }).sort({ createdAt: -1 }).limit(10)
```

---

## Performance Optimization

### Query Optimization
```javascript
// Use explain() to analyze queries
db.users.find({ age: { $gte: 25 } }).explain("executionStats")

// Use hint() to force index usage
db.users.find({ age: 25 }).hint({ age: 1 })

// Use projection to limit returned fields
db.users.find({}, { name: 1, email: 1, _id: 0 })

// Use limit() to restrict results
db.users.find().sort({ createdAt: -1 }).limit(10)

// Avoid $where operator (uses JavaScript engine)
// Bad
db.users.find({ $where: "this.age > 25" })
// Good
db.users.find({ age: { $gt: 25 } })
```

### Aggregation Optimization
```javascript
// Put $match early in pipeline
db.orders.aggregate([
    { $match: { status: "completed" } }, // Filter early
    { $lookup: { /* ... */ } },
    { $group: { /* ... */ } }
])

// Use $project to reduce document size
db.orders.aggregate([
    { $match: { status: "completed" } },
    { $project: { customer: 1, amount: 1 } }, // Reduce fields early
    { $group: { _id: "$customer", total: { $sum: "$amount" } } }
])

// Use allowDiskUse for large datasets
db.orders.aggregate([
    { $group: { _id: "$customer", total: { $sum: "$amount" } } }
], { allowDiskUse: true })
```

### Connection and Resource Management
```javascript
// Set read preference
db.users.find().readPref("secondary")

// Use read concern
db.users.find().readConcern("majority")

// Use write concern
db.users.insertOne(
    { name: "John" },
    { writeConcern: { w: "majority", j: true } }
)

// Connection pooling (in application)
// maxPoolSize: 100
// minPoolSize: 5
// maxIdleTimeMS: 30000
```

---

## Data Modeling Patterns

### Embedding vs Referencing

#### Embedding (One-to-Few)
```javascript
// User with embedded addresses
{
    _id: ObjectId("..."),
    name: "John Doe",
    email: "john@example.com",
    addresses: [
        {
            type: "home",
            street: "123 Main St",
            city: "New York",
            zipCode: "10001"
        },
        {
            type: "work",
            street: "456 Business Ave",
            city: "New York",
            zipCode: "10002"
        }
    ]
}
```

#### Referencing (One-to-Many)
```javascript
// User document
{
    _id: ObjectId("user1"),
    name: "John Doe",
    email: "john@example.com"
}

// Order documents
{
    _id: ObjectId("order1"),
    userId: ObjectId("user1"),
    amount: 100,
    items: [...]
}
```

### Schema Design Patterns

#### Polymorphic Pattern
```javascript
// Different types of products in same collection
{
    _id: ObjectId("..."),
    type: "book",
    title: "MongoDB Guide",
    author: "John Smith",
    isbn: "978-1234567890"
}

{
    _id: ObjectId("..."),
    type: "electronics",
    name: "Laptop",
    brand: "TechCorp",
    model: "X1000"
}
```

#### Attribute Pattern
```javascript
// Flexible attributes for products
{
    _id: ObjectId("..."),
    name: "Laptop",
    attributes: [
        { key: "RAM", value: "16GB", type: "string" },
        { key: "Storage", value: "512GB", type: "string" },
        { key: "Weight", value: 2.5, type: "number", unit: "kg" }
    ]
}

// Index on attributes for flexible queries
db.products.createIndex({ "attributes.key": 1, "attributes.value": 1 })
```

#### Bucket Pattern (Time Series)
```javascript
// IoT sensor data bucketed by hour
{
    _id: ObjectId("..."),
    sensorId: "sensor123",
    timestamp: ISODate("2023-01-01T10:00:00Z"),
    measurements: [
        { time: ISODate("2023-01-01T10:00:00Z"), temperature: 22.5 },
        { time: ISODate("2023-01-01T10:01:00Z"), temperature: 22.7 },
        { time: ISODate("2023-01-01T10:02:00Z"), temperature: 22.3 }
        // ... up to 60 measurements per hour
    ]
}
```

#### Subset Pattern
```javascript
// Movie with most accessed reviews embedded
{
    _id: ObjectId("..."),
    title: "Great Movie",
    year: 2023,
    topReviews: [
        { author: "Critic1", rating: 5, text: "Amazing!" },
        { author: "Critic2", rating: 4, text: "Very good" }
        // Only top 10 reviews embedded
    ],
    reviewCount: 1500,
    avgRating: 4.2
}

// Full reviews in separate collection
// db.reviews with movieId reference
```

---

## Advanced Queries

### Complex Aggregations
```javascript
// Multi-stage aggregation with multiple operations
db.sales.aggregate([
    // Stage 1: Match recent sales
    {
        $match: {
            date: { $gte: new Date("2023-01-01") },
            status: "completed"
        }
    },
    
    // Stage 2: Add computed fields
    {
        $addFields: {
            month: { $month: "$date" },
            quarter: { $ceil: { $divide: [{ $month: "$date" }, 3] } }
        }
    },
    
    // Stage 3: Group by product and quarter
    {
        $group: {
            _id: {
                product: "$product",
                quarter: "$quarter"
            },
            totalSales: { $sum: "$amount" },
            avgSale: { $avg: "$amount" },
            salesCount: { $sum: 1 },
            maxSale: { $max: "$amount" }
        }
    },
    
    // Stage 4: Sort by total sales
    { $sort: { totalSales: -1 } },
    
    // Stage 5: Group by product to get quarterly data
    {
        $group: {
            _id: "$_id.product",
            quarterlyData: {
                $push: {
                    quarter: "$_id.quarter",
                    totalSales: "$totalSales",
                    avgSale: "$avgSale",
                    salesCount: "$salesCount"
                }
            },
            yearlyTotal: { $sum: "$totalSales" }
        }
    },
    
    // Stage 6: Final projection
    {
        $project: {
            product: "$_id",
            yearlyTotal: 1,
            quarterlyData: 1,
            _id: 0
        }
    }
])
```

### Window Functions (MongoDB 5.0+)
```javascript
// Running totals and rankings
db.sales.aggregate([
    {
        $setWindowFields: {
            partitionBy: "$product",
            sortBy: { date: 1 },
            output: {
                runningTotal: {
                    $sum: "$amount",
                    window: { documents: ["unbounded", "current"] }
                },
                rank: { $rank: {} },
                movingAvg: {
                    $avg: "$amount",
                    window: { documents: [-2, 0] } // 3-period moving average
                }
            }
        }
    }
])
```

### Faceted Search
```javascript
// Multiple aggregations in single query
db.products.aggregate([
    {
        $facet: {
            // Price ranges
            priceRanges: [
                {
                    $bucket: {
                        groupBy: "$price",
                        boundaries: [0, 50, 100, 200, 500],
                        default: "Other",
                        output: { count: { $sum: 1 } }
                    }
                }
            ],
            
            // Categories
            categories: [
                { $group: { _id: "$category", count: { $sum: 1 } } },
                { $sort: { count: -1 } }
            ],
            
            // Average price
            avgPrice: [
                { $group: { _id: null, avgPrice: { $avg: "$price" } } }
            ]
        }
    }
])
```

### Graph Operations
```javascript
// Find connections (friends of friends)
db.users.aggregate([
    { $match: { _id: ObjectId("user1") } },
    {
        $graphLookup: {
            from: "users",
            startWith: "$friends",
            connectFromField: "friends",
            connectToField: "_id",
            as: "network",
            maxDepth: 2
        }
    }
])
```

---

## Transactions

### Single Document Transactions (Atomic)
```javascript
// Atomic operations on single document
db.accounts.updateOne(
    { _id: "account1" },
    {
        $inc: { balance: -100 },
        $push: {
            transactions: {
                type: "debit",
                amount: 100,
                timestamp: new Date()
            }
        }
    }
)
```

### Multi-Document Transactions
```javascript
// Start session
const session = db.getMongo().startSession()

try {
    session.startTransaction()
    
    // Transfer money between accounts
    db.accounts.updateOne(
        { _id: "account1" },
        { $inc: { balance: -100 } },
        { session: session }
    )
    
    db.accounts.updateOne(
        { _id: "account2" },
        { $inc: { balance: 100 } },
        { session: session }
    )
    
    // Log transaction
    db.transactions.insertOne({
        from: "account1",
        to: "account2",
        amount: 100,
        timestamp: new Date()
    }, { session: session })
    
    session.commitTransaction()
} catch (error) {
    session.abortTransaction()
    throw error
} finally {
    session.endSession()
}
```

### Transaction Best Practices
```javascript
// Use retryable writes
db.accounts.updateOne(
    { _id: "account1" },
    { $inc: { balance: -100 } },
    { retryWrites: true }
)

// Set transaction options
session.startTransaction({
    readConcern: { level: "majority" },
    writeConcern: { w: "majority" },
    maxTimeMS: 5000
})
```

---

## Replication & Sharding

### Replica Set Operations
```javascript
// Check replica set status
rs.status()

// Check replica set configuration
rs.conf()

// Add member to replica set
rs.add("mongodb3.example.com:27017")

// Remove member
rs.remove("mongodb3.example.com:27017")

// Step down primary
rs.stepDown()

// Check if current node is master
db.isMaster()
```

### Read Preferences
```javascript
// Read from primary only (default)
db.users.find().readPref("primary")

// Read from secondary if available
db.users.find().readPref("primaryPreferred")

// Read from secondary only
db.users.find().readPref("secondary")

// Read from secondary if available, otherwise primary
db.users.find().readPref("secondaryPreferred")

// Read from nearest member
db.users.find().readPref("nearest")
```

### Sharding
```javascript
// Enable sharding on database
sh.enableSharding("myDatabase")

// Shard collection
sh.shardCollection("myDatabase.users", { userId: 1 })

// Check shard status
sh.status()

// Check collection sharding info
db.users.getShardDistribution()

// Add shard
sh.addShard("shard1/mongodb1.example.com:27017")
```

---

## Monitoring & Debugging

### Database Statistics
```javascript
// Database stats
db.stats()

// Collection stats
db.users.stats()

// Index stats
db.users.aggregate([{ $indexStats: {} }])

// Current operations
db.currentOp()

// Kill operation
db.killOp(123456)
```

### Profiling
```javascript
// Enable profiling for slow operations (>100ms)
db.setProfilingLevel(1, { slowms: 100 })

// Enable profiling for all operations
db.setProfilingLevel(2)

// Disable profiling
db.setProfilingLevel(0)

// Check profiling status
db.getProfilingStatus()

// Query profiler collection
db.system.profile.find().limit(5).sort({ ts: -1 }).pretty()
```

### Performance Monitoring
```javascript
// Server status
db.serverStatus()

// Replica set status
db.runCommand("replSetGetStatus")

// Check locks
db.runCommand("serverStatus").locks

// Check connections
db.runCommand("serverStatus").connections

// Check memory usage
db.runCommand("serverStatus").mem
```

### Diagnostic Commands
```javascript
// Validate collection
db.users.validate()

// Check collection size
db.users.totalSize()

// Get collection storage stats
db.users.storageSize()

// Compact collection (reclaim space)
db.runCommand({ compact: "users" })

// Repair database
db.repairDatabase()
```

---

## Security Best Practices

### Authentication
```javascript
// Create admin user
use admin
db.createUser({
    user: "admin",
    pwd: "securePassword",
    roles: ["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"]
})

// Create database-specific user
use myDatabase
db.createUser({
    user: "appUser",
    pwd: "appPassword",
    roles: ["readWrite"]
})

// Create read-only user
db.createUser({
    user: "readOnlyUser",
    pwd: "readPassword",
    roles: ["read"]
})
```

### Authorization
```javascript
// Custom role
db.createRole({
    role: "customRole",
    privileges: [
        {
            resource: { db: "myDatabase", collection: "users" },
            actions: ["find", "insert", "update"]
        }
    ],
    roles: []
})

// Grant role to user
db.grantRolesToUser("appUser", ["customRole"])

// Revoke role from user
db.revokeRolesFromUser("appUser", ["customRole"])
```

### Security Configuration
```javascript
// Enable authentication in mongod.conf
/*
security:
  authorization: enabled
  keyFile: /path/to/keyfile
*/

// SSL/TLS configuration
/*
net:
  ssl:
    mode: requireSSL
    PEMKeyFile: /path/to/server.pem
    CAFile: /path/to/ca.pem
*/
```

---

## Backup & Recovery

### Backup Strategies
```bash
# mongodump - Logical backup
mongodump --host localhost:27017 --db myDatabase --out /backup/path

# mongodump with authentication
mongodump --host localhost:27017 --username admin --password --authenticationDatabase admin --db myDatabase --out /backup/path

# Backup specific collection
mongodump --host localhost:27017 --db myDatabase --collection users --out /backup/path

# Compressed backup
mongodump --host localhost:27017 --db myDatabase --gzip --out /backup/path
```

### Restore Operations
```bash
# mongorestore - Restore from backup
mongorestore --host localhost:27017 --db myDatabase /backup/path/myDatabase

# Restore with authentication
mongorestore --host localhost:27017 --username admin --password --authenticationDatabase admin --db myDatabase /backup/path/myDatabase

# Restore specific collection
mongorestore --host localhost:27017 --db myDatabase --collection users /backup/path/myDatabase/users.bson

# Restore compressed backup
mongorestore --host localhost:27017 --gzip --db myDatabase /backup/path/myDatabase
```

### Point-in-Time Recovery
```bash
# Enable oplog
mongod --replSet rs0 --oplogSize 1024

# Backup with oplog
mongodump --host localhost:27017 --oplog --out /backup/path

# Restore to specific point in time
mongorestore --host localhost:27017 --oplogReplay --oplogLimit 1609459200:1 /backup/path
```

---

## Python Integration

### PyMongo Basics
```python
from pymongo import MongoClient
from datetime import datetime
import pymongo

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['myDatabase']
collection = db['users']

# Insert document
user = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "created_at": datetime.now()
}
result = collection.insert_one(user)
print(f"Inserted document with id: {result.inserted_id}")

# Find documents
users = collection.find({"age": {"$gte": 25}})
for user in users:
    print(user)

# Update document
collection.update_one(
    {"email": "john@example.com"},
    {"$set": {"age": 31, "last_modified": datetime.now()}}
)

# Delete document
collection.delete_one({"email": "john@example.com"})
```

### Advanced PyMongo Operations
```python
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import BulkWriteError
import pymongo

client = MongoClient('mongodb://localhost:27017/')
db = client['myDatabase']

# Bulk operations
from pymongo import InsertOne, UpdateOne, DeleteOne

bulk_ops = [
    InsertOne({"name": "Alice", "age": 25}),
    UpdateOne({"name": "Bob"}, {"$set": {"age": 30}}),
    DeleteOne({"name": "Charlie"})
]

try:
    result = db.users.bulk_write(bulk_ops)
    print(f"Inserted: {result.inserted_count}")
    print(f"Modified: {result.modified_count}")
    print(f"Deleted: {result.deleted_count}")
except BulkWriteError as bwe:
    print(f"Bulk write error: {bwe.details}")

# Aggregation pipeline
pipeline = [
    {"$match": {"age": {"$gte": 25}}},
    {"$group": {"_id": "$department", "avg_age": {"$avg": "$age"}}},
    {"$sort": {"avg_age": -1}}
]

results = list(db.users.aggregate(pipeline))
for result in results:
    print(result)

# Create index
db.users.create_index([("email", ASCENDING)], unique=True)
db.users.create_index([("age", ASCENDING), ("name", ASCENDING)])

# Text search
db.posts.create_index([("title", "text"), ("content", "text")])
results = db.posts.find({"$text": {"$search": "mongodb python"}})
```

### Connection Management
```python
from pymongo import MongoClient
from pymongo.read_preferences import ReadPreference

# Connection with options
client = MongoClient(
    'mongodb://username:password@localhost:27017/',
    maxPoolSize=50,
    minPoolSize=5,
    maxIdleTimeMS=30000,
    serverSelectionTimeoutMS=5000,
    socketTimeoutMS=20000
)

# Read preferences
db = client.myDatabase
collection = db.users.with_options(
    read_preference=ReadPreference.SECONDARY_PREFERRED
)

# Write concern
from pymongo.write_concern import WriteConcern

collection = db.users.with_options(
    write_concern=WriteConcern(w="majority", j=True)
)
```

### Transactions in Python
```python
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

client = MongoClient('mongodb://localhost:27017/')
db = client.myDatabase

def transfer_money(from_account, to_account, amount):
    with client.start_session() as session:
        with session.start_transaction():
            try:
                # Debit from source account
                result = db.accounts.update_one(
                    {"_id": from_account, "balance": {"$gte": amount}},
                    {"$inc": {"balance": -amount}},
                    session=session
                )
                
                if result.modified_count == 0:
                    raise ValueError("Insufficient funds")
                
                # Credit to destination account
                db.accounts.update_one(
                    {"_id": to_account},
                    {"$inc": {"balance": amount}},
                    session=session
                )
                
                # Log transaction
                db.transactions.insert_one({
                    "from": from_account,
                    "to": to_account,
                    "amount": amount,
                    "timestamp": datetime.now()
                }, session=session)
                
                print("Transfer completed successfully")
                
            except Exception as e:
                print(f"Transfer failed: {e}")
                raise

# Usage
transfer_money("account1", "account2", 100)
```

---

## Useful Tricks & Tips

### Query Optimization Tricks
```javascript
// Use covered queries (query + projection covered by index)
db.users.createIndex({ email: 1, name: 1, age: 1 })
db.users.find({ email: "john@example.com" }, { name: 1, age: 1, _id: 0 })

// Use $exists: false to find missing fields efficiently
db.users.find({ phone: { $exists: false } })

// Use $type to query by data type
db.users.find({ age: { $type: "number" } })

// Efficient pagination with range queries
// Instead of skip/limit for large offsets
db.users.find({ _id: { $gt: ObjectId("last_seen_id") } }).limit(10)
```

### Data Manipulation Tricks
```javascript
// Convert string to number
db.users.updateMany(
    { age: { $type: "string" } },
    [{ $set: { age: { $toInt: "$age" } } }]
)

// Add field based on existing field
db.users.updateMany(
    {},
    [{ $set: { fullName: { $concat: ["$firstName", " ", "$lastName"] } } }]
)

// Remove field from all documents
db.users.updateMany({}, { $unset: { oldField: "" } })

// Rename field
db.users.updateMany({}, { $rename: { oldName: "newName" } })
```

### Array Manipulation
```javascript
// Add to array if not exists
db.users.updateOne(
    { _id: ObjectId("...") },
    { $addToSet: { tags: "new-tag" } }
)

// Remove from array
db.users.updateOne(
    { _id: ObjectId("...") },
    { $pull: { tags: "old-tag" } }
)

// Update array element
db.users.updateOne(
    { _id: ObjectId("..."), "addresses.type": "home" },
    { $set: { "addresses.$.city": "New York" } }
)

// Update all array elements
db.users.updateOne(
    { _id: ObjectId("...") },
    { $set: { "addresses.$[].country": "USA" } }
)

// Update array elements with condition
db.users.updateOne(
    { _id: ObjectId("...") },
    { $set: { "addresses.$[elem].verified": true } },
    { arrayFilters: [{ "elem.type": "home" }] }
)
```

### Aggregation Tricks
```javascript
// Random sample
db.users.aggregate([{ $sample: { size: 10 } }])

// Convert array to object
db.products.aggregate([
    {
        $addFields: {
            attributesObj: {
                $arrayToObject: {
                    $map: {
                        input: "$attributes",
                        as: "attr",
                        in: { k: "$$attr.key", v: "$$attr.value" }
                    }
                }
            }
        }
    }
])

// Flatten nested arrays
db.posts.aggregate([
    { $unwind: "$comments" },
    { $unwind: "$comments.replies" },
    { $group: { _id: "$_id", allReplies: { $push: "$comments.replies" } } }
])

// Calculate percentiles
db.sales.aggregate([
    {
        $group: {
            _id: null,
            amounts: { $push: "$amount" }
        }
    },
    {
        $addFields: {
            p50: { $arrayElemAt: ["$amounts", { $floor: { $multiply: [0.5, { $size: "$amounts" }] } }] },
            p90: { $arrayElemAt: ["$amounts", { $floor: { $multiply: [0.9, { $size: "$amounts" }] } }] }
        }
    }
])
```

### Performance Tips
```javascript
// Use hint() to force index usage
db.users.find({ age: 25, name: "John" }).hint({ age: 1, name: 1 })

// Use allowDiskUse for large aggregations
db.orders.aggregate([
    { $group: { _id: "$customer", total: { $sum: "$amount" } } }
], { allowDiskUse: true })

// Use cursor.batchSize() for large result sets
db.users.find().batchSize(100)

// Use cursor.noCursorTimeout() for long-running queries
db.users.find().noCursorTimeout()
```

### Debugging and Monitoring
```javascript
// Check query execution plan
db.users.find({ email: "john@example.com" }).explain("executionStats")

// Monitor current operations
db.currentOp({ "active": true, "secs_running": { "$gt": 5 } })

// Check index usage
db.users.aggregate([
    { $indexStats: {} },
    { $sort: { "accesses.ops": -1 } }
])

// Profile slow queries
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find({ "millis": { $gt: 100 } }).sort({ ts: -1 }).limit(5)
```

### Useful Administrative Commands
```javascript
// Check database size
db.stats(1024*1024) // Size in MB

// Check collection size
db.users.stats(1024*1024) // Size in MB

// Compact collection
db.runCommand({ compact: "users", force: true })

// Get server build info
db.runCommand("buildInfo")

// Check feature compatibility version
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })
```

---

## MongoDB Compass Tips

### Visual Query Builder
- Use the query bar for complex filters
- Drag and drop to build aggregation pipelines
- Export queries to various programming languages
- Use schema analysis to understand data distribution

### Performance Insights
- Real-time performance metrics
- Query performance advisor
- Index recommendations
- Connection monitoring

---

## Best Practices Summary

### Schema Design
- Embed for one-to-few relationships
- Reference for one-to-many relationships
- Consider query patterns when designing schema
- Use appropriate data types
- Avoid deep nesting (>3 levels)

### Indexing
- Create indexes for frequently queried fields
- Use compound indexes for multi-field queries
- Follow ESR rule: Equality, Sort, Range
- Monitor index usage and remove unused indexes
- Use partial indexes for sparse data

### Queries
- Use projection to limit returned fields
- Put selective filters early in aggregation pipelines
- Use $match before $lookup when possible
- Avoid $where operator
- Use explain() to analyze query performance

### Operations
- Use bulk operations for multiple writes
- Implement proper error handling
- Use transactions for multi-document consistency
- Monitor slow queries and optimize
- Regular backup and test recovery procedures

This comprehensive MongoDB cheatsheet covers everything from basic operations to advanced optimization techniques. Keep it handy for quick reference during development and administration tasks!