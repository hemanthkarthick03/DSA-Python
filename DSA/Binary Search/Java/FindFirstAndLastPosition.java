// LeetCode 34: Find First and Last Position of Element in Sorted Array
// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

public class FindFirstAndLastPosition {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[]{-1, -1};
        
        // Find first position
        result[0] = findFirst(nums, target);
        if (result[0] == -1) {
            return result;
        }
        
        // Find last position
        result[1] = findLast(nums, target);
        
        return result;
    }
    
    private int findFirst(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int first = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                first = mid;
                right = mid - 1; // Continue searching left
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return first;
    }
    
    private int findLast(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int last = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                last = mid;
                left = mid + 1; // Continue searching right
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return last;
    }
    
    public static void main(String[] args) {
        FindFirstAndLastPosition solution = new FindFirstAndLastPosition();
        int[] nums = {5, 7, 7, 8, 8, 10};
        int target = 8;
        
        int[] result = solution.searchRange(nums, target);
        System.out.println("First and last position: [" + result[0] + ", " + result[1] + "]");
    }
}