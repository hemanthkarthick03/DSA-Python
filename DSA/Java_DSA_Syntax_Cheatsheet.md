# Java DSA Syntax Cheatsheet

A comprehensive guide to Java syntax for Data Structures and Algorithms, perfect for coding interviews and competitive programming.

---

## Table of Contents
1. [Basic Syntax](#basic-syntax)
2. [Arrays](#arrays)
3. [Strings](#strings)
4. [Collections Framework](#collections-framework)
5. [Common Data Structures](#common-data-structures)
6. [Sorting & Searching](#sorting--searching)
7. [Math & Utility Methods](#math--utility-methods)
8. [Input/Output](#inputoutput)
9. [Common Patterns](#common-patterns)
10. [Time & Space Complexity](#time--space-complexity)

---

## Basic Syntax

### Variable Declaration
```java
// Primitive types
int num = 10;
long bigNum = 1000000000L;
double decimal = 3.14;
boolean flag = true;
char character = 'A';

// Wrapper classes (for Collections)
Integer intObj = 10;
Long longObj = 1000000000L;
Double doubleObj = 3.14;
Boolean boolObj = true;
Character charObj = 'A';

// Constants
final int MAX_SIZE = 100;
static final int CONSTANT = 42;
```

### Control Structures
```java
// If-else
if (condition) {
    // code
} else if (anotherCondition) {
    // code
} else {
    // code
}

// Ternary operator
int result = condition ? valueIfTrue : valueIfFalse;

// Switch statement
switch (variable) {
    case 1:
        // code
        break;
    case 2:
        // code
        break;
    default:
        // code
}

// Enhanced switch (Java 14+)
int result = switch (variable) {
    case 1 -> 10;
    case 2 -> 20;
    default -> 0;
};
```

### Loops
```java
// For loop
for (int i = 0; i < n; i++) {
    // code
}

// Enhanced for loop (for-each)
for (int element : array) {
    // code
}

// While loop
while (condition) {
    // code
}

// Do-while loop
do {
    // code
} while (condition);

// Break and continue
for (int i = 0; i < n; i++) {
    if (condition) break;    // Exit loop
    if (condition) continue; // Skip iteration
}
```

---

## Arrays

### Array Declaration and Initialization
```java
// Declaration
int[] arr;
int arr[];  // Alternative syntax

// Initialization
int[] arr = new int[5];           // Size 5, default values (0)
int[] arr = {1, 2, 3, 4, 5};      // Direct initialization
int[] arr = new int[]{1, 2, 3};   // Alternative syntax

// 2D Arrays
int[][] matrix = new int[3][4];   // 3x4 matrix
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}};

// Jagged arrays
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[3];
jagged[2] = new int[1];
```

### Array Operations
```java
// Length
int length = arr.length;
int rows = matrix.length;
int cols = matrix[0].length;

// Access elements
int first = arr[0];
int last = arr[arr.length - 1];

// Iterate through array
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

// Enhanced for loop
for (int element : arr) {
    System.out.println(element);
}

// Copy arrays
int[] copy = arr.clone();
int[] copy = Arrays.copyOf(arr, arr.length);
int[] copy = Arrays.copyOfRange(arr, start, end);

// Fill array
Arrays.fill(arr, value);
Arrays.fill(arr, start, end, value);
```

### Array Utility Methods
```java
import java.util.Arrays;

// Sort
Arrays.sort(arr);                    // Ascending order
Arrays.sort(arr, start, end);        // Sort range
Arrays.sort(arr, Collections.reverseOrder()); // Descending (Integer[])

// Search
int index = Arrays.binarySearch(arr, target);

// Compare
boolean equal = Arrays.equals(arr1, arr2);

// Convert to string
String str = Arrays.toString(arr);
String str = Arrays.deepToString(matrix); // For 2D arrays

// Convert to List
List<Integer> list = Arrays.asList(arr); // For Integer[]
List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList()); // For int[]
```

---

## Strings

### String Declaration and Operations
```java
// Declaration
String str = "Hello";
String str = new String("Hello");

// Length
int length = str.length();

// Character access
char ch = str.charAt(index);

// Substring
String sub = str.substring(start);
String sub = str.substring(start, end); // end exclusive

// Concatenation
String result = str1 + str2;
String result = str1.concat(str2);

// Comparison
boolean equal = str1.equals(str2);
boolean equalIgnoreCase = str1.equalsIgnoreCase(str2);
int comparison = str1.compareTo(str2);

// Search
int index = str.indexOf(ch);
int index = str.indexOf(substring);
int lastIndex = str.lastIndexOf(ch);
boolean contains = str.contains(substring);
```

### String Manipulation
```java
// Case conversion
String upper = str.toUpperCase();
String lower = str.toLowerCase();

// Trim whitespace
String trimmed = str.trim();

// Replace
String replaced = str.replace(oldChar, newChar);
String replaced = str.replace(oldString, newString);
String replaced = str.replaceAll(regex, replacement);

// Split
String[] parts = str.split(delimiter);
String[] parts = str.split(regex, limit);

// Check properties
boolean isEmpty = str.isEmpty();
boolean isBlank = str.isBlank(); // Java 11+
boolean startsWith = str.startsWith(prefix);
boolean endsWith = str.endsWith(suffix);
```

### StringBuilder (Mutable Strings)
```java
// Creation
StringBuilder sb = new StringBuilder();
StringBuilder sb = new StringBuilder("initial");
StringBuilder sb = new StringBuilder(capacity);

// Operations
sb.append(str);           // Add to end
sb.insert(index, str);    // Insert at position
sb.delete(start, end);    // Delete range
sb.deleteCharAt(index);   // Delete single character
sb.reverse();             // Reverse string
sb.setCharAt(index, ch);  // Set character at index

// Convert to String
String result = sb.toString();

// Length and capacity
int length = sb.length();
int capacity = sb.capacity();
```

### Character Operations
```java
// Character class methods
boolean isDigit = Character.isDigit(ch);
boolean isLetter = Character.isLetter(ch);
boolean isLetterOrDigit = Character.isLetterOrDigit(ch);
boolean isUpperCase = Character.isUpperCase(ch);
boolean isLowerCase = Character.isLowerCase(ch);
boolean isWhitespace = Character.isWhitespace(ch);

char upper = Character.toUpperCase(ch);
char lower = Character.toLowerCase(ch);

// Convert between char and int
int ascii = (int) ch;
char character = (char) ascii;
int digit = Character.getNumericValue(ch); // '5' -> 5
```

---

## Collections Framework

### List Interface
```java
import java.util.*;

// ArrayList (Dynamic array)
List<Integer> list = new ArrayList<>();
List<Integer> list = new ArrayList<>(capacity);
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));

// LinkedList (Doubly linked list)
List<Integer> list = new LinkedList<>();

// Common operations
list.add(element);              // Add to end
list.add(index, element);       // Add at index
list.get(index);                // Get element
list.set(index, element);       // Set element
list.remove(index);             // Remove by index
list.remove(Object);            // Remove by value
list.size();                    // Get size
list.isEmpty();                 // Check if empty
list.contains(element);         // Check if contains
list.indexOf(element);          // Find index
list.clear();                   // Remove all elements

// Iteration
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}

for (Integer element : list) {
    System.out.println(element);
}

// Convert to array
Integer[] array = list.toArray(new Integer[0]);
```

### Set Interface
```java
// HashSet (Hash table)
Set<Integer> set = new HashSet<>();

// LinkedHashSet (Maintains insertion order)
Set<Integer> set = new LinkedHashSet<>();

// TreeSet (Sorted set)
Set<Integer> set = new TreeSet<>();

// Common operations
set.add(element);               // Add element
set.remove(element);            // Remove element
set.contains(element);          // Check if contains
set.size();                     // Get size
set.isEmpty();                  // Check if empty
set.clear();                    // Remove all elements

// Set operations
set1.addAll(set2);              // Union
set1.retainAll(set2);           // Intersection
set1.removeAll(set2);           // Difference
```

### Map Interface
```java
// HashMap (Hash table)
Map<String, Integer> map = new HashMap<>();

// LinkedHashMap (Maintains insertion order)
Map<String, Integer> map = new LinkedHashMap<>();

// TreeMap (Sorted by keys)
Map<String, Integer> map = new TreeMap<>();

// Common operations
map.put(key, value);            // Add/update entry
map.get(key);                   // Get value
map.getOrDefault(key, defaultValue); // Get with default
map.remove(key);                // Remove entry
map.containsKey(key);           // Check if key exists
map.containsValue(value);       // Check if value exists
map.size();                     // Get size
map.isEmpty();                  // Check if empty
map.clear();                    // Remove all entries

// Iteration
for (String key : map.keySet()) {
    System.out.println(key + ": " + map.get(key));
}

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// Update operations
map.putIfAbsent(key, value);    // Put if key doesn't exist
map.merge(key, value, (oldVal, newVal) -> oldVal + newVal); // Merge values
map.compute(key, (k, v) -> v == null ? 1 : v + 1); // Compute new value
```

---

## Common Data Structures

### Stack
```java
import java.util.Stack;

Stack<Integer> stack = new Stack<>();

// Operations
stack.push(element);            // Add to top
int top = stack.pop();          // Remove and return top
int top = stack.peek();         // Return top without removing
boolean empty = stack.isEmpty(); // Check if empty
int size = stack.size();        // Get size

// Using Deque as Stack (preferred)
Deque<Integer> stack = new ArrayDeque<>();
stack.push(element);
int top = stack.pop();
int top = stack.peek();
```

### Queue
```java
import java.util.*;

// LinkedList implementation
Queue<Integer> queue = new LinkedList<>();

// ArrayDeque implementation (preferred)
Queue<Integer> queue = new ArrayDeque<>();

// Operations
queue.offer(element);           // Add to rear
queue.add(element);             // Add to rear (throws exception if fails)
int front = queue.poll();       // Remove and return front (null if empty)
int front = queue.remove();     // Remove and return front (throws exception if empty)
int front = queue.peek();       // Return front without removing (null if empty)
int front = queue.element();    // Return front without removing (throws exception if empty)
boolean empty = queue.isEmpty(); // Check if empty
int size = queue.size();        // Get size
```

### Deque (Double-ended Queue)
```java
Deque<Integer> deque = new ArrayDeque<>();

// Add operations
deque.addFirst(element);        // Add to front
deque.addLast(element);         // Add to rear
deque.offerFirst(element);      // Add to front
deque.offerLast(element);       // Add to rear

// Remove operations
int first = deque.removeFirst(); // Remove from front
int last = deque.removeLast();   // Remove from rear
int first = deque.pollFirst();   // Remove from front (null if empty)
int last = deque.pollLast();     // Remove from rear (null if empty)

// Peek operations
int first = deque.peekFirst();   // Peek front
int last = deque.peekLast();     // Peek rear
```

### Priority Queue (Heap)
```java
// Min heap (default)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Max heap
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Custom comparator
PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a - b); // Min heap
PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a); // Max heap

// Operations
pq.offer(element);              // Add element
pq.add(element);                // Add element
int top = pq.poll();            // Remove and return top
int top = pq.peek();            // Return top without removing
boolean empty = pq.isEmpty();   // Check if empty
int size = pq.size();           // Get size

// For custom objects
class Node {
    int val, priority;
    Node(int val, int priority) {
        this.val = val;
        this.priority = priority;
    }
}

PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.priority - b.priority);
```

---

## Sorting & Searching

### Sorting
```java
import java.util.*;

// Arrays
int[] arr = {3, 1, 4, 1, 5};
Arrays.sort(arr);                           // Ascending
Arrays.sort(arr, start, end);               // Sort range

// For descending order (use Integer[] instead of int[])
Integer[] arr = {3, 1, 4, 1, 5};
Arrays.sort(arr, Collections.reverseOrder());

// Custom comparator
Arrays.sort(arr, (a, b) -> a - b);          // Ascending
Arrays.sort(arr, (a, b) -> b - a);          // Descending

// Lists
List<Integer> list = Arrays.asList(3, 1, 4, 1, 5);
Collections.sort(list);                     // Ascending
Collections.sort(list, Collections.reverseOrder()); // Descending
Collections.sort(list, (a, b) -> a - b);    // Custom comparator

// Sort by multiple criteria
class Person {
    String name;
    int age;
    // constructor, getters, setters
}

List<Person> people = new ArrayList<>();
// Sort by age, then by name
Collections.sort(people, (a, b) -> {
    if (a.age != b.age) return a.age - b.age;
    return a.name.compareTo(b.name);
});

// Using Comparator.comparing (Java 8+)
people.sort(Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName));
```

### Searching
```java
// Binary search (array must be sorted)
int[] arr = {1, 2, 3, 4, 5};
int index = Arrays.binarySearch(arr, target);
int index = Arrays.binarySearch(arr, start, end, target);

// List binary search
List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
int index = Collections.binarySearch(list, target);

// Custom binary search
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // Not found
}

// Lower bound (first element >= target)
public int lowerBound(int[] arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < target) left = mid + 1;
        else right = mid;
    }
    return left;
}

// Upper bound (first element > target)
public int upperBound(int[] arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return left;
}
```

---

## Math & Utility Methods

### Math Class
```java
// Basic operations
int abs = Math.abs(-5);                     // Absolute value
int max = Math.max(a, b);                   // Maximum
int min = Math.min(a, b);                   // Minimum
double pow = Math.pow(base, exponent);      // Power
double sqrt = Math.sqrt(number);            // Square root
double log = Math.log(number);              // Natural logarithm
double log10 = Math.log10(number);          // Base-10 logarithm

// Rounding
double ceil = Math.ceil(3.2);               // 4.0 (round up)
double floor = Math.floor(3.8);             // 3.0 (round down)
long round = Math.round(3.6);               // 4 (round to nearest)

// Trigonometric
double sin = Math.sin(angle);
double cos = Math.cos(angle);
double tan = Math.tan(angle);

// Constants
double pi = Math.PI;
double e = Math.E;

// Random
double random = Math.random();              // [0.0, 1.0)
int randomInt = (int)(Math.random() * n);   // [0, n)
```

### Common Math Operations
```java
// GCD (Greatest Common Divisor)
public int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// LCM (Least Common Multiple)
public int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

// Check if prime
public boolean isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

// Factorial
public long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Fibonacci
public int fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

// Power with modulo
public long modPow(long base, long exp, long mod) {
    long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        exp >>= 1;
        base = (base * base) % mod;
    }
    return result;
}
```

### Bit Operations
```java
// Basic bit operations
int and = a & b;                            // Bitwise AND
int or = a | b;                             // Bitwise OR
int xor = a ^ b;                            // Bitwise XOR
int not = ~a;                               // Bitwise NOT
int leftShift = a << n;                     // Left shift (multiply by 2^n)
int rightShift = a >> n;                    // Right shift (divide by 2^n)
int unsignedRightShift = a >>> n;           // Unsigned right shift

// Common bit tricks
boolean isEven = (n & 1) == 0;              // Check if even
boolean isPowerOfTwo = (n & (n - 1)) == 0;  // Check if power of 2
int setBit = n | (1 << i);                  // Set i-th bit
int clearBit = n & ~(1 << i);               // Clear i-th bit
int toggleBit = n ^ (1 << i);               // Toggle i-th bit
boolean getBit = (n & (1 << i)) != 0;       // Get i-th bit
int countBits = Integer.bitCount(n);        // Count set bits
int leadingZeros = Integer.numberOfLeadingZeros(n);
int trailingZeros = Integer.numberOfTrailingZeros(n);
```

---

## Input/Output

### Scanner (Input)
```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);

// Read different types
int n = sc.nextInt();
long l = sc.nextLong();
double d = sc.nextDouble();
String str = sc.next();                     // Single word
String line = sc.nextLine();                // Entire line
char ch = sc.next().charAt(0);              // Single character

// Read array
int[] arr = new int[n];
for (int i = 0; i < n; i++) {
    arr[i] = sc.nextInt();
}

// Check if input available
if (sc.hasNext()) {
    // Read next input
}

sc.close(); // Close scanner
```

### System.out (Output)
```java
// Basic output
System.out.print("Hello");                 // No newline
System.out.println("Hello");               // With newline
System.out.printf("Number: %d\n", num);    // Formatted output

// Formatted output
System.out.printf("%d %s %.2f\n", num, str, decimal);
System.out.printf("%5d\n", num);           // Right-aligned, width 5
System.out.printf("%-5d\n", num);          // Left-aligned, width 5
System.out.printf("%05d\n", num);          // Zero-padded, width 5

// Print array
System.out.println(Arrays.toString(arr));
System.out.println(Arrays.deepToString(matrix)); // For 2D arrays
```

### BufferedReader (Faster Input)
```java
import java.io.*;
import java.util.StringTokenizer;

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

// Read line
String line = br.readLine();

// Parse integers from line
StringTokenizer st = new StringTokenizer(line);
int a = Integer.parseInt(st.nextToken());
int b = Integer.parseInt(st.nextToken());

// Or split and parse
String[] parts = line.split(" ");
int[] arr = new int[parts.length];
for (int i = 0; i < parts.length; i++) {
    arr[i] = Integer.parseInt(parts[i]);
}

br.close();
```

---

## Common Patterns

### Two Pointers
```java
// Two pointers from ends
public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) return false;
        left++;
        right--;
    }
    return true;
}

// Two pointers same direction
public int removeDuplicates(int[] nums) {
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow]) {
            nums[++slow] = nums[fast];
        }
    }
    return slow + 1;
}
```

### Sliding Window
```java
// Fixed size window
public double findMaxAverage(int[] nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        sum += nums[i];
    }
    int maxSum = sum;
    for (int i = k; i < nums.length; i++) {
        sum = sum - nums[i - k] + nums[i];
        maxSum = Math.max(maxSum, sum);
    }
    return (double) maxSum / k;
}

// Variable size window
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        while (set.contains(s.charAt(right))) {
            set.remove(s.charAt(left++));
        }
        set.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

### Binary Search Template
```java
// Standard binary search
public int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

// Find leftmost position
public int findFirst(int[] nums, int target) {
    int left = 0, right = nums.length - 1, result = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            result = mid;
            right = mid - 1; // Continue searching left
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}
```

### DFS Template
```java
// Tree DFS
public void dfs(TreeNode root) {
    if (root == null) return;
    
    // Process current node
    System.out.println(root.val);
    
    // Recurse on children
    dfs(root.left);
    dfs(root.right);
}

// Graph DFS
public void dfs(int[][] graph, int node, boolean[] visited) {
    visited[node] = true;
    System.out.println(node);
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited);
        }
    }
}
```

### BFS Template
```java
// Tree BFS
public void bfs(TreeNode root) {
    if (root == null) return;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        TreeNode node = queue.poll();
        System.out.println(node.val);
        
        if (node.left != null) queue.offer(node.left);
        if (node.right != null) queue.offer(node.right);
    }
}

// Graph BFS
public void bfs(int[][] graph, int start) {
    boolean[] visited = new boolean[graph.length];
    Queue<Integer> queue = new LinkedList<>();
    
    queue.offer(start);
    visited[start] = true;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.println(node);
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.offer(neighbor);
            }
        }
    }
}
```

---

## Time & Space Complexity

### Common Time Complexities
```java
// O(1) - Constant
int first = arr[0];
map.get(key);

// O(log n) - Logarithmic
Arrays.binarySearch(arr, target);
TreeSet operations;

// O(n) - Linear
for (int i = 0; i < n; i++) { /* ... */ }
Linear search;

// O(n log n) - Linearithmic
Arrays.sort(arr);
Collections.sort(list);

// O(n²) - Quadratic
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        /* ... */
    }
}

// O(2^n) - Exponential
// Recursive fibonacci without memoization
public int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
```

### Space Complexity Examples
```java
// O(1) - Constant space
int sum = 0;
for (int num : arr) sum += num;

// O(n) - Linear space
int[] copy = new int[n];
List<Integer> list = new ArrayList<>();

// O(n) - Recursive call stack
public int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

---

## Quick Reference

### Common Operations Complexity
| Operation | ArrayList | LinkedList | HashMap | TreeMap | HashSet | TreeSet |
|-----------|-----------|------------|---------|---------|---------|---------|
| Add | O(1) | O(1) | O(1) | O(log n) | O(1) | O(log n) |
| Remove | O(n) | O(1) | O(1) | O(log n) | O(1) | O(log n) |
| Search | O(n) | O(n) | O(1) | O(log n) | O(1) | O(log n) |
| Access | O(1) | O(n) | O(1) | O(log n) | - | - |

### When to Use What
- **ArrayList**: Random access, frequent reads
- **LinkedList**: Frequent insertions/deletions at beginning/middle
- **HashMap**: Fast lookups, no ordering needed
- **TreeMap**: Sorted keys, range queries
- **HashSet**: Fast membership testing, no duplicates
- **TreeSet**: Sorted unique elements
- **PriorityQueue**: Always need min/max element
- **Stack/Deque**: LIFO operations, backtracking
- **Queue**: FIFO operations, BFS

This cheatsheet covers the essential Java syntax and patterns needed for DSA problems and coding interviews!