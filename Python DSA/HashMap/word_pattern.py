"""
WORD PATTERN - Easy
Check if string follows same pattern.

Logical Thinking:
1. Split string into words
2. Create bijective mapping
3. Verify pattern matches

Logical Thinking:
def word_pattern(pattern, s):
    words = s.split()
    return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Word Pattern...")
    print("Add your test cases here")
