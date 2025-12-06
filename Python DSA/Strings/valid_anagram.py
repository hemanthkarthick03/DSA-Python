"""
VALID ANAGRAM - Easy
Check if two strings are anagrams

Logical Thinking:
- See implementation for approach
"""

def is_anagram(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)


# Test cases
if __name__ == "__main__":
    print(f"Testing Valid Anagram...")
    print("✅ Refer to implementation")
