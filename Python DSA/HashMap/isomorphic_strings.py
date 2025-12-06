"""
ISOMORPHIC STRINGS - Easy
Two strings are isomorphic if characters can be replaced to get other.

Logical Thinking:
1. Create two mappings (s->t and t->s)
2. Check consistency for each character pair
3. Both mappings must be bijective

Logical Thinking:
def is_isomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Isomorphic Strings...")
    print("Add your test cases here")
