"""
FIRST UNIQUE CHAR - Easy
Find first non-repeating character

Logical Thinking:
- See implementation for approach
"""

def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# Test cases
if __name__ == "__main__":
    print(f"Testing First Unique Char...")
    print("✅ Refer to implementation")
