# 🐍 Python Coding Tricks for Google-Level DSA Interviews

**Master Python idioms and shortcuts to solve problems faster and cleaner**

---

## Table of Contents
1. [List Comprehensions & Generators](#list-comprehensions--generators)
2. [String Manipulation Tricks](#string-manipulation-tricks)
3. [Dictionary & Set Tricks](#dictionary--set-tricks)
4. [Math & Number Tricks](#math--number-tricks)
5. [Slicing & Indexing Magic](#slicing--indexing-magic)
6. [Built-in Functions Mastery](#built-in-functions-mastery)
7. [Lambda & Functional Programming](#lambda--functional-programming)
8. [Collections Module Secrets](#collections-module-secrets)
9. [Itertools Power Moves](#itertools-power-moves)
10. [Bit Manipulation Shortcuts](#bit-manipulation-shortcuts)
11. [Common Interview Patterns](#common-interview-patterns)
12. [Time & Space Optimizations](#time--space-optimizations)

---

## List Comprehensions & Generators

### Basic List Comprehension
```python
# Instead of:
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * i)

# Do this:
result = [i * i for i in range(10) if i % 2 == 0]
```

### Nested List Comprehension
```python
# 2D matrix creation
matrix = [[0] * n for _ in range(m)]

# NOT: matrix = [[0] * n] * m  # This creates shallow copies!

# Flatten 2D list
flattened = [num for row in matrix for num in row]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
```

### Generator Expressions (Memory Efficient)
```python
# When you don't need to store all values
sum_squares = sum(x * x for x in range(1000000))  # No list created

# Find first match (stops early)
first_even = next((x for x in range(1000) if x % 2 == 0), None)
```

### Dictionary Comprehension
```python
# Create frequency map
freq = {x: nums.count(x) for x in set(nums)}

# Swap keys and values
swapped = {v: k for k, v in original.items()}

# Filter dictionary
filtered = {k: v for k, v in d.items() if v > 10}
```

### Set Comprehension
```python
# Unique squares
unique_squares = {x * x for x in nums}

# Remove duplicates while keeping order (Python 3.7+)
seen = set()
unique = [x for x in nums if not (x in seen or seen.add(x))]
```

**LeetCode Problems:**
- Two Sum (dict comprehension)
- Valid Sudoku (set comprehension)
- Group Anagrams (dict comprehension)

---

## String Manipulation Tricks

### String Reversal
```python
# Reverse entire string
s[::-1]

# Reverse words in string
' '.join(s.split()[::-1])

# Reverse each word individually
' '.join(word[::-1] for word in s.split())
```

### String Checking
```python
# Check palindrome
s == s[::-1]

# Check if all characters are unique
len(s) == len(set(s))

# Check if anagrams
sorted(s1) == sorted(s2)
# or: Counter(s1) == Counter(s2)

# Check if substring
'abc' in 'xyzabcdef'

# Count substring occurrences
s.count('ab')
```

### String Building (Efficient)
```python
# BAD - O(n²) due to string immutability
result = ""
for c in chars:
    result += c

# GOOD - O(n) using list
result = []
for c in chars:
    result.append(c)
return ''.join(result)

# BETTER - list comprehension
return ''.join(result)
```

### String Parsing
```python
# Split by multiple delimiters
import re
parts = re.split(r'[,;\s]+', string)

# Remove non-alphanumeric
''.join(c for c in s if c.isalnum())
# or: re.sub(r'[^a-zA-Z0-9]', '', s)

# Extract digits
digits = ''.join(c for c in s if c.isdigit())
# or: digits = re.findall(r'\d', s)
```

### String Rotation & Manipulation
```python
# Check if s2 is rotation of s1
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

# Remove duplicates keeping order
from collections import OrderedDict
''.join(OrderedDict.fromkeys(s))
```

**LeetCode Problems:**
- Valid Palindrome
- Longest Palindromic Substring
- Group Anagrams
- Valid Anagram
- Reverse Words in String

---

## Dictionary & Set Tricks

### Default Values
```python
# Instead of:
if key not in d:
    d[key] = 0
d[key] += 1

# Use defaultdict:
from collections import defaultdict
d = defaultdict(int)
d[key] += 1

# Or dict.get():
d[key] = d.get(key, 0) + 1
```

### Counter Magic
```python
from collections import Counter

# Frequency map
freq = Counter(nums)

# Most common elements
top_k = [x for x, _ in freq.most_common(k)]

# Arithmetic on counters
c1 + c2  # Add counts
c1 - c2  # Subtract (keep positive only)
c1 & c2  # Intersection (min counts)
c1 | c2  # Union (max counts)
```

### Set Operations
```python
# Intersection
common = set1 & set2

# Union
all_items = set1 | set2

# Difference
only_in_set1 = set1 - set2

# Symmetric difference (XOR)
different = set1 ^ set2

# Check subset/superset
set1 <= set2  # Is subset
set1 >= set2  # Is superset
```

### Dictionary Tricks
```python
# Merge dictionaries (Python 3.9+)
merged = d1 | d2

# Python 3.5+
merged = {**d1, **d2}

# Get with default and set
value = d.setdefault(key, default_value)

# Pop with default
value = d.pop(key, default_value)

# Reverse lookup (value to key)
key = next((k for k, v in d.items() if v == target), None)
```

### Ordered Dictionary
```python
from collections import OrderedDict

# LRU Cache pattern
od = OrderedDict()
od['a'] = 1
od.move_to_end('a')  # Move to end
od.popitem(last=False)  # Pop from beginning
```

**LeetCode Problems:**
- Two Sum (dict)
- Top K Frequent Elements (Counter)
- LRU Cache (OrderedDict)
- Contains Duplicate (set)
- Intersection of Two Arrays (set)

---

## Math & Number Tricks

### Integer Division & Modulo
```python
# Floor division
quotient = a // b

# Get quotient and remainder
quotient, remainder = divmod(a, b)

# Ceiling division
import math
ceil_div = math.ceil(a / b)
# or: ceil_div = (a + b - 1) // b
# or: ceil_div = -(-a // b)
```

### Power & Roots
```python
# Fast exponentiation
pow(x, n)
# or: x ** n

# Modular exponentiation
pow(x, n, mod)  # (x^n) % mod - efficient!

# Square root
import math
math.isqrt(n)  # Integer square root (Python 3.8+)
int(math.sqrt(n))

# Check perfect square
math.isqrt(n) ** 2 == n
```

### GCD & LCM
```python
import math

# Greatest Common Divisor
gcd = math.gcd(a, b)

# For multiple numbers (Python 3.9+)
from functools import reduce
gcd_all = reduce(math.gcd, numbers)

# Least Common Multiple
lcm = abs(a * b) // math.gcd(a, b)
```

### Number Properties
```python
# Check prime (optimized)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

# Count digits
num_digits = len(str(n))
# or: num_digits = math.floor(math.log10(n)) + 1  # for n > 0

# Sum of digits
digit_sum = sum(int(d) for d in str(n))
# or: digit_sum = sum(map(int, str(n)))

# Reverse number
reversed_num = int(str(n)[::-1])
```

### Range Tricks
```python
# Inclusive range
range(start, end + 1)

# Reverse range
range(n, -1, -1)  # n, n-1, ..., 1, 0

# Even numbers
range(0, n, 2)

# Step through every kth element
range(0, n, k)
```

**LeetCode Problems:**
- Pow(x, n) (fast exponentiation)
- Sqrt(x) (binary search)
- Happy Number (digit sum)
- Palindrome Number
- Reverse Integer

---

## Slicing & Indexing Magic

### Basic Slicing
```python
# arr[start:end:step]

# First k elements
arr[:k]

# Last k elements
arr[-k:]

# All except first k
arr[k:]

# All except last k
arr[:-k]

# Reverse
arr[::-1]

# Every other element
arr[::2]

# Even indices
arr[::2]

# Odd indices
arr[1::2]
```

### Advanced Slicing
```python
# Middle element(s)
mid = arr[len(arr)//2]  # Middle for odd length
mid_two = arr[len(arr)//2-1:len(arr)//2+1]  # Two middle for even

# Rotate array by k
arr = arr[k:] + arr[:k]
# or: arr[-k:] + arr[:-k]  # rotate right

# Remove element at index i
arr = arr[:i] + arr[i+1:]

# Insert element at index i
arr = arr[:i] + [new_elem] + arr[i:]

# Swap elements
arr[i], arr[j] = arr[j], arr[i]
```

### Slice Assignment
```python
# Replace slice
arr[i:j] = new_values

# Delete slice
del arr[i:j]
# or: arr[i:j] = []

# Reverse subarray in-place
arr[i:j] = arr[i:j][::-1]
```

### String Slicing
```python
# Check prefix
s.startswith(prefix)
# or: s[:len(prefix)] == prefix

# Check suffix
s.endswith(suffix)
# or: s[-len(suffix):] == suffix

# Remove prefix/suffix (Python 3.9+)
s.removeprefix(prefix)
s.removesuffix(suffix)
```

**LeetCode Problems:**
- Rotate Array (slicing)
- Reverse String (slicing)
- Valid Palindrome (slicing)
- Remove Element (slice assignment)

---

## Built-in Functions Mastery

### Enumeration & Iteration
```python
# Get index and value
for i, val in enumerate(arr):
    print(i, val)

# Start from different index
for i, val in enumerate(arr, start=1):
    print(i, val)

# Parallel iteration
for a, b, c in zip(arr1, arr2, arr3):
    print(a, b, c)

# Longest wins (Python 3)
from itertools import zip_longest
for a, b in zip_longest(arr1, arr2, fillvalue=0):
    print(a, b)
```

### Min/Max Tricks
```python
# Max with key function
max_val = max(arr, key=lambda x: x[1])  # Max by second element

# Multiple conditions
max_val = max(arr, key=lambda x: (x[0], -x[1]))  # Max x[0], then min x[1]

# Min/max of multiple values
minimum = min(a, b, c)

# Default for empty
max_val = max(arr, default=0)
```

### Sorting Mastery
```python
# Sort by multiple keys
arr.sort(key=lambda x: (x[0], -x[1]))  # First ascending, second descending

# Sort with custom comparator (use functools.cmp_to_key)
from functools import cmp_to_key
def compare(a, b):
    return a - b
arr.sort(key=cmp_to_key(compare))

# Sort strings by length then alphabetically
words.sort(key=lambda x: (len(x), x))

# Stable sort (Python's sort is stable)
# Elements with equal keys maintain relative order
```

### All/Any/Filter
```python
# Check if all elements satisfy condition
all(x > 0 for x in arr)

# Check if any element satisfies condition
any(x > 0 for x in arr)

# Filter elements
filtered = list(filter(lambda x: x > 0, arr))
# or: filtered = [x for x in arr if x > 0]

# Map transformation
squared = list(map(lambda x: x**2, arr))
# or: squared = [x**2 for x in arr]
```

### Sum & Product
```python
# Sum of array
total = sum(arr)

# Sum with start value
total = sum(arr, start_value)

# Product of array
from functools import reduce
import operator
product = reduce(operator.mul, arr, 1)
# or: product = 1
#     for x in arr:
#         product *= x
```

**LeetCode Problems:**
- Two Sum (enumerate)
- Merge Intervals (sorting)
- Meeting Rooms (sorting)
- Valid Parentheses (all/any)

---

## Lambda & Functional Programming

### Lambda Functions
```python
# Basic lambda
square = lambda x: x ** 2

# Multiple arguments
add = lambda x, y: x + y

# Conditional lambda
abs_val = lambda x: x if x >= 0 else -x

# Lambda with default arguments
greet = lambda name, msg='Hello': f'{msg}, {name}'
```

### Map, Filter, Reduce
```python
from functools import reduce

# Map - transform each element
doubled = list(map(lambda x: x * 2, arr))

# Filter - keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, arr))

# Reduce - accumulate values
total = reduce(lambda acc, x: acc + x, arr, 0)
product = reduce(lambda acc, x: acc * x, arr, 1)

# Find max using reduce
max_val = reduce(lambda a, b: a if a > b else b, arr)
```

### Sorting with Lambda
```python
# Sort by custom key
points.sort(key=lambda p: p[0]**2 + p[1]**2)  # Distance from origin

# Sort 2D by column
matrix.sort(key=lambda row: row[1])

# Sort strings by custom rule
words.sort(key=lambda w: (len(w), w))
```

### functools.partial
```python
from functools import partial

# Create specialized function
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
```

**LeetCode Problems:**
- K Closest Points to Origin (lambda sorting)
- Sort Colors (lambda)
- Custom Sort String (lambda)

---

## Collections Module Secrets

### Counter Advanced
```python
from collections import Counter

c = Counter('abracadabra')

# Get count (returns 0 if not found)
c['z']  # 0

# Most common n elements
c.most_common(3)  # [('a', 5), ('b', 2), ('r', 2)]

# Elements as list (with repetition)
list(c.elements())  # ['a', 'a', 'a', 'a', 'a', 'b', 'b', ...]

# Subtract counters
c1 - c2  # Keep only positive counts

# Update counter
c.update('aabbcc')
```

### deque (Double-ended Queue)
```python
from collections import deque

dq = deque([1, 2, 3])

# Add to both ends - O(1)
dq.append(4)        # Add to right
dq.appendleft(0)    # Add to left

# Remove from both ends - O(1)
dq.pop()            # Remove from right
dq.popleft()        # Remove from left

# Rotate
dq.rotate(2)        # Rotate right by 2
dq.rotate(-1)       # Rotate left by 1

# Max length (circular buffer)
dq = deque(maxlen=5)  # Automatically removes oldest when full
```

### defaultdict
```python
from collections import defaultdict

# List of lists
graph = defaultdict(list)
graph[1].append(2)  # No KeyError

# Counter without imports
freq = defaultdict(int)
for x in arr:
    freq[x] += 1

# Set of sets
groups = defaultdict(set)
groups[key].add(value)

# Custom default factory
def default_value():
    return float('inf')
d = defaultdict(default_value)
```

### OrderedDict
```python
from collections import OrderedDict

# Maintains insertion order
od = OrderedDict()
od['a'] = 1
od['b'] = 2

# Move to end (useful for LRU)
od.move_to_end('a')
od.move_to_end('a', last=False)  # Move to beginning

# Pop items
od.popitem(last=True)   # Remove last (LIFO)
od.popitem(last=False)  # Remove first (FIFO)
```

### namedtuple
```python
from collections import namedtuple

# Create Point class
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # Named access

# Good for readable code
Person = namedtuple('Person', 'name age city')
person = Person('Alice', 30, 'NYC')
```

**LeetCode Problems:**
- Top K Frequent Elements (Counter)
- LRU Cache (OrderedDict)
- Sliding Window Maximum (deque)
- Design Browser History (deque)

---

## Itertools Power Moves

### Combinations & Permutations
```python
from itertools import combinations, permutations, product

# Combinations (order doesn't matter)
list(combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]

# Permutations (order matters)
list(permutations([1,2,3], 2))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# Cartesian product
list(product([1,2], [3,4]))  # [(1,3), (1,4), (2,3), (2,4)]

# Product with repeat
list(product([0,1], repeat=3))  # All 3-bit binary numbers
```

### Infinite Iterators
```python
from itertools import count, cycle, repeat

# Count from n
for i in count(10):
    if i > 15:
        break
    print(i)  # 10, 11, 12, 13, 14, 15

# Cycle through sequence
counter = 0
for item in cycle([1, 2, 3]):
    if counter > 5:
        break
    print(item)
    counter += 1

# Repeat value n times
list(repeat(5, 3))  # [5, 5, 5]
```

### Grouping & Accumulation
```python
from itertools import groupby, accumulate

# Group consecutive elements
data = [1, 1, 2, 2, 2, 3, 1, 1]
for key, group in groupby(data):
    print(key, list(group))

# Cumulative sum
list(accumulate([1,2,3,4]))  # [1, 3, 6, 10]

# Cumulative product
from operator import mul
list(accumulate([1,2,3,4], mul))  # [1, 2, 6, 24]

# Running maximum
list(accumulate([3,1,4,1,5], max))  # [3, 3, 4, 4, 5]
```

### Chain & Flatten
```python
from itertools import chain

# Chain multiple iterables
list(chain([1,2], [3,4], [5,6]))  # [1,2,3,4,5,6]

# Flatten 2D list
matrix = [[1,2], [3,4], [5,6]]
flattened = list(chain.from_iterable(matrix))  # [1,2,3,4,5,6]
```

### Slicing Iterators
```python
from itertools import islice

# Get slice of iterator
list(islice(range(10), 2, 8, 2))  # [2, 4, 6]

# First n items
list(islice(infinite_iterator, 10))
```

**LeetCode Problems:**
- Subsets (combinations)
- Permutations (permutations)
- Letter Combinations of Phone Number (product)
- Combination Sum (combinations)

---

## Bit Manipulation Shortcuts

### Basic Operations
```python
# Check if bit is set
def is_bit_set(num, i):
    return (num >> i) & 1

# Set bit
def set_bit(num, i):
    return num | (1 << i)

# Clear bit
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle bit
def toggle_bit(num, i):
    return num ^ (1 << i)
```

### Tricks
```python
# Check if power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Count set bits (Brian Kernighan)
def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
# or: bin(n).count('1')

# Get rightmost set bit
rightmost = n & -n

# Clear rightmost set bit
n & (n - 1)

# XOR all numbers (find single number)
result = 0
for num in nums:
    result ^= num

# Swap without temp
a ^= b
b ^= a
a ^= b
```

### Bitmask DP
```python
# Check if subset includes element i
if mask & (1 << i):
    pass

# Add element i to subset
mask |= (1 << i)

# Remove element i from subset
mask &= ~(1 << i)

# Iterate all subsets of mask
subset = mask
while subset:
    # Process subset
    subset = (subset - 1) & mask
```

**LeetCode Problems:**
- Single Number (XOR)
- Number of 1 Bits (bit counting)
- Power of Two (bit trick)
- Missing Number (XOR)
- Subsets (bitmask)

---

## Common Interview Patterns

### Two Pointers
```python
# Opposite ends
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process
        if condition:
            left += 1
        else:
            right -= 1

# Same direction
def two_pointer_same(arr):
    slow = fast = 0
    while fast < len(arr):
        if condition:
            slow += 1
        fast += 1
```

### Sliding Window
```python
# Fixed size
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Variable size
def sliding_window_variable(arr):
    left = 0
    max_len = 0
    window = set()
    
    for right in range(len(arr)):
        while arr[right] in window:
            window.remove(arr[left])
            left += 1
        window.add(arr[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### Fast & Slow Pointers
```python
# Find cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find middle
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Monotonic Stack
```python
# Next greater element
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result
```

### Binary Search Template
```python
# Standard binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Find leftmost
def binary_search_left(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

**LeetCode Problems:**
- Two Sum (two pointers)
- Container With Most Water (two pointers)
- Longest Substring Without Repeating (sliding window)
- Linked List Cycle (fast/slow)
- Daily Temperatures (monotonic stack)

---

## Time & Space Optimizations

### Space Optimization Tricks
```python
# Rolling array for DP
# Instead of: dp = [[0] * n for _ in range(m)]
# Use: dp = [0] * n (only keep previous row)

# In-place modifications
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Use indices instead of creating new arrays
# Track start/end pointers instead of slicing
```

### Constant Space Tricks
```python
# Mark visited in array using sign
def mark_visited(nums):
    for num in nums:
        idx = abs(num) - 1
        nums[idx] = -abs(nums[idx])

# Use math to encode two values in one
def encode(a, b):
    return a * 1000 + b  # If both < 1000

def decode(encoded):
    return encoded // 1000, encoded % 1000
```

### Time Optimization
```python
# Early termination
def find_element(arr, target):
    for x in arr:
        if x == target:
            return True  # Return immediately
        if x > target:  # Early exit
            break
    return False

# Precomputation
# Compute prefix sum once
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]

# Range sum query in O(1)
def range_sum(left, right):
    return prefix[right + 1] - prefix[left]
```

### Cache Results
```python
# Memoization with decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Manual memoization
def dp_with_memo():
    memo = {}
    
    def helper(n):
        if n in memo:
            return memo[n]
        # Compute result
        result = ...
        memo[n] = result
        return result
    
    return helper
```

**LeetCode Problems:**
- Remove Duplicates (in-place)
- Move Zeroes (in-place)
- Find All Duplicates (constant space)
- Range Sum Query (prefix sum)

---

## Google-Specific Tips

### Code Quality
```python
# Use descriptive variable names
left, right = 0, len(arr) - 1  # Good
l, r = 0, len(arr) - 1          # Avoid

# Add comments for complex logic
# Binary search to find leftmost position where arr[i] >= target
```

### Edge Cases to Check
```python
# Always consider:
# - Empty input: arr = []
# - Single element: arr = [1]
# - Two elements: arr = [1, 2]
# - All same: arr = [1, 1, 1]
# - Sorted: arr = [1, 2, 3]
# - Reverse sorted: arr = [3, 2, 1]
# - Duplicates: arr = [1, 2, 2, 3]
# - Negative numbers: arr = [-1, 0, 1]
# - Large numbers: test with constraints
```

### Performance Patterns
```python
# O(n log n) - Sorting-based solutions
arr.sort()

# O(n) - Hash map solutions
from collections import Counter
freq = Counter(arr)

# O(log n) - Binary search
import bisect
idx = bisect.bisect_left(arr, target)

# O(1) - Math-based solutions
# Use formulas, bit manipulation
```

### Communication During Interview
```python
# Template for explaining approach:
"""
1. Clarify requirements and constraints
   - "Can the array be empty?"
   - "Are all numbers positive?"

2. Explain brute force
   - "The naive approach would be O(n²)..."

3. Optimize
   - "We can use a hash map to reduce to O(n)..."

4. Analyze complexity
   - "Time: O(n), Space: O(n)"

5. Consider edge cases
   - "For empty input, we return 0"

6. Test with example
   - Walk through with provided example
"""
```

---

## Final Pro Tips

### 1. **Use Python's Strengths**
```python
# Multiple assignment
a, b = b, a  # Swap

# Chained comparisons
if a < b < c:
    pass

# Conditional expressions
result = x if condition else y

# Unpacking
first, *middle, last = arr
```

### 2. **Know Your Built-ins**
```python
# divmod for quotient and remainder
q, r = divmod(a, b)

# any/all for boolean checks
if any(x > 0 for x in arr):
    pass

# zip for parallel iteration
for a, b in zip(arr1, arr2):
    pass

# enumerate for index tracking
for i, val in enumerate(arr):
    pass
```

### 3. **Avoid Common Mistakes**
```python
# BAD: Mutable default argument
def func(arr=[]):  # DON'T
    arr.append(1)

# GOOD:
def func(arr=None):
    if arr is None:
        arr = []
    arr.append(1)

# BAD: Modifying list while iterating
for x in arr:
    if condition:
        arr.remove(x)  # DON'T

# GOOD: Use list comprehension
arr = [x for x in arr if not condition]
```

### 4. **Master These Data Structures**
```python
# Priority Queue (min heap)
import heapq
heap = []
heapq.heappush(heap, item)
min_item = heapq.heappop(heap)

# OrderedDict for LRU
from collections import OrderedDict
cache = OrderedDict()

# Counter for frequency
from collections import Counter
freq = Counter(arr)

# deque for O(1) ends
from collections import deque
dq = deque()
```

---

## Quick Reference: Time Complexities

| Operation | List | Set | Dict | deque |
|-----------|------|-----|------|-------|
| Access | O(1) | - | O(1) | O(n) |
| Search | O(n) | O(1) | O(1) | O(n) |
| Insert | O(n) | O(1) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) | O(1) |
| Append | O(1)* | O(1) | O(1) | O(1) |

*Amortized

---

## Practice Problems by Pattern

### Two Pointers: 15 problems
- Two Sum II, 3Sum, 4Sum
- Container With Most Water
- Trapping Rain Water
- Remove Duplicates
- Move Zeroes

### Sliding Window: 12 problems
- Longest Substring Without Repeating
- Minimum Window Substring
- Max Consecutive Ones
- Longest Repeating Character Replacement

### Hash Map: 20 problems
- Two Sum, Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence
- Subarray Sum Equals K

### Binary Search: 15 problems
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Sqrt(x), Pow(x, n)

### DP: 25 problems
- Climbing Stairs, House Robber
- Coin Change, Edit Distance
- Longest Increasing Subsequence

---

**Master these tricks and you'll code faster, cleaner, and smarter in your Google interview! 🚀**

*Practice makes perfect. Solve 200 problems and these will become second nature!*
