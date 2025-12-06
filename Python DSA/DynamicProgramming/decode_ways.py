"""
DECODE WAYS - Medium
Count ways to decode a digit string (1=A, 2=B, ..., 26=Z).

Logical Thinking:
1. DP: dp[i] = ways to decode s[0:i]
2. Single digit (1-9): add dp[i-1]
3. Two digits (10-26): add dp[i-2]

Logical Thinking:
def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    prev2, prev1 = 1, 1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != '0':
            curr = prev1
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2
        prev2, prev1 = prev1, curr
    return prev1
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Decode Ways...")
    print("Add your test cases here")
