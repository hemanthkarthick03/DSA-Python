"""
CONTAINS DUPLICATE - Easy
Return true if any value appears at least twice in array.

Logical Thinking:
1. Use set to track seen values
2. If value already in set, return True
3. Otherwise add to set

Logical Thinking:
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Contains Duplicate...")
    print("Add your test cases here")
