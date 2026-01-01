// LeetCode 70: Climbing Stairs
// You are climbing a staircase. It takes n steps to reach the top.

public class ClimbingStairs {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        
        int prev2 = 1; // f(1)
        int prev1 = 2; // f(2)
        
        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    // Recursive approach with memoization
    public int climbStairsMemo(int n) {
        int[] memo = new int[n + 1];
        return climbStairsHelper(n, memo);
    }
    
    private int climbStairsHelper(int n, int[] memo) {
        if (n <= 2) {
            return n;
        }
        
        if (memo[n] != 0) {
            return memo[n];
        }
        
        memo[n] = climbStairsHelper(n - 1, memo) + climbStairsHelper(n - 2, memo);
        return memo[n];
    }
    
    public static void main(String[] args) {
        ClimbingStairs solution = new ClimbingStairs();
        
        int[] testCases = {2, 3, 4, 5, 10};
        
        for (int n : testCases) {
            System.out.println("Ways to climb " + n + " stairs: " + solution.climbStairs(n));
        }
    }
}