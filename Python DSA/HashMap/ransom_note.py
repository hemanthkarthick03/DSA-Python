"""
RANSOM NOTE - Easy
Can ransom note be constructed using letters from magazine?

Logical Thinking:
1. Count letters in magazine
2. Check if all letters in note are available
3. Use Counter for easy comparison

Logical Thinking:
from collections import Counter
def can_construct(note, magazine):
    return not (Counter(note) - Counter(magazine))
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Ransom Note...")
    print("Add your test cases here")
