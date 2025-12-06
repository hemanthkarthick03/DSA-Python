"""
LeetCode Easy Problems (1-70)
Master DSA Fundamentals - Arrays, Strings, HashMaps, Basic Math, Two Pointers
"""

# ============================ ARRAYS ============================

def two_sum(nums, target):
    """
    Problem 1: Two Sum
    Given an array of integers nums and an integer target, return indices of two numbers that add up to target.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def remove_duplicates(nums):
    """
    Problem 2: Remove Duplicates from Sorted Array
    Remove duplicates in-place such that each element appears only once and return the new length.
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    """
    if not nums:
        return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1


def remove_element(nums, val):
    """
    Problem 3: Remove Element
    Remove all occurrences of val in-place and return the new length.
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


def search_insert(nums, target):
    """
    Problem 4: Search Insert Position
    Given a sorted array and a target value, return the index if found, otherwise return where it would be.
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def max_profit(prices):
    """
    Problem 5: Best Time to Buy and Sell Stock
    Find the maximum profit from buying and selling stock once.
    Input: prices = [7,1,5,3,6,4]
    Output: 5 (buy at 1, sell at 6)
    """
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def contains_duplicate(nums):
    """
    Problem 6: Contains Duplicate
    Return true if any value appears at least twice in the array.
    Input: nums = [1,2,3,1]
    Output: true
    """
    return len(nums) != len(set(nums))


def single_number(nums):
    """
    Problem 7: Single Number
    Every element appears twice except for one. Find that single one.
    Input: nums = [2,2,1]
    Output: 1
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def intersection(nums1, nums2):
    """
    Problem 8: Intersection of Two Arrays
    Return the intersection of two arrays.
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
    """
    return list(set(nums1) & set(nums2))


def move_zeroes(nums):
    """
    Problem 9: Move Zeroes
    Move all 0's to the end while maintaining relative order.
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


def plus_one(digits):
    """
    Problem 10: Plus One
    Given a non-empty array representing a non-negative integer, plus one to the integer.
    Input: digits = [1,2,3]
    Output: [1,2,4]
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def find_disappeared_numbers(nums):
    """
    Problem 11: Find All Numbers Disappeared in an Array
    Find all numbers in [1, n] that don't appear in the array.
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]
    """
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def third_max(nums):
    """
    Problem 12: Third Maximum Number
    Return the third maximum number in this array, or maximum if less than three.
    Input: nums = [3,2,1]
    Output: 1
    """
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[2] if len(nums) >= 3 else nums[0]


def find_max_consecutive_ones(nums):
    """
    Problem 13: Max Consecutive Ones
    Find the maximum number of consecutive 1s in the array.
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    """
    max_count = current = 0
    for num in nums:
        if num == 1:
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0
    return max_count


def sorted_squares(nums):
    """
    Problem 14: Squares of a Sorted Array
    Return an array of the squares of each number sorted in non-decreasing order.
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    """
    return sorted([x * x for x in nums])


def majority_element(nums):
    """
    Problem 15: Majority Element
    Find the element that appears more than n/2 times.
    Input: nums = [3,2,3]
    Output: 3
    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate


# ============================ STRINGS ============================

def reverse_string(s):
    """
    Problem 16: Reverse String
    Reverse the string in-place.
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_vowels(s):
    """
    Problem 17: Reverse Vowels of a String
    Reverse only the vowels in the string.
    Input: s = "hello"
    Output: "holle"
    """
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        else:
            right -= 1
    return ''.join(s)


def first_uniq_char(s):
    """
    Problem 18: First Unique Character in a String
    Find the first non-repeating character and return its index.
    Input: s = "leetcode"
    Output: 0
    """
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


def is_anagram(s, t):
    """
    Problem 19: Valid Anagram
    Determine if t is an anagram of s.
    Input: s = "anagram", t = "nagaram"
    Output: true
    """
    return sorted(s) == sorted(t)


def is_palindrome_string(s):
    """
    Problem 20: Valid Palindrome
    Determine if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


def longest_common_prefix(strs):
    """
    Problem 21: Longest Common Prefix
    Find the longest common prefix string amongst an array of strings.
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    """
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def str_str(haystack, needle):
    """
    Problem 22: Implement strStr()
    Return the index of the first occurrence of needle in haystack, or -1 if not present.
    Input: haystack = "hello", needle = "ll"
    Output: 2
    """
    if not needle:
        return 0
    return haystack.find(needle)


def length_of_last_word(s):
    """
    Problem 23: Length of Last Word
    Return the length of the last word in the string.
    Input: s = "Hello World"
    Output: 5
    """
    return len(s.strip().split()[-1]) if s.strip() else 0


def add_binary(a, b):
    """
    Problem 24: Add Binary
    Given two binary strings, return their sum as a binary string.
    Input: a = "11", b = "1"
    Output: "100"
    """
    return bin(int(a, 2) + int(b, 2))[2:]


def is_subsequence(s, t):
    """
    Problem 25: Is Subsequence
    Check if s is a subsequence of t.
    Input: s = "abc", t = "ahbgdc"
    Output: true
    """
    i = 0
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    return i == len(s)


# ============================ LINKED LIST ============================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    Problem 26: Reverse Linked List
    Reverse a singly linked list.
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
    """
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev


def has_cycle(head):
    """
    Problem 27: Linked List Cycle
    Determine if a linked list has a cycle in it.
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def merge_two_lists(l1, l2):
    """
    Problem 28: Merge Two Sorted Lists
    Merge two sorted linked lists and return it as a sorted list.
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    """
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next


def delete_duplicates(head):
    """
    Problem 29: Remove Duplicates from Sorted List
    Delete all duplicates such that each element appears only once.
    Input: head = [1,1,2]
    Output: [1,2]
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


def remove_elements(head, val):
    """
    Problem 30: Remove Linked List Elements
    Remove all nodes with the given val.
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


# ============================ TREES ============================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    Problem 31: Maximum Depth of Binary Tree
    Find the maximum depth of a binary tree.
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_same_tree(p, q):
    """
    Problem 32: Same Tree
    Check if two binary trees are the same.
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def invert_tree(root):
    """
    Problem 33: Invert Binary Tree
    Invert a binary tree.
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def is_symmetric(root):
    """
    Problem 34: Symmetric Tree
    Check if a tree is a mirror of itself.
    Input: root = [1,2,2,3,4,4,3]
    Output: true
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    return is_mirror(root, root) if root else True


def has_path_sum(root, target_sum):
    """
    Problem 35: Path Sum
    Determine if the tree has a root-to-leaf path with sum equal to targetSum.
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


def min_depth(root):
    """
    Problem 36: Minimum Depth of Binary Tree
    Find the minimum depth of a binary tree.
    Input: root = [3,9,20,null,null,15,7]
    Output: 2
    """
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


def sorted_array_to_bst(nums):
    """
    Problem 37: Convert Sorted Array to Binary Search Tree
    Convert sorted array to a height balanced BST.
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    """
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    return root


def is_balanced(root):
    """
    Problem 38: Balanced Binary Tree
    Determine if a binary tree is height-balanced.
    Input: root = [3,9,20,null,null,15,7]
    Output: true
    """
    def check_height(node):
        if not node:
            return 0
        left = check_height(node.left)
        if left == -1:
            return -1
        right = check_height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check_height(root) != -1


# ============================ MATH ============================

def is_palindrome_number(x):
    """
    Problem 39: Palindrome Number
    Determine whether an integer is a palindrome.
    Input: x = 121
    Output: true
    """
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


def roman_to_int(s):
    """
    Problem 40: Roman to Integer
    Convert a roman numeral to an integer.
    Input: s = "III"
    Output: 3
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total


def is_happy(n):
    """
    Problem 41: Happy Number
    A happy number is defined by replacing it with sum of squares of its digits until it equals 1.
    Input: n = 19
    Output: true
    """
    def get_next(num):
        return sum(int(d) ** 2 for d in str(num))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1


def is_ugly(n):
    """
    Problem 42: Ugly Number
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    Input: n = 6
    Output: true
    """
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1


def is_power_of_two(n):
    """
    Problem 43: Power of Two
    Determine if an integer is a power of two.
    Input: n = 16
    Output: true
    """
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_three(n):
    """
    Problem 44: Power of Three
    Determine if an integer is a power of three.
    Input: n = 27
    Output: true
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def add_digits(num):
    """
    Problem 45: Add Digits
    Given an integer, repeatedly add all its digits until the result has only one digit.
    Input: num = 38
    Output: 2 (3 + 8 = 11, 1 + 1 = 2)
    """
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


def fizz_buzz(n):
    """
    Problem 46: Fizz Buzz
    Return string array where for multiples of 3 print "Fizz", for 5 print "Buzz", for both print "FizzBuzz".
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def count_primes(n):
    """
    Problem 47: Count Primes
    Count the number of prime numbers less than n.
    Input: n = 10
    Output: 4 (2, 3, 5, 7)
    """
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)


def my_sqrt(x):
    """
    Problem 48: Sqrt(x)
    Compute and return the square root of x (integer part only).
    Input: x = 8
    Output: 2
    """
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def climb_stairs(n):
    """
    Problem 49: Climbing Stairs
    How many distinct ways can you climb to the top if you can climb 1 or 2 steps?
    Input: n = 3
    Output: 3 (1+1+1, 1+2, 2+1)
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def excel_sheet_column_number(column_title):
    """
    Problem 50: Excel Sheet Column Number
    Convert Excel column title to its corresponding number.
    Input: columnTitle = "AB"
    Output: 28
    """
    result = 0
    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


# ============================ HASHMAPS & SETS ============================

def contains_nearby_duplicate(nums, k):
    """
    Problem 51: Contains Duplicate II
    Find if there are two indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
    Input: nums = [1,2,3,1], k = 3
    Output: true
    """
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


def is_isomorphic(s, t):
    """
    Problem 52: Isomorphic Strings
    Determine if two strings are isomorphic (can replace characters in s to get t).
    Input: s = "egg", t = "add"
    Output: true
    """
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


def word_pattern(pattern, s):
    """
    Problem 53: Word Pattern
    Check if s follows the same pattern.
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    """
    words = s.split()
    if len(pattern) != len(words):
        return False
    return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


def can_construct(ransom_note, magazine):
    """
    Problem 54: Ransom Note
    Check if ransomNote can be constructed from magazine letters.
    Input: ransomNote = "a", magazine = "b"
    Output: false
    """
    from collections import Counter
    return not (Counter(ransom_note) - Counter(magazine))


def find_restaurant(list1, list2):
    """
    Problem 55: Minimum Index Sum of Two Lists
    Find common strings with least index sum.
    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    Output: ["Shogun"]
    """
    index_map = {s: i for i, s in enumerate(list1)}
    min_sum = float('inf')
    result = []
    for j, s in enumerate(list2):
        if s in index_map:
            index_sum = j + index_map[s]
            if index_sum < min_sum:
                min_sum = index_sum
                result = [s]
            elif index_sum == min_sum:
                result.append(s)
    return result


# ============================ STACK & QUEUE ============================

def is_valid(s):
    """
    Problem 56: Valid Parentheses
    Determine if the input string has valid parentheses.
    Input: s = "()"
    Output: true
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


def implement_stack_using_queues():
    """
    Problem 57: Implement Stack using Queues
    Implement a LIFO stack using only two queues.
    """
    from collections import deque
    
    class MyStack:
        def __init__(self):
            self.queue = deque()
        
        def push(self, x):
            self.queue.append(x)
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
        
        def pop(self):
            return self.queue.popleft()
        
        def top(self):
            return self.queue[0]
        
        def empty(self):
            return len(self.queue) == 0
    
    return MyStack


def implement_queue_using_stacks():
    """
    Problem 58: Implement Queue using Stacks
    Implement a FIFO queue using only two stacks.
    """
    class MyQueue:
        def __init__(self):
            self.in_stack = []
            self.out_stack = []
        
        def push(self, x):
            self.in_stack.append(x)
        
        def pop(self):
            self._move()
            return self.out_stack.pop()
        
        def peek(self):
            self._move()
            return self.out_stack[-1]
        
        def empty(self):
            return not self.in_stack and not self.out_stack
        
        def _move(self):
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
    
    return MyQueue


# ============================ BIT MANIPULATION ============================

def hamming_weight(n):
    """
    Problem 59: Number of 1 Bits
    Return the number of '1' bits in the binary representation.
    Input: n = 00000000000000000000000000001011
    Output: 3
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def hamming_distance(x, y):
    """
    Problem 60: Hamming Distance
    The Hamming distance between two integers is the number of positions at which bits differ.
    Input: x = 1, y = 4
    Output: 2
    """
    return bin(x ^ y).count('1')


def reverse_bits(n):
    """
    Problem 61: Reverse Bits
    Reverse bits of a 32-bit unsigned integer.
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    """
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


def missing_number(nums):
    """
    Problem 62: Missing Number
    Find the missing number in array containing n distinct numbers from 0 to n.
    Input: nums = [3,0,1]
    Output: 2
    """
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


# ============================ GREEDY ============================

def can_place_flowers(flowerbed, n):
    """
    Problem 63: Can Place Flowers
    Can you plant n flowers without violating the no-adjacent-flowers rule?
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
    """
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
    return count >= n


def lemonade_change(bills):
    """
    Problem 64: Lemonade Change
    Each customer buys one lemonade for $5. Can you provide correct change to every customer?
    Input: bills = [5,5,5,10,20]
    Output: true
    """
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


# ============================ TWO POINTERS ============================

def merge(nums1, m, nums2, n):
    """
    Problem 65: Merge Sorted Array
    Merge nums2 into nums1 as one sorted array.
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    """
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


def is_palindrome_two_pointers(s):
    """
    Problem 66: Valid Palindrome (Two Pointers)
    Check if string is palindrome using two pointers.
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    """
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


def assign_cookies(g, s):
    """
    Problem 67: Assign Cookies
    Each child i has greed factor g[i], each cookie j has size s[j]. Maximize satisfied children.
    Input: g = [1,2,3], s = [1,1]
    Output: 1
    """
    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child


def find_content_children(g, s):
    """
    Problem 68: Assign Cookies (Alternative)
    Maximize the number of content children given greed factors and cookie sizes.
    Input: g = [1,2], s = [1,2,3]
    Output: 2
    """
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i


def is_long_pressed_name(name, typed):
    """
    Problem 69: Long Pressed Name
    Check if typed could have been typed when the keyboard might be held longer.
    Input: name = "alex", typed = "aaleex"
    Output: true
    """
    i = j = 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    return i == len(name)


def back_space_compare(s, t):
    """
    Problem 70: Backspace String Compare
    Given two strings with '#' meaning backspace, check if they are equal.
    Input: s = "ab#c", t = "ad#c"
    Output: true
    """
    def build(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return build(s) == build(t)


if __name__ == "__main__":
    print("=" * 60)
    print("EASY PROBLEMS (1-70) - DSA FUNDAMENTALS")
    print("=" * 60)
    print("\nSample Tests:")
    print(f"1. Two Sum: {two_sum([2, 7, 11, 15], 9)}")
    print(f"5. Max Profit: {max_profit([7, 1, 5, 3, 6, 4])}")
    print(f"19. Is Anagram: {is_anagram('anagram', 'nagaram')}")
    print(f"31. Max Depth: {max_depth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))}")
    print(f"49. Climb Stairs: {climb_stairs(5)}")
    print("=" * 60)
