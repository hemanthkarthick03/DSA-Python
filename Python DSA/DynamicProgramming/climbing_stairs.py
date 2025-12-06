"""
CLIMBING STAIRS - Easy
Count ways to climb n stairs (1 or 2 steps at a time).

Logical Thinking:
1. Base: 1 way for 1 stair, 2 ways for 2 stairs
2. Current ways = ways[i-1] + ways[i-2]
3. Fibonacci pattern

Logical Thinking:
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Climbing Stairs...")
    print("Add your test cases here")
