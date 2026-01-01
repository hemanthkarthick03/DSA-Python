// LeetCode 198: House Robber
// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.

public class HouseRobber {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        
        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    // Alternative approach using DP array
    public int robDP(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        
        return dp[nums.length - 1];
    }
    
    // Recursive approach with memoization
    public int robMemo(int[] nums) {
        int[] memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return robHelper(nums, nums.length - 1, memo);
    }
    
    private int robHelper(int[] nums, int i, int[] memo) {
        if (i < 0) return 0;
        if (i == 0) return nums[0];
        
        if (memo[i] != -1) return memo[i];
        
        memo[i] = Math.max(robHelper(nums, i - 1, memo), 
                          robHelper(nums, i - 2, memo) + nums[i]);
        return memo[i];
    }
    
    public static void main(String[] args) {
        HouseRobber solution = new HouseRobber();
        
        int[] nums1 = {1, 2, 3, 1};
        int[] nums2 = {2, 7, 9, 3, 1};
        
        System.out.println("Max money robbed: " + solution.rob(nums1));
        System.out.println("Max money robbed: " + solution.rob(nums2));
    }
}