"""
SINGLE NUMBER - Easy
Find element that appears once (others appear twice).

Logical Thinking:
1. XOR all numbers
2. Duplicates cancel out (a ^ a = 0)
3. Result is single number

Logical Thinking:
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Single Number...")
    print("Add your test cases here")
