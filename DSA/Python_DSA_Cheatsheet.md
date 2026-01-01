# Python DSA Cheatsheet - Complete Guide with Problem-Solving Patterns

## Table of Contents
- [Python Fundamentals for DSA](#python-fundamentals-for-dsa)
- [Time & Space Complexity](#time--space-complexity)
- [Arrays & Lists](#arrays--lists)
- [Strings](#strings)
- [Hash Tables & Dictionaries](#hash-tables--dictionaries)
- [Stacks & Queues](#stacks--queues)
- [Linked Lists](#linked-lists)
- [Trees](#trees)
- [Graphs](#graphs)
- [Dynamic Programming](#dynamic-programming)
- [Sorting & Searching](#sorting--searching)
- [Problem-Solving Patterns](#problem-solving-patterns)
- [Interview Tips & Tricks](#interview-tips--tricks)

## Python Fundamentals for DSA

### Essential Built-in Functions
```python
# Math operations
import math
math.ceil(4.2)      # 5 - ceiling
math.floor(4.8)     # 4 - floor
math.sqrt(16)       # 4.0 - square root
abs(-5)             # 5 - absolute value
pow(2, 3)           # 8 - power
divmod(10, 3)       # (3, 1) - quotient and remainder

# Min/Max operations
min(1, 2, 3)        # 1
max([1, 2, 3])      # 3
min(arr, key=len)   # element with minimum length

# String/List operations
len("hello")        # 5
sum([1, 2, 3])      # 6
sorted([3, 1, 2])   # [1, 2, 3]
reversed([1, 2, 3]) # iterator for [3, 2, 1]
enumerate(['a', 'b', 'c'])  # [(0, 'a'), (1, 'b'), (2, 'c')]
zip([1, 2], ['a', 'b'])     # [(1, 'a'), (2, 'b')]

# Type conversions
int("123")          # 123
str(123)            # "123"
list("abc")         # ['a', 'b', 'c']
tuple([1, 2, 3])    # (1, 2, 3)
set([1, 2, 2, 3])   # {1, 2, 3}
```

### List Comprehensions & Generators
```python
# List comprehensions
squares = [x**2 for x in range(10)]                    # [0, 1, 4, 9, 16, ...]
evens = [x for x in range(20) if x % 2 == 0]         # [0, 2, 4, 6, ...]
matrix = [[i*j for j in range(3)] for i in range(3)]  # 2D matrix

# Dictionary comprehensions
char_count = {char: word.count(char) for char in set(word)}
squares_dict = {x: x**2 for x in range(5)}

# Set comprehensions
unique_lengths = {len(word) for word in words}

# Generator expressions (memory efficient)
squares_gen = (x**2 for x in range(1000000))  # Memory efficient
sum_of_squares = sum(x**2 for x in range(100))
```

### Useful Python Tricks for DSA
```python
# Multiple assignment
a, b = b, a  # Swap variables
x, y, z = 1, 2, 3  # Multiple assignment

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
head, *tail = [1, 2, 3, 4]              # head=1, tail=[2,3,4]

# Default values with get()
count = counter.get(key, 0)  # Returns 0 if key doesn't exist

# Infinity values
float('inf')   # Positive infinity
float('-inf')  # Negative infinity

# Binary operations
bin(5)         # '0b101'
5 & 3          # 1 (AND)
5 | 3          # 7 (OR)
5 ^ 3          # 6 (XOR)
5 << 1         # 10 (left shift)
5 >> 1         # 2 (right shift)

# String formatting
f"Value: {value}, Index: {i}"  # f-strings (preferred)
"Value: {}, Index: {}".format(value, i)  # format method
```

## Time & Space Complexity

### Big O Notation Reference
```python
# O(1) - Constant Time
def get_first_element(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear Time
def find_max(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# O(n log n) - Linearithmic Time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

# O(n²) - Quadratic Time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2^n) - Exponential Time
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)
```

### Space Complexity Examples
```python
# O(1) Space - Constant Space
def reverse_array_inplace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# O(n) Space - Linear Space
def reverse_array_new(arr):
    return arr[::-1]  # Creates new array

# O(n) Space - Recursive call stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # n recursive calls on stack
```

## Arrays & Lists

### Common Array Operations
```python
# Array initialization
arr = [0] * n                    # [0, 0, 0, ..., 0] (n times)
matrix = [[0] * cols for _ in range(rows)]  # 2D array
visited = [False] * n            # Boolean array

# Slicing operations
arr[start:end]      # Elements from start to end-1
arr[start:]         # Elements from start to end
arr[:end]           # Elements from beginning to end-1
arr[::step]         # Every step-th element
arr[::-1]           # Reverse array
arr[start:end:step] # Start to end with step

# Common patterns
arr.append(item)           # Add to end - O(1)
arr.insert(index, item)    # Insert at index - O(n)
arr.pop()                  # Remove last - O(1)
arr.pop(index)             # Remove at index - O(n)
arr.remove(item)           # Remove first occurrence - O(n)
arr.index(item)            # Find index - O(n)
arr.count(item)            # Count occurrences - O(n)
```

### Two Pointers Technique
```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def remove_duplicates(arr):
    """Remove duplicates from sorted array in-place"""
    if not arr:
        return 0
    
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return write_index

def reverse_words(s):
    """Reverse words in a string"""
    # Convert to list for in-place operations
    chars = list(s)
    
    # Reverse entire string
    reverse_range(chars, 0, len(chars) - 1)
    
    # Reverse each word
    start = 0
    for end in range(len(chars) + 1):
        if end == len(chars) or chars[end] == ' ':
            reverse_range(chars, start, end - 1)
            start = end + 1
    
    return ''.join(chars)

def reverse_range(chars, start, end):
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
```

### Sliding Window Technique
```python
def max_sum_subarray(arr, k):
    """Maximum sum of subarray of size k"""
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def longest_substring_without_repeating(s):
    """Length of longest substring without repeating characters"""
    char_index = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

def min_window_substring(s, t):
    """Minimum window substring containing all characters of t"""
    if not s or not t:
        return ""
    
    # Count characters in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    
    window_counts = {}
    ans = float("inf"), None, None
    
    while right < len(s):
        # Add character from right to window
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        # Contract window until it's no longer valid
        while left <= right and formed == required:
            character = s[left]
            
            # Save the smallest window
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

### Array Rotation & Manipulation
```python
def rotate_array(arr, k):
    """Rotate array to the right by k steps"""
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Method 1: Using extra space
    return arr[-k:] + arr[:-k]

def rotate_array_inplace(arr, k):
    """Rotate array in-place using reversal"""
    n = len(arr)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

def find_missing_number(arr, n):
    """Find missing number in array of 1 to n"""
    # Method 1: Using sum formula
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
    
    # Method 2: Using XOR
    xor_all = 0
    xor_arr = 0
    
    for i in range(1, n + 1):
        xor_all ^= i
    
    for num in arr:
        xor_arr ^= num
    
    return xor_all ^ xor_arr

def find_duplicate_number(arr):
    """Find duplicate in array using Floyd's cycle detection"""
    # Phase 1: Find intersection point
    slow = fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow
```

## Strings

### String Manipulation Patterns
```python
def is_palindrome(s):
    """Check if string is palindrome (ignoring case and non-alphanumeric)"""
    # Method 1: Two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

def longest_palindromic_substring(s):
    """Find longest palindromic substring"""
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

def group_anagrams(strs):
    """Group anagrams together"""
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to create key
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())

def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    if len(s1) != len(s2):
        return False
    
    # Method 1: Using sorting
    return sorted(s1) == sorted(s2)
    
    # Method 2: Using character count
    from collections import Counter
    return Counter(s1) == Counter(s2)
```

### String Searching Algorithms
```python
def kmp_search(text, pattern):
    """KMP (Knuth-Morris-Pratt) string matching algorithm"""
    def build_lps(pattern):
        """Build Longest Proper Prefix which is also Suffix array"""
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    if not pattern:
        return []
    
    lps = build_lps(pattern)
    matches = []
    
    i = j = 0  # i for text, j for pattern
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

def rabin_karp_search(text, pattern):
    """Rabin-Karp string matching using rolling hash"""
    if len(pattern) > len(text):
        return []
    
    base = 256
    prime = 101
    pattern_len = len(pattern)
    text_len = len(text)
    
    # Calculate hash of pattern and first window
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = pow(base, pattern_len-1) % prime
    for i in range(pattern_len - 1):
        h = (h * base) % prime
    
    # Calculate hash of pattern and first window
    for i in range(pattern_len):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    matches = []
    
    # Slide pattern over text
    for i in range(text_len - pattern_len + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check characters one by one
            if text[i:i + pattern_len] == pattern:
                matches.append(i)
        
        # Calculate hash for next window
        if i < text_len - pattern_len:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_len])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return matches
```## Lambd
a Functions & Functional Programming

### Lambda Functions
```python
# Basic lambda syntax
square = lambda x: x**2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Square all numbers
squares = list(map(lambda x: x**2, numbers))

# Sort by custom criteria
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
students.sort(key=lambda x: x[1])  # Sort by grade

# Find maximum using custom key
words = ['python', 'java', 'c++', 'javascript']
longest = max(words, key=lambda x: len(x))

# Conditional lambda
max_val = lambda a, b: a if a > b else b
```

### Map, Filter, Reduce
```python
from functools import reduce

# Map - Apply function to all elements
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25]

# Multiple iterables with map
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
# Result: [5, 7, 9]

# Filter - Filter elements based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6, 8, 10]

# Reduce - Reduce sequence to single value
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
# Result: 15

product = reduce(lambda x, y: x * y, numbers)
# Result: 120

# Find maximum using reduce
max_num = reduce(lambda x, y: x if x > y else y, numbers)
```

### Advanced Functional Programming
```python
# Partial functions
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Fix first argument to 2
triple = partial(multiply, 3)  # Fix first argument to 3

print(double(5))  # 10
print(triple(4))  # 12

# Function composition
def compose(f, g):
    return lambda x: f(g(x))

add_one = lambda x: x + 1
square = lambda x: x**2

# Compose functions: square(add_one(x))
composed = compose(square, add_one)
print(composed(3))  # 16 (3+1)^2

# Higher-order functions
def make_multiplier(n):
    return lambda x: x * n

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))  # 10
print(times_3(4))  # 12
```

## Hash Tables & Dictionaries

### Dictionary Operations & Patterns
```python
# Dictionary creation and initialization
d = {}
d = dict()
d = {'a': 1, 'b': 2, 'c': 3}
d = dict(a=1, b=2, c=3)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in d.items() if v > 1}

# Common patterns
from collections import defaultdict, Counter

# DefaultDict - Avoid KeyError
dd = defaultdict(int)  # Default value 0
dd = defaultdict(list)  # Default value []
dd = defaultdict(set)   # Default value set()

# Counter - Count occurrences
text = "hello world"
char_count = Counter(text)
word_count = Counter(['apple', 'banana', 'apple', 'cherry'])

# Most common elements
most_common = char_count.most_common(3)  # Top 3 most common

# Dictionary operations
d.get(key, default)     # Get with default value
d.setdefault(key, default)  # Set if key doesn't exist
d.pop(key, default)     # Remove and return value
d.popitem()             # Remove and return arbitrary item
d.update(other_dict)    # Update with another dict

# Merge dictionaries (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Hash Table Problem Patterns
```python
def two_sum(nums, target):
    """Find two numbers that add up to target"""
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    
    return []

def group_anagrams(strs):
    """Group strings that are anagrams"""
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

def first_non_repeating_char(s):
    """Find first non-repeating character"""
    char_count = {}
    
    # Count occurrences
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first non-repeating
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

def longest_substring_without_repeating(s):
    """Longest substring without repeating characters"""
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

def subarray_sum_equals_k(nums, k):
    """Count subarrays with sum equal to k"""
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle case where prefix_sum == k
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Update count of current prefix_sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

## Stacks & Queues

### Stack Implementation & Patterns
```python
# Stack using list
stack = []
stack.append(item)      # Push
item = stack.pop()      # Pop
top = stack[-1]         # Peek
is_empty = len(stack) == 0

# Stack problems
def valid_parentheses(s):
    """Check if parentheses are valid"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

def daily_temperatures(temperatures):
    """Days until warmer temperature"""
    result = [0] * len(temperatures)
    stack = []  # Store indices
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

def largest_rectangle_histogram(heights):
    """Largest rectangle in histogram"""
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights + [0]):  # Add 0 to process remaining
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

def evaluate_rpn(tokens):
    """Evaluate Reverse Polish Notation"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))
    
    return stack[0]
```

### Queue Implementation & Patterns
```python
from collections import deque

# Queue using deque (preferred)
queue = deque()
queue.append(item)      # Enqueue
item = queue.popleft()  # Dequeue
front = queue[0]        # Peek front
is_empty = len(queue) == 0

# Queue using list (inefficient)
queue = []
queue.append(item)      # Enqueue
item = queue.pop(0)     # Dequeue (O(n) operation)

# BFS template using queue
def bfs_template(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        # Process node
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def level_order_traversal(root):
    """Level order traversal of binary tree"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

def sliding_window_maximum(nums, k):
    """Maximum in each sliding window of size k"""
    from collections import deque
    
    dq = deque()  # Store indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

## Linked Lists

### Linked List Implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, val):
        if not self.head:
            return
        
        if self.head.val == val:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        return elements
```

### Linked List Patterns
```python
def reverse_linked_list(head):
    """Reverse a linked list"""
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

def has_cycle(head):
    """Detect cycle in linked list (Floyd's algorithm)"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

def find_cycle_start(head):
    """Find start of cycle in linked list"""
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def merge_two_sorted_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 or l2
    
    return dummy.next

def remove_nth_from_end(head, n):
    """Remove nth node from end"""
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node from end
    second.next = second.next.next
    
    return dummy.next

def find_middle(head):
    """Find middle node of linked list"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

## Trees

### Binary Tree Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
```

### Tree Traversal Algorithms
```python
def inorder_traversal(root):
    """Inorder: Left -> Root -> Right"""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def inorder_iterative(root):
    """Iterative inorder traversal"""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

def preorder_traversal(root):
    """Preorder: Root -> Left -> Right"""
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def postorder_traversal(root):
    """Postorder: Left -> Right -> Root"""
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

def level_order_traversal(root):
    """Level order (BFS) traversal"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```### Tree 
Problem Patterns
```python
def max_depth(root):
    """Maximum depth of binary tree"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def is_valid_bst(root):
    """Validate binary search tree"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def lowest_common_ancestor(root, p, q):
    """Find LCA in BST"""
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root

def path_sum(root, target_sum):
    """Check if path exists with given sum"""
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return (path_sum(root.left, remaining) or 
            path_sum(root.right, remaining))

def diameter_of_tree(root):
    """Diameter of binary tree"""
    max_diameter = 0
    
    def depth(node):
        nonlocal max_diameter
        if not node:
            return 0
        
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        
        # Update diameter
        max_diameter = max(max_diameter, left_depth + right_depth)
        
        return 1 + max(left_depth, right_depth)
    
    depth(root)
    return max_diameter
```

## Graphs

### Graph Representations
```python
# Adjacency List (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Adjacency Matrix
def create_adjacency_matrix(vertices, edges):
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    
    for u, v in edges:
        i, j = vertex_to_index[u], vertex_to_index[v]
        matrix[i][j] = 1
        matrix[j][i] = 1  # For undirected graph
    
    return matrix

# Edge List
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
```

### Graph Traversal Algorithms
```python
def dfs_recursive(graph, start, visited=None):
    """Depth-First Search (Recursive)"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    """Depth-First Search (Iterative)"""
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            # Add neighbors to stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

def bfs(graph, start):
    """Breadth-First Search"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def has_path(graph, start, end):
    """Check if path exists between two nodes"""
    if start == end:
        return True
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False
```

### Advanced Graph Algorithms
```python
def dijkstra(graph, start):
    """Dijkstra's shortest path algorithm"""
    import heapq
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current = heapq.heappop(pq)
        
        if current_distance > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def topological_sort(graph):
    """Topological sort using DFS"""
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]

def detect_cycle_undirected(graph):
    """Detect cycle in undirected graph"""
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    
    return False

def number_of_islands(grid):
    """Count number of islands in 2D grid"""
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or grid[r][c] == '0'):
            return
        
        visited.add((r, c))
        
        # Visit all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    
    return islands
```

## Dynamic Programming

### DP Patterns & Examples
```python
def fibonacci_dp(n):
    """Fibonacci with memoization"""
    memo = {}
    
    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    
    return fib(n)

def fibonacci_tabulation(n):
    """Fibonacci with tabulation"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def coin_change(coins, amount):
    """Minimum coins to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def longest_increasing_subsequence(nums):
    """Length of longest increasing subsequence"""
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def edit_distance(word1, word2):
    """Minimum edit distance between two strings"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack problem"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i - 1][w]
            
            # Include current item if possible
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    return dp[n][capacity]
```

## Sorting & Searching

### Sorting Algorithms
```python
def bubble_sort(arr):
    """Bubble Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    """Selection Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion Sort - O(n²)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge Sort - O(n log n)"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Quick Sort - O(n log n) average"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    """Heap Sort - O(n log n)"""
    import heapq
    
    # Convert to min heap
    heapq.heapify(arr)
    
    # Extract elements in sorted order
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    
    return sorted_arr
```

## Interview Tips & Tricks

### Problem-Solving Framework
```python
"""
1. UNDERSTAND THE PROBLEM
   - Read carefully and ask clarifying questions
   - Identify inputs, outputs, and constraints
   - Work through examples manually

2. PLAN YOUR APPROACH
   - Identify the problem pattern
   - Choose appropriate data structures
   - Consider time/space complexity

3. IMPLEMENT SOLUTION
   - Start with brute force if needed
   - Write clean, readable code
   - Handle edge cases

4. TEST AND OPTIMIZE
   - Test with examples and edge cases
   - Optimize if needed
   - Explain your solution
"""

# Common edge cases to consider
def handle_edge_cases(arr):
    # Empty input
    if not arr:
        return []
    
    # Single element
    if len(arr) == 1:
        return arr
    
    # All elements same
    if len(set(arr)) == 1:
        return arr
    
    # Already sorted
    if arr == sorted(arr):
        return arr
    
    # Reverse sorted
    if arr == sorted(arr, reverse=True):
        return arr[::-1]
```

### Time Complexity Quick Reference
```python
# O(1) - Constant
dict_lookup = d[key]
list_append = arr.append(x)
set_lookup = x in s

# O(log n) - Logarithmic
binary_search_result = bisect.bisect_left(arr, x)
heap_operations = heapq.heappush(heap, x)

# O(n) - Linear
list_search = x in arr
max_element = max(arr)
sum_elements = sum(arr)

# O(n log n) - Linearithmic
sorted_array = sorted(arr)
merge_sort_result = merge_sort(arr)

# O(n²) - Quadratic
nested_loops = [[i*j for j in range(n)] for i in range(n)]
bubble_sort_result = bubble_sort(arr)

# O(2^n) - Exponential
fibonacci_naive_result = fibonacci_naive(n)
all_subsets = generate_all_subsets(arr)
```

### Python-Specific Optimizations
```python
# Use list comprehensions instead of loops
# Slower
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i**2)

# Faster
result = [i**2 for i in range(10) if i % 2 == 0]

# Use built-in functions
# Slower
max_val = arr[0]
for val in arr[1:]:
    if val > max_val:
        max_val = val

# Faster
max_val = max(arr)

# Use collections.Counter for counting
# Slower
count = {}
for item in arr:
    count[item] = count.get(item, 0) + 1

# Faster
from collections import Counter
count = Counter(arr)

# Use enumerate instead of range(len())
# Less Pythonic
for i in range(len(arr)):
    print(i, arr[i])

# More Pythonic
for i, val in enumerate(arr):
    print(i, val)

# Use zip for parallel iteration
# Less efficient
for i in range(min(len(arr1), len(arr2))):
    print(arr1[i], arr2[i])

# More efficient
for a, b in zip(arr1, arr2):
    print(a, b)
```

This completes the comprehensive Python DSA Cheatsheet with lambda functions, functional programming concepts, and all essential data structures and algorithms patterns!