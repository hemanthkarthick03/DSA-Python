// LeetCode 217: Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array.

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        
        return false;
    }
    
    public static void main(String[] args) {
        ContainsDuplicate solution = new ContainsDuplicate();
        int[] nums1 = {1, 2, 3, 1};
        int[] nums2 = {1, 2, 3, 4};
        
        System.out.println("Contains duplicate: " + solution.containsDuplicate(nums1));
        System.out.println("Contains duplicate: " + solution.containsDuplicate(nums2));
    }
}