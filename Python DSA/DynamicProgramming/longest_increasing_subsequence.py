"""
LONGEST INCREASING SUBSEQUENCE - Medium
Find length of longest increasing subsequence.

Logical Thinking:
1. DP: dp[i] = LIS ending at i
2. For each j < i, if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
3. Return max(dp)

Logical Thinking:
def length_of_LIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Increasing Subsequence...")
    print("Add your test cases here")
