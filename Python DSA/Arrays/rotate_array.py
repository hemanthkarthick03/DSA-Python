"""
ROTATE ARRAY - Medium
Rotate array to the right by k steps.

Example: nums = [1,2,3,4,5,6,7], k = 3 → [5,6,7,1,2,3,4]

Logical Thinking:
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements
4. Three reversals achieve rotation in-place

Key: Reversal algorithm, in-place modification
Time: O(n) | Space: O(1)
"""

def rotate(nums, k):
    k = k % len(nums)
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    print(f"Testing Rotate Array...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
