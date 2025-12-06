"""
HOUSE ROBBER - Medium
Rob houses without alerting adjacent houses.

Logical Thinking:
1. For each house: max(rob this + skip previous, skip this)
2. Track max money with/without robbing current
3. Return maximum

Logical Thinking:
def rob(nums):
    prev2 = prev1 = 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing House Robber...")
    print("Add your test cases here")
