"""
LONGEST PALINDROMIC SUBSEQUENCE - Medium
Find LPS length

Logical Thinking:
1. DP: dp[i][j] = LPS in s[i:j]
2. If s[i]==s[j]: dp[i][j] = 2 + dp[i+1][j-1]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Palindromic Subsequence...")
    print("Add your test cases here")
