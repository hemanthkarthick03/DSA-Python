// LeetCode 322: Coin Change
// You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

import java.util.Arrays;

public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
    
    // Alternative approach using DFS with memoization
    public int coinChangeDFS(int[] coins, int amount) {
        int[] memo = new int[amount + 1];
        Arrays.fill(memo, -2);
        return dfs(coins, amount, memo);
    }
    
    private int dfs(int[] coins, int amount, int[] memo) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;
        
        if (memo[amount] != -2) {
            return memo[amount];
        }
        
        int minCoins = Integer.MAX_VALUE;
        for (int coin : coins) {
            int result = dfs(coins, amount - coin, memo);
            if (result != -1) {
                minCoins = Math.min(minCoins, result + 1);
            }
        }
        
        memo[amount] = minCoins == Integer.MAX_VALUE ? -1 : minCoins;
        return memo[amount];
    }
    
    public static void main(String[] args) {
        CoinChange solution = new CoinChange();
        
        int[] coins1 = {1, 3, 4};
        int amount1 = 6;
        
        int[] coins2 = {2};
        int amount2 = 3;
        
        System.out.println("Min coins needed: " + solution.coinChange(coins1, amount1));
        System.out.println("Min coins needed: " + solution.coinChange(coins2, amount2));
    }
}