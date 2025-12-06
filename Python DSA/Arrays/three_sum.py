"""

-1 0 1 2 -1 -4
-4 -1 -1 0 1 2
    i  j     k


THREE SUM - Medium

Problem:
Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Logical Thinking:
1. Sort array first for two-pointer technique
2. Fix one number, find two others using two pointers
3. Skip duplicates to avoid duplicate triplets
4. Left pointer moves right, right pointer moves left
5. If sum < 0, move left pointer; if sum > 0, move right pointer

Key Concepts: Sorting, Two Pointers, Skip Duplicates
Time: O(n²) | Space: O(1)
"""

def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


# Test cases
if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 1, 1]) == []
    print("✅ All test cases passed!")
