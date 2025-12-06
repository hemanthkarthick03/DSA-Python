"""
COUNTING BITS - Easy
Count 1 bits for numbers 0 to n.

Logical Thinking:
1. DP: dp[i] = dp[i >> 1] + (i & 1)
2. Use previous results
3. Right shift removes last bit

Logical Thinking:
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Counting Bits...")
    print("Add your test cases here")
