"""
PERFECT SQUARES - Medium
Minimum perfect squares that sum to n

Logical Thinking:
- See implementation for approach
"""

def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]


# Test cases
if __name__ == "__main__":
    print(f"Testing Perfect Squares...")
    print("✅ Refer to implementation")
