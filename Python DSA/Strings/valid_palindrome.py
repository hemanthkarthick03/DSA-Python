"""
VALID PALINDROME - Easy
Check if string is palindrome considering only alphanumeric characters.

Example: s = "A man, a plan, a canal: Panama" → Output: true

Logical Thinking:
1. Two pointers from both ends
2. Skip non-alphanumeric characters
3. Compare characters (case-insensitive)
4. Move towards center

Key: Two pointers, character validation
Time: O(n) | Space: O(1)
"""

def is_palindrome(s):
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


# Test cases
if __name__ == "__main__":
    print(f"Testing Valid Palindrome...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
