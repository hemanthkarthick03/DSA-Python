"""
WORD BREAK - Medium
Check if string can be segmented into dictionary words.

Logical Thinking:
1. DP: dp[i] = can break s[0:i]
2. For each position, check all possible words
3. dp[i] = True if any word ends at i and dp[start] is True

Logical Thinking:
def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    word_set = set(word_dict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Word Break...")
    print("Add your test cases here")
