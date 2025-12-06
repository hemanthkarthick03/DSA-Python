"""
MINIMUM WINDOW SUBSTRING - Hard
Find minimum window in s that contains all characters of t.

Example: s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"

Logical Thinking:
1. Expand window until all chars of t are included
2. Contract window while maintaining all chars
3. Track minimum window that satisfies condition
4. Use frequency counters

Key: Sliding window, two frequency maps
Time: O(m + n) | Space: O(m + n)
"""

from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    formed = 0
    window_counts = {}
    
    left = right = 0
    ans = float("inf"), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# Test cases
if __name__ == "__main__":
    print(f"Testing Minimum Window Substring...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
