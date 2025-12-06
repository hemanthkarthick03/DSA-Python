"""
TWO SUM - Easy

Problem:
Given an array of integers nums and an integer target, return indices of two 
numbers that add up to target. Each input has exactly one solution.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Logical Thinking:
1. Brute Force: Check every pair - O(n²) time
2. Optimized: Use hashmap to store complements - O(n) time
3. For each number, check if (target - number) exists in hashmap
4. Store number with its index for quick lookup

Key Concepts: HashMap, Complement Pattern
Time: O(n) | Space: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Test cases
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✅ All test cases passed!")
