"""
BEST TIME TO BUY SELL STOCK - Easy
Given an array prices where prices[i] is the price of stock on ith day,
find maximum profit from one buy and one sell transaction.

Example: prices = [7,1,5,3,6,4] → Output: 5

Logical Thinking:
1. Track minimum price seen so far
2. Calculate profit if we sell at current price
3. Update max profit if current profit is better
4. One pass solution - no need to check all pairs

Key: Greedy approach, keep track of min and max profit
Time: O(n) | Space: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


# Test cases
if __name__ == "__main__":
    print(f"Testing Best Time To Buy Sell Stock...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
