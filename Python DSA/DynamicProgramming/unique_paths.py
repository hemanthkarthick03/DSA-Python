"""
UNIQUE PATHS - Medium
Count unique paths in m x n grid from top-left to bottom-right.

Logical Thinking:
1. DP: dp[i][j] = paths to reach (i, j)
2. dp[i][j] = dp[i-1][j] + dp[i][j-1]
3. Can optimize to 1D array

Logical Thinking:
def unique_paths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Unique Paths...")
    print("Add your test cases here")
