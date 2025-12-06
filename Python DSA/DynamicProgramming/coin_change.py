"""
COIN CHANGE - Medium
Find minimum coins needed to make amount.

Logical Thinking:
1. DP array: dp[i] = min coins for amount i
2. For each coin, update all reachable amounts
3. Return dp[amount]

Logical Thinking:
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Coin Change...")
    print("Add your test cases here")
