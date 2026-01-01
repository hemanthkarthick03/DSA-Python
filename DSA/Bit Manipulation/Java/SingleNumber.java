// LeetCode 136: Single Number
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

public class SingleNumber {
    public int singleNumber(int[] nums) {
        int result = 0;
        
        // XOR all numbers - duplicates will cancel out
        for (int num : nums) {
            result ^= num;
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        SingleNumber solution = new SingleNumber();
        int[] nums1 = {2, 2, 1};
        int[] nums2 = {4, 1, 2, 1, 2};
        
        System.out.println("Single number: " + solution.singleNumber(nums1));
        System.out.println("Single number: " + solution.singleNumber(nums2));
    }
}