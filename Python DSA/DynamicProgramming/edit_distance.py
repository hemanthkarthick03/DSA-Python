"""
EDIT DISTANCE - Hard
Minimum operations to convert word1 to word2.

Logical Thinking:
1. DP: dp[i][j] = min ops to convert word1[0:i] to word2[0:j]
2. If chars match: dp[i][j] = dp[i-1][j-1]
3. Else: min(insert, delete, replace) + 1

Logical Thinking:
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Edit Distance...")
    print("Add your test cases here")
