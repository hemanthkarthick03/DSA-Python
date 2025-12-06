"""
IMPLEMENT STRSTR - Easy
Return index of first occurrence of needle in haystack, or -1.

Example: haystack = "hello", needle = "ll" → Output: 2

Logical Thinking:
1. Slide needle over haystack
2. Compare characters when first char matches
3. Advanced: KMP algorithm for O(n+m)
4. Simple: Built-in find() or manual iteration

Key: String matching, sliding pattern
Time: O(n*m) simple | Space: O(1)
"""

def str_str(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


# Test cases
if __name__ == "__main__":
    print(f"Testing Implement Strstr...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
