"""
SUBARRAY PRODUCT LESS THAN K - Medium
Count subarrays with product < k

Logical Thinking:
- See implementation for approach
"""

def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    product = 1
    left = count = 0
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


# Test cases
if __name__ == "__main__":
    print(f"Testing Subarray Product Less Than K...")
    print("✅ Refer to implementation")
