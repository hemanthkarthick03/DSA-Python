# 🚀 JavaScript & DSA Tricks Cheatsheet

## Table of Contents
1. [JavaScript Fundamentals](#javascript-fundamentals)
2. [Array Tricks](#array-tricks)
3. [String Manipulation](#string-manipulation)
4. [Object & Map Tricks](#object--map-tricks)
5. [Mathematical Operations](#mathematical-operations)
6. [Sorting Algorithms](#sorting-algorithms)
7. [Searching Algorithms](#searching-algorithms)
8. [Dynamic Programming](#dynamic-programming)
9. [Graph Algorithms](#graph-algorithms)
10. [Tree Algorithms](#tree-algorithms)
11. [Sliding Window Technique](#sliding-window-technique)
12. [Two Pointers Technique](#two-pointers-technique)
13. [Bit Manipulation](#bit-manipulation)
14. [Advanced JavaScript Patterns](#advanced-javascript-patterns)
15. [Performance Optimization](#performance-optimization)

---

## JavaScript Fundamentals

### Variable Declarations and Scope
```javascript
// Hoisting behavior
console.log(x); // undefined (not error)
var x = 5;

// Block scope with let/const
{
    let y = 10;
    const z = 20;
}
// console.log(y); // ReferenceError

// Temporal dead zone
console.log(a); // ReferenceError
let a = 5;
```

### Arrow Functions vs Regular Functions
```javascript
// Regular function
function regular() {
    console.log(this); // depends on call context
    console.log(arguments); // arguments object available
}

// Arrow function
const arrow = () => {
    console.log(this); // lexical this
    // console.log(arguments); // ReferenceError
}

// Arrow function with rest parameters
const arrowWithRest = (...args) => {
    console.log(args); // array of arguments
}
```

### Destructuring Tricks
```javascript
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first, second, rest); // 1, 2, [3, 4, 5]

// Swapping variables
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b); // 2, 1

// Object destructuring with renaming
const { name: userName, age: userAge } = { name: "John", age: 30 };

// Nested destructuring
const { address: { city } } = { address: { city: "NYC" } };

// Default values
const { x = 10, y = 20 } = { x: 5 };
console.log(x, y); // 5, 20
```

### Template Literals and Tagged Templates
```javascript
// Multi-line strings
const multiLine = `
    This is a
    multi-line
    string
`;

// Expression interpolation
const name = "World";
const greeting = `Hello, ${name}!`;

// Tagged templates
function highlight(strings, ...values) {
    return strings.reduce((result, string, i) => {
        return result + string + (values[i] ? `<mark>${values[i]}</mark>` : '');
    }, '');
}

const user = "John";
const age = 30;
const message = highlight`User ${user} is ${age} years old`;
```

---

## Array Tricks

### Array Creation and Initialization
```javascript
// Create array with specific length
const arr1 = new Array(5); // [empty × 5]
const arr2 = Array(5).fill(0); // [0, 0, 0, 0, 0]
const arr3 = [...Array(5)].map((_, i) => i); // [0, 1, 2, 3, 4]

// Create 2D array
const matrix = Array(3).fill().map(() => Array(3).fill(0));

// Range function
const range = (start, end) => [...Array(end - start)].map((_, i) => start + i);
console.log(range(1, 6)); // [1, 2, 3, 4, 5]
```

### Array Manipulation
```javascript
// Remove duplicates
const removeDuplicates = arr => [...new Set(arr)];
console.log(removeDuplicates([1, 2, 2, 3, 3, 4])); // [1, 2, 3, 4]

// Flatten array
const flatten = arr => arr.flat(Infinity);
const flattenRecursive = arr => arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flattenRecursive(val)) : acc.concat(val), []);

// Chunk array
const chunk = (arr, size) => 
    Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
        arr.slice(i * size, i * size + size)
    );
console.log(chunk([1, 2, 3, 4, 5, 6, 7], 3)); // [[1, 2, 3], [4, 5, 6], [7]]

// Shuffle array (Fisher-Yates)
const shuffle = arr => {
    const result = [...arr];
    for (let i = result.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
};
```### A
dvanced Array Methods
```javascript
// Find and filter combinations
const users = [
    { name: "John", age: 30, active: true },
    { name: "Jane", age: 25, active: false },
    { name: "Bob", age: 35, active: true }
];

// Find with default
const findUserOrDefault = (users, name) => 
    users.find(user => user.name === name) || { name: "Unknown", age: 0 };

// Group by property
const groupBy = (arr, key) => 
    arr.reduce((groups, item) => {
        const group = item[key];
        groups[group] = groups[group] || [];
        groups[group].push(item);
        return groups;
    }, {});

console.log(groupBy(users, 'active'));

// Count occurrences
const countBy = (arr, fn) => 
    arr.reduce((counts, item) => {
        const key = fn(item);
        counts[key] = (counts[key] || 0) + 1;
        return counts;
    }, {});

// Partition array
const partition = (arr, predicate) => 
    arr.reduce(([pass, fail], item) => 
        predicate(item) ? [[...pass, item], fail] : [pass, [...fail, item]], [[], []]);

const [active, inactive] = partition(users, user => user.active);
```

### Array Performance Tricks
```javascript
// Fast array copy
const fastCopy = arr => arr.slice();
const spreadCopy = arr => [...arr];

// Fast array clear
arr.length = 0; // Fastest way to clear array

// Check if array
const isArray = Array.isArray; // Faster than instanceof

// Fast array search
const binarySearch = (arr, target) => {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
};
```

---

## String Manipulation

### String Creation and Formatting
```javascript
// Pad strings
const padStart = str => str.padStart(10, '0'); // "0000000123"
const padEnd = str => str.padEnd(10, '-'); // "123-------"

// Capitalize words
const capitalize = str => str.charAt(0).toUpperCase() + str.slice(1);
const titleCase = str => str.split(' ').map(capitalize).join(' ');

// Reverse string
const reverse = str => str.split('').reverse().join('');
const reverseWords = str => str.split(' ').reverse().join(' ');

// Remove extra spaces
const cleanSpaces = str => str.replace(/\s+/g, ' ').trim();
```

### String Algorithms
```javascript
// Check palindrome
const isPalindrome = str => {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
};

// Longest common subsequence
const lcs = (str1, str2) => {
    const m = str1.length, n = str2.length;
    const dp = Array(m + 1).fill().map(() => Array(n + 1).fill(0));
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
};

// String matching (KMP algorithm)
const kmpSearch = (text, pattern) => {
    const buildLPS = pattern => {
        const lps = Array(pattern.length).fill(0);
        let len = 0, i = 1;
        
        while (i < pattern.length) {
            if (pattern[i] === pattern[len]) {
                lps[i++] = ++len;
            } else if (len) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        return lps;
    };
    
    const lps = buildLPS(pattern);
    const matches = [];
    let i = 0, j = 0;
    
    while (i < text.length) {
        if (text[i] === pattern[j]) {
            i++; j++;
        }
        
        if (j === pattern.length) {
            matches.push(i - j);
            j = lps[j - 1];
        } else if (i < text.length && text[i] !== pattern[j]) {
            j ? j = lps[j - 1] : i++;
        }
    }
    return matches;
};
```

---

## Object & Map Tricks

### Object Manipulation
```javascript
// Deep clone object
const deepClone = obj => {
    if (obj === null || typeof obj !== 'object') return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof Array) return obj.map(deepClone);
    
    const cloned = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloned[key] = deepClone(obj[key]);
        }
    }
    return cloned;
};

// Merge objects deeply
const deepMerge = (target, source) => {
    const result = { ...target };
    for (let key in source) {
        if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
            result[key] = deepMerge(result[key] || {}, source[key]);
        } else {
            result[key] = source[key];
        }
    }
    return result;
};

// Pick properties
const pick = (obj, keys) => 
    keys.reduce((result, key) => {
        if (key in obj) result[key] = obj[key];
        return result;
    }, {});

// Omit properties
const omit = (obj, keys) => 
    Object.keys(obj)
        .filter(key => !keys.includes(key))
        .reduce((result, key) => {
            result[key] = obj[key];
            return result;
        }, {});
```

### Map and Set Tricks
```javascript
// Frequency counter using Map
const frequencyCounter = arr => {
    const freq = new Map();
    arr.forEach(item => freq.set(item, (freq.get(item) || 0) + 1));
    return freq;
};

// LRU Cache implementation
class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map();
    }
    
    get(key) {
        if (this.cache.has(key)) {
            const value = this.cache.get(key);
            this.cache.delete(key);
            this.cache.set(key, value);
            return value;
        }
        return -1;
    }
    
    put(key, value) {
        if (this.cache.has(key)) {
            this.cache.delete(key);
        } else if (this.cache.size >= this.capacity) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
        this.cache.set(key, value);
    }
}

// WeakMap for private properties
const privateProps = new WeakMap();

class MyClass {
    constructor(value) {
        privateProps.set(this, { value });
    }
    
    getValue() {
        return privateProps.get(this).value;
    }
}
```

---

## Mathematical Operations

### Number Utilities
```javascript
// Check if number is prime
const isPrime = n => {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) return false;
    }
    return true;
};

// Generate primes using Sieve of Eratosthenes
const sieveOfEratosthenes = n => {
    const primes = Array(n + 1).fill(true);
    primes[0] = primes[1] = false;
    
    for (let i = 2; i * i <= n; i++) {
        if (primes[i]) {
            for (let j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }
    
    return primes.map((isPrime, num) => isPrime ? num : null)
                 .filter(num => num !== null);
};

// GCD and LCM
const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
const lcm = (a, b) => (a * b) / gcd(a, b);

// Fast exponentiation
const fastPow = (base, exp, mod = null) => {
    let result = 1;
    base = base % (mod || Number.MAX_SAFE_INTEGER);
    
    while (exp > 0) {
        if (exp % 2 === 1) {
            result = (result * base) % (mod || Number.MAX_SAFE_INTEGER);
        }
        exp = Math.floor(exp / 2);
        base = (base * base) % (mod || Number.MAX_SAFE_INTEGER);
    }
    return result;
};
```

### Random Number Generation
```javascript
// Random integer between min and max (inclusive)
const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

// Random float between min and max
const randomFloat = (min, max) => Math.random() * (max - min) + min;

// Weighted random selection
const weightedRandom = items => {
    const weights = items.map(item => item.weight);
    const totalWeight = weights.reduce((sum, weight) => sum + weight, 0);
    let random = Math.random() * totalWeight;
    
    for (let i = 0; i < items.length; i++) {
        random -= weights[i];
        if (random <= 0) return items[i];
    }
    return items[items.length - 1];
};
```

---

## Sorting Algorithms

### Quick Sort Implementation
```javascript
const quickSort = arr => {
    if (arr.length <= 1) return arr;
    
    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(x => x < pivot);
    const middle = arr.filter(x => x === pivot);
    const right = arr.filter(x => x > pivot);
    
    return [...quickSort(left), ...middle, ...quickSort(right)];
};

// In-place quick sort
const quickSortInPlace = (arr, low = 0, high = arr.length - 1) => {
    if (low < high) {
        const pi = partition(arr, low, high);
        quickSortInPlace(arr, low, pi - 1);
        quickSortInPlace(arr, pi + 1, high);
    }
    return arr;
};

const partition = (arr, low, high) => {
    const pivot = arr[high];
    let i = low - 1;
    
    for (let j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
};
```

### Merge Sort Implementation
```javascript
const mergeSort = arr => {
    if (arr.length <= 1) return arr;
    
    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    
    return merge(left, right);
};

const merge = (left, right) => {
    const result = [];
    let i = 0, j = 0;
    
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i++]);
        } else {
            result.push(right[j++]);
        }
    }
    
    return result.concat(left.slice(i)).concat(right.slice(j));
};
```

### Heap Sort Implementation
```javascript
const heapSort = arr => {
    const n = arr.length;
    
    // Build max heap
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // Extract elements from heap
    for (let i = n - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
    
    return arr;
};

const heapify = (arr, n, i) => {
    let largest = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
};
```

---

## Searching Algorithms

### Binary Search Variations
```javascript
// Standard binary search
const binarySearch = (arr, target) => {
    let left = 0, right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
};

// Find first occurrence
const findFirst = (arr, target) => {
    let left = 0, right = arr.length - 1, result = -1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            result = mid;
            right = mid - 1; // Continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
};

// Find last occurrence
const findLast = (arr, target) => {
    let left = 0, right = arr.length - 1, result = -1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            result = mid;
            left = mid + 1; // Continue searching right
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
};

// Search in rotated sorted array
const searchRotated = (arr, target) => {
    let left = 0, right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        
        if (arr[left] <= arr[mid]) { // Left half is sorted
            if (target >= arr[left] && target < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else { // Right half is sorted
            if (target > arr[mid] && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
};
```

---

## Dynamic Programming

### Classic DP Problems
```javascript
// Fibonacci with memoization
const fibonacci = (() => {
    const memo = {};
    return function fib(n) {
        if (n in memo) return memo[n];
        if (n <= 1) return n;
        return memo[n] = fib(n - 1) + fib(n - 2);
    };
})();

// Longest Increasing Subsequence
const lengthOfLIS = nums => {
    if (!nums.length) return 0;
    
    const dp = Array(nums.length).fill(1);
    let maxLength = 1;
    
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        maxLength = Math.max(maxLength, dp[i]);
    }
    
    return maxLength;
};

// Coin Change Problem
const coinChange = (coins, amount) => {
    const dp = Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (coin <= i) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
};

// 0/1 Knapsack Problem
const knapsack = (weights, values, capacity) => {
    const n = weights.length;
    const dp = Array(n + 1).fill().map(() => Array(capacity + 1).fill(0));
    
    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    
    return dp[n][capacity];
};
```

---

## Graph Algorithms

### Graph Representation and Traversal
```javascript
// Graph class with adjacency list
class Graph {
    constructor() {
        this.adjacencyList = {};
    }
    
    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }
    
    addEdge(v1, v2) {
        this.adjacencyList[v1].push(v2);
        this.adjacencyList[v2].push(v1);
    }
    
    // Depth-First Search
    dfs(start) {
        const result = [];
        const visited = {};
        const adjacencyList = this.adjacencyList;
        
        (function dfsHelper(vertex) {
            if (!vertex) return null;
            visited[vertex] = true;
            result.push(vertex);
            
            adjacencyList[vertex].forEach(neighbor => {
                if (!visited[neighbor]) {
                    return dfsHelper(neighbor);
                }
            });
        })(start);
        
        return result;
    }
    
    // Breadth-First Search
    bfs(start) {
        const queue = [start];
        const result = [];
        const visited = {};
        visited[start] = true;
        
        while (queue.length) {
            const vertex = queue.shift();
            result.push(vertex);
            
            this.adjacencyList[vertex].forEach(neighbor => {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push(neighbor);
                }
            });
        }
        
        return result;
    }
}

// Dijkstra's Algorithm
const dijkstra = (graph, start) => {
    const distances = {};
    const visited = new Set();
    const previous = {};
    const pq = new PriorityQueue();
    
    // Initialize distances
    for (let vertex in graph) {
        distances[vertex] = vertex === start ? 0 : Infinity;
        pq.enqueue(vertex, distances[vertex]);
    }
    
    while (!pq.isEmpty()) {
        const current = pq.dequeue().val;
        if (visited.has(current)) continue;
        visited.add(current);
        
        for (let neighbor in graph[current]) {
            const distance = distances[current] + graph[current][neighbor];
            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                previous[neighbor] = current;
                pq.enqueue(neighbor, distance);
            }
        }
    }
    
    return { distances, previous };
};

// Priority Queue for Dijkstra
class PriorityQueue {
    constructor() {
        this.values = [];
    }
    
    enqueue(val, priority) {
        this.values.push({ val, priority });
        this.sort();
    }
    
    dequeue() {
        return this.values.shift();
    }
    
    sort() {
        this.values.sort((a, b) => a.priority - b.priority);
    }
    
    isEmpty() {
        return this.values.length === 0;
    }
}
```

---

## Tree Algorithms

### Binary Tree Implementation
```javascript
class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }
    
    // Tree traversals
    inorderTraversal(node = this.root, result = []) {
        if (node) {
            this.inorderTraversal(node.left, result);
            result.push(node.val);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }
    
    preorderTraversal(node = this.root, result = []) {
        if (node) {
            result.push(node.val);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }
    
    postorderTraversal(node = this.root, result = []) {
        if (node) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.val);
        }
        return result;
    }
    
    levelOrderTraversal() {
        if (!this.root) return [];
        
        const result = [];
        const queue = [this.root];
        
        while (queue.length) {
            const levelSize = queue.length;
            const currentLevel = [];
            
            for (let i = 0; i < levelSize; i++) {
                const node = queue.shift();
                currentLevel.push(node.val);
                
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            
            result.push(currentLevel);
        }
        
        return result;
    }
    
    // Tree properties
    maxDepth(node = this.root) {
        if (!node) return 0;
        return 1 + Math.max(this.maxDepth(node.left), this.maxDepth(node.right));
    }
    
    isBalanced(node = this.root) {
        const checkBalance = node => {
            if (!node) return 0;
            
            const left = checkBalance(node.left);
            if (left === -1) return -1;
            
            const right = checkBalance(node.right);
            if (right === -1) return -1;
            
            if (Math.abs(left - right) > 1) return -1;
            return Math.max(left, right) + 1;
        };
        
        return checkBalance(node) !== -1;
    }
    
    // Lowest Common Ancestor
    lowestCommonAncestor(root, p, q) {
        if (!root || root === p || root === q) return root;
        
        const left = this.lowestCommonAncestor(root.left, p, q);
        const right = this.lowestCommonAncestor(root.right, p, q);
        
        if (left && right) return root;
        return left || right;
    }
}
```

### Binary Search Tree
```javascript
class BST extends BinaryTree {
    insert(val) {
        const newNode = new TreeNode(val);
        
        if (!this.root) {
            this.root = newNode;
            return this;
        }
        
        let current = this.root;
        while (true) {
            if (val === current.val) return undefined;
            
            if (val < current.val) {
                if (!current.left) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if (!current.right) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }
    
    find(val) {
        if (!this.root) return false;
        
        let current = this.root;
        while (current) {
            if (val === current.val) return current;
            if (val < current.val) current = current.left;
            else current = current.right;
        }
        return false;
    }
    
    delete(val) {
        this.root = this.deleteNode(this.root, val);
        return this;
    }
    
    deleteNode(node, val) {
        if (!node) return null;
        
        if (val < node.val) {
            node.left = this.deleteNode(node.left, val);
        } else if (val > node.val) {
            node.right = this.deleteNode(node.right, val);
        } else {
            // Node to delete found
            if (!node.left) return node.right;
            if (!node.right) return node.left;
            
            // Node has two children
            const minRight = this.findMin(node.right);
            node.val = minRight.val;
            node.right = this.deleteNode(node.right, minRight.val);
        }
        
        return node;
    }
    
    findMin(node) {
        while (node.left) node = node.left;
        return node;
    }
}
```

---

## Sliding Window Technique

### Fixed Size Window
```javascript
// Maximum sum of k consecutive elements
const maxSumSubarray = (arr, k) => {
    if (arr.length < k) return null;
    
    let windowSum = 0;
    // Calculate sum of first window
    for (let i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    let maxSum = windowSum;
    
    // Slide the window
    for (let i = k; i < arr.length; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];
        maxSum = Math.max(maxSum, windowSum);
    }
    
    return maxSum;
};

// Find all anagrams in string
const findAnagrams = (s, p) => {
    const result = [];
    const pCount = {};
    const windowCount = {};
    
    // Count characters in p
    for (const char of p) {
        pCount[char] = (pCount[char] || 0) + 1;
    }
    
    let left = 0, right = 0, matches = 0;
    
    while (right < s.length) {
        // Expand window
        const rightChar = s[right];
        if (rightChar in pCount) {
            windowCount[rightChar] = (windowCount[rightChar] || 0) + 1;
            if (windowCount[rightChar] === pCount[rightChar]) {
                matches++;
            }
        }
        
        // Contract window if needed
        if (right - left + 1 > p.length) {
            const leftChar = s[left];
            if (leftChar in pCount) {
                if (windowCount[leftChar] === pCount[leftChar]) {
                    matches--;
                }
                windowCount[leftChar]--;
            }
            left++;
        }
        
        // Check if window is valid
        if (matches === Object.keys(pCount).length) {
            result.push(left);
        }
        
        right++;
    }
    
    return result;
};
```

### Variable Size Window
```javascript
// Longest substring without repeating characters
const lengthOfLongestSubstring = s => {
    const seen = new Set();
    let left = 0, maxLength = 0;
    
    for (let right = 0; right < s.length; right++) {
        while (seen.has(s[right])) {
            seen.delete(s[left]);
            left++;
        }
        seen.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
};

// Minimum window substring
const minWindow = (s, t) => {
    const tCount = {};
    for (const char of t) {
        tCount[char] = (tCount[char] || 0) + 1;
    }
    
    let left = 0, minLen = Infinity, minStart = 0;
    let required = Object.keys(tCount).length;
    let formed = 0;
    const windowCount = {};
    
    for (let right = 0; right < s.length; right++) {
        const char = s[right];
        windowCount[char] = (windowCount[char] || 0) + 1;
        
        if (tCount[char] && windowCount[char] === tCount[char]) {
            formed++;
        }
        
        while (left <= right && formed === required) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }
            
            const leftChar = s[left];
            windowCount[leftChar]--;
            if (tCount[leftChar] && windowCount[leftChar] < tCount[leftChar]) {
                formed--;
            }
            left++;
        }
    }
    
    return minLen === Infinity ? "" : s.substring(minStart, minStart + minLen);
};
```

---

## Two Pointers Technique

### Array Two Pointers
```javascript
// Two sum in sorted array
const twoSum = (arr, target) => {
    let left = 0, right = arr.length - 1;
    
    while (left < right) {
        const sum = arr[left] + arr[right];
        if (sum === target) return [left, right];
        if (sum < target) left++;
        else right--;
    }
    
    return [-1, -1];
};

// Three sum
const threeSum = nums => {
    nums.sort((a, b) => a - b);
    const result = [];
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        let left = i + 1, right = nums.length - 1;
        
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
};

// Container with most water
const maxArea = height => {
    let left = 0, right = height.length - 1;
    let maxWater = 0;
    
    while (left < right) {
        const water = Math.min(height[left], height[right]) * (right - left);
        maxWater = Math.max(maxWater, water);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxWater;
};
```

### String Two Pointers
```javascript
// Valid palindrome
const isPalindrome = s => {
    const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let left = 0, right = cleaned.length - 1;
    
    while (left < right) {
        if (cleaned[left] !== cleaned[right]) return false;
        left++;
        right--;
    }
    
    return true;
};

// Reverse words in string
const reverseWords = s => {
    const words = s.trim().split(/\s+/);
    let left = 0, right = words.length - 1;
    
    while (left < right) {
        [words[left], words[right]] = [words[right], words[left]];
        left++;
        right--;
    }
    
    return words.join(' ');
};
```

---

## Bit Manipulation

### Basic Bit Operations
```javascript
// Check if number is power of 2
const isPowerOfTwo = n => n > 0 && (n & (n - 1)) === 0;

// Count set bits (1s) in binary representation
const countSetBits = n => {
    let count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
};

// Brian Kernighan's algorithm for counting set bits
const countSetBitsFast = n => {
    let count = 0;
    while (n) {
        n &= n - 1; // Remove rightmost set bit
        count++;
    }
    return count;
};

// Find single number (XOR approach)
const singleNumber = nums => nums.reduce((acc, num) => acc ^ num, 0);

// Swap two numbers without temp variable
const swapNumbers = (a, b) => {
    a ^= b;
    b ^= a;
    a ^= b;
    return [a, b];
};

// Get, set, clear, toggle bit
const getBit = (num, i) => (num & (1 << i)) !== 0;
const setBit = (num, i) => num | (1 << i);
const clearBit = (num, i) => num & ~(1 << i);
const toggleBit = (num, i) => num ^ (1 << i);
```

### Advanced Bit Manipulation
```javascript
// Find two non-repeating elements
const findTwoNonRepeating = nums => {
    const xor = nums.reduce((acc, num) => acc ^ num, 0);
    const rightmostSetBit = xor & -xor;
    
    let num1 = 0, num2 = 0;
    for (const num of nums) {
        if (num & rightmostSetBit) {
            num1 ^= num;
        } else {
            num2 ^= num;
        }
    }
    
    return [num1, num2];
};

// Generate all subsets using bit manipulation
const generateSubsets = nums => {
    const result = [];
    const n = nums.length;
    
    for (let i = 0; i < (1 << n); i++) {
        const subset = [];
        for (let j = 0; j < n; j++) {
            if (i & (1 << j)) {
                subset.push(nums[j]);
            }
        }
        result.push(subset);
    }
    
    return result;
};

// Reverse bits of 32-bit integer
const reverseBits = n => {
    let result = 0;
    for (let i = 0; i < 32; i++) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    return result >>> 0; // Unsigned right shift
};
```

---

## Advanced JavaScript Patterns

### Functional Programming Patterns
```javascript
// Curry function
const curry = fn => {
    return function curried(...args) {
        if (args.length >= fn.length) {
            return fn.apply(this, args);
        } else {
            return function(...args2) {
                return curried.apply(this, args.concat(args2));
            };
        }
    };
};

// Example usage
const add = (a, b, c) => a + b + c;
const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6

// Compose functions
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);

// Example
const addOne = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const composedFn = compose(square, double, addOne);
console.log(composedFn(3)); // ((3 + 1) * 2)^2 = 64

// Memoization
const memoize = fn => {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn.apply(this, args);
        cache.set(key, result);
        return result;
    };
};

// Debounce and Throttle
const debounce = (fn, delay) => {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn.apply(this, args), delay);
    };
};

const throttle = (fn, limit) => {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            fn.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
};
```

### Design Patterns
```javascript
// Singleton Pattern
const Singleton = (() => {
    let instance;
    
    function createInstance() {
        return {
            name: 'Singleton Instance',
            getValue: () => Math.random()
        };
    }
    
    return {
        getInstance: () => {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        }
    };
})();

// Observer Pattern
class EventEmitter {
    constructor() {
        this.events = {};
    }
    
    on(event, listener) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(listener);
    }
    
    emit(event, ...args) {
        if (this.events[event]) {
            this.events[event].forEach(listener => listener(...args));
        }
    }
    
    off(event, listenerToRemove) {
        if (this.events[event]) {
            this.events[event] = this.events[event].filter(
                listener => listener !== listenerToRemove
            );
        }
    }
}

// Factory Pattern
class ShapeFactory {
    static createShape(type, ...args) {
        switch (type.toLowerCase()) {
            case 'circle':
                return new Circle(...args);
            case 'rectangle':
                return new Rectangle(...args);
            case 'triangle':
                return new Triangle(...args);
            default:
                throw new Error(`Shape type ${type} not supported`);
        }
    }
}

// Strategy Pattern
class PaymentProcessor {
    constructor(strategy) {
        this.strategy = strategy;
    }
    
    processPayment(amount) {
        return this.strategy.process(amount);
    }
    
    setStrategy(strategy) {
        this.strategy = strategy;
    }
}

const creditCardStrategy = {
    process: amount => `Processing $${amount} via Credit Card`
};

const paypalStrategy = {
    process: amount => `Processing $${amount} via PayPal`
};
```

### Async Patterns
```javascript
// Promise utilities
const promiseAll = promises => {
    return new Promise((resolve, reject) => {
        const results = [];
        let completed = 0;
        
        if (promises.length === 0) {
            resolve(results);
            return;
        }
        
        promises.forEach((promise, index) => {
            Promise.resolve(promise)
                .then(result => {
                    results[index] = result;
                    completed++;
                    if (completed === promises.length) {
                        resolve(results);
                    }
                })
                .catch(reject);
        });
    });
};

const promiseAllSettled = promises => {
    return Promise.all(
        promises.map(promise =>
            Promise.resolve(promise)
                .then(value => ({ status: 'fulfilled', value }))
                .catch(reason => ({ status: 'rejected', reason }))
        )
    );
};

// Retry with exponential backoff
const retryWithBackoff = async (fn, maxRetries = 3, baseDelay = 1000) => {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === maxRetries - 1) throw error;
            
            const delay = baseDelay * Math.pow(2, i);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    }
};

// Async queue with concurrency limit
class AsyncQueue {
    constructor(concurrency = 1) {
        this.concurrency = concurrency;
        this.running = 0;
        this.queue = [];
    }
    
    async add(fn) {
        return new Promise((resolve, reject) => {
            this.queue.push({
                fn,
                resolve,
                reject
            });
            this.process();
        });
    }
    
    async process() {
        if (this.running >= this.concurrency || this.queue.length === 0) {
            return;
        }
        
        this.running++;
        const { fn, resolve, reject } = this.queue.shift();
        
        try {
            const result = await fn();
            resolve(result);
        } catch (error) {
            reject(error);
        } finally {
            this.running--;
            this.process();
        }
    }
}
```

---

## Performance Optimization

### Memory Management
```javascript
// Object pooling
class ObjectPool {
    constructor(createFn, resetFn, initialSize = 10) {
        this.createFn = createFn;
        this.resetFn = resetFn;
        this.pool = [];
        
        // Pre-populate pool
        for (let i = 0; i < initialSize; i++) {
            this.pool.push(this.createFn());
        }
    }
    
    acquire() {
        if (this.pool.length > 0) {
            return this.pool.pop();
        }
        return this.createFn();
    }
    
    release(obj) {
        this.resetFn(obj);
        this.pool.push(obj);
    }
}

// Weak references for caching
const cache = new WeakMap();

function expensiveOperation(obj) {
    if (cache.has(obj)) {
        return cache.get(obj);
    }
    
    const result = /* expensive computation */;
    cache.set(obj, result);
    return result;
}

// Lazy evaluation
class LazyValue {
    constructor(fn) {
        this.fn = fn;
        this.computed = false;
        this.value = undefined;
    }
    
    get() {
        if (!this.computed) {
            this.value = this.fn();
            this.computed = true;
        }
        return this.value;
    }
}
```

### Algorithm Optimization
```javascript
// Fast array operations
const fastRemove = (arr, index) => {
    // Swap with last element and pop (O(1) instead of O(n))
    if (index < arr.length - 1) {
        arr[index] = arr[arr.length - 1];
    }
    arr.pop();
    return arr;
};

// Efficient string building
const buildString = parts => {
    // Use array join instead of string concatenation
    return parts.join('');
};

// Fast object property access
const createAccessor = properties => {
    // Pre-compile property access
    const accessorFn = new Function('obj', `
        return {
            ${properties.map(prop => `${prop}: obj.${prop}`).join(', ')}
        };
    `);
    return accessorFn;
};

// Batch DOM operations
const batchDOMUpdates = operations => {
    const fragment = document.createDocumentFragment();
    operations.forEach(op => op(fragment));
    document.body.appendChild(fragment);
};

// Use requestAnimationFrame for smooth animations
const smoothAnimation = (duration, callback) => {
    const start = performance.now();
    
    const animate = currentTime => {
        const elapsed = currentTime - start;
        const progress = Math.min(elapsed / duration, 1);
        
        callback(progress);
        
        if (progress < 1) {
            requestAnimationFrame(animate);
        }
    };
    
    requestAnimationFrame(animate);
};
```

### Benchmarking and Profiling
```javascript
// Simple benchmark function
const benchmark = (fn, iterations = 1000000) => {
    const start = performance.now();
    
    for (let i = 0; i < iterations; i++) {
        fn();
    }
    
    const end = performance.now();
    return end - start;
};

// Memory usage tracking
const trackMemory = fn => {
    const before = performance.memory ? performance.memory.usedJSHeapSize : 0;
    const result = fn();
    const after = performance.memory ? performance.memory.usedJSHeapSize : 0;
    
    return {
        result,
        memoryUsed: after - before
    };
};

// Performance monitoring
class PerformanceMonitor {
    constructor() {
        this.metrics = new Map();
    }
    
    start(label) {
        this.metrics.set(label, performance.now());
    }
    
    end(label) {
        const start = this.metrics.get(label);
        if (start) {
            const duration = performance.now() - start;
            console.log(`${label}: ${duration.toFixed(2)}ms`);
            this.metrics.delete(label);
            return duration;
        }
    }
    
    measure(label, fn) {
        this.start(label);
        const result = fn();
        this.end(label);
        return result;
    }
}
```

---

## Common Interview Problems

### Array Problems
```javascript
// Rotate array
const rotateArray = (arr, k) => {
    k = k % arr.length;
    return arr.slice(-k).concat(arr.slice(0, -k));
};

// Find missing number
const findMissingNumber = arr => {
    const n = arr.length + 1;
    const expectedSum = (n * (n + 1)) / 2;
    const actualSum = arr.reduce((sum, num) => sum + num, 0);
    return expectedSum - actualSum;
};

// Product of array except self
const productExceptSelf = nums => {
    const result = Array(nums.length);
    
    // Left products
    result[0] = 1;
    for (let i = 1; i < nums.length; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }
    
    // Right products
    let right = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        result[i] *= right;
        right *= nums[i];
    }
    
    return result;
};
```

### String Problems
```javascript
// Group anagrams
const groupAnagrams = strs => {
    const groups = new Map();
    
    for (const str of strs) {
        const key = str.split('').sort().join('');
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key).push(str);
    }
    
    return Array.from(groups.values());
};

// Longest palindromic substring
const longestPalindrome = s => {
    let start = 0, maxLen = 1;
    
    const expandAroundCenter = (left, right) => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            const len = right - left + 1;
            if (len > maxLen) {
                start = left;
                maxLen = len;
            }
            left--;
            right++;
        }
    };
    
    for (let i = 0; i < s.length; i++) {
        expandAroundCenter(i, i); // Odd length palindromes
        expandAroundCenter(i, i + 1); // Even length palindromes
    }
    
    return s.substring(start, start + maxLen);
};
```

This comprehensive JavaScript and DSA cheatsheet covers fundamental concepts, advanced algorithms, and practical optimization techniques. Each section includes working code examples that you can use directly in interviews or projects. The guide progresses from basic JavaScript concepts to complex algorithmic problems, making it suitable for developers at all levels.