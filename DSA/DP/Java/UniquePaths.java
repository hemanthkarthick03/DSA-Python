// LeetCode 62: Unique Paths
// There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).

public class UniquePaths {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        // Initialize first row and first column
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Fill the dp table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        return dp[m - 1][n - 1];
    }
    
    // Space optimized approach
    public int uniquePathsOptimized(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        
        return dp[n - 1];
    }
    
    // Mathematical approach using combinations
    public int uniquePathsMath(int m, int n) {
        long result = 1;
        
        for (int i = 1; i < m; i++) {
            result = result * (n - 1 + i) / i;
        }
        
        return (int) result;
    }
    
    public static void main(String[] args) {
        UniquePaths solution = new UniquePaths();
        
        int[][] testCases = {{3, 7}, {3, 2}, {7, 3}, {3, 3}};
        
        for (int[] test : testCases) {
            int m = test[0], n = test[1];
            System.out.println("Unique paths for " + m + "x" + n + " grid: " + 
                             solution.uniquePaths(m, n));
        }
    }
}