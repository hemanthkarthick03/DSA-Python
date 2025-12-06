"""
MISSING NUMBER - Easy
Find missing number in array 0 to n.

Logical Thinking:
1. XOR all numbers and indices
2. Missing number will remain
3. Alternative: sum formula

Logical Thinking:
def missing_number(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Missing Number...")
    print("Add your test cases here")
