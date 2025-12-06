"""
MAXIMUM SUBARRAY - Medium
Find contiguous subarray with the largest sum (Kadane's Algorithm).

Example: nums = [-2,1,-3,4,-1,2,1,-5,4] → Output: 6

Logical Thinking:
1. Current sum = max(current_num, current_sum + current_num)
2. At each position, decide: start new subarray or extend?
3. Track global maximum
4. If current sum becomes negative, reset

Key: Kadane's Algorithm, DP thinking
Time: O(n) | Space: O(1)
"""

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Test cases
if __name__ == "__main__":
    print(f"Testing Maximum Subarray...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
