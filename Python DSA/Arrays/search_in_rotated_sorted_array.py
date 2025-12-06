"""
SEARCH IN ROTATED SORTED ARRAY - Medium
Search target in rotated sorted array in O(log n).

Example: nums = [4,5,6,7,0,1,2], target = 0 → Output: 4

Logical Thinking:
1. Modified binary search
2. Determine which half is sorted
3. Check if target is in sorted half
4. Adjust search boundaries accordingly

Key: Binary search with rotation handling
Time: O(log n) | Space: O(1)
"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# Test cases
if __name__ == "__main__":
    print(f"Testing Search In Rotated Sorted Array...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
