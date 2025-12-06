"""
LONGEST SUBSTRING WITHOUT REPEATING - Medium
Find length of longest substring without repeating characters.

Example: s = "abcabcbb" → Output: 3 ("abc")

Logical Thinking:
1. Sliding window with hashmap
2. Expand window by moving right pointer
3. If duplicate found, shrink from left
4. Track maximum window size

Key: Sliding window, hashmap for seen characters
Time: O(n) | Space: O(min(n, charset))
"""

def length_of_longest_substring(s):
    seen = {}
    left = max_len = 0
    
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len


# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Substring Without Repeating...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
