"""
FIND MINIMUM IN ROTATED SORTED ARRAY - Medium
Find minimum element in rotated sorted array.

Example: nums = [3,4,5,1,2] → Output: 1

Logical Thinking:
1. Binary search but compare mid with right
2. If mid > right: minimum is in right half
3. If mid < right: minimum is in left half (including mid)
4. Handle edge case of no rotation

Key: Modified binary search, pivot detection
Time: O(log n) | Space: O(1)
"""

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# Test cases
if __name__ == "__main__":
    print(f"Testing Find Minimum In Rotated Sorted Array...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
