"""
TWO SUM - Easy
Given array nums and target, return indices of two numbers that add to target.

Logical Thinking:
1. Use hashmap to store seen numbers
2. For each num, check if complement exists
3. Return indices when found

Logical Thinking:
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Two Sum...")
    print("Add your test cases here")
