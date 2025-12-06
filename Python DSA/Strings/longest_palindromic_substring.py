"""
LONGEST PALINDROMIC SUBSTRING - Medium
Find the longest palindromic substring in s.

Example: s = "babad" → Output: "bab" or "aba"

Logical Thinking:
1. Expand around center for each position
2. Consider odd length (single center) and even length (two centers)
3. Track maximum palindrome found
4. Alternative: DP but less space efficient

Key: Expand around center, two cases (odd/even)
Time: O(n²) | Space: O(1)
"""

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Palindromic Substring...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
