"""
MAXIMUM PRODUCT SUBARRAY - Medium
Find maximum product subarray

Logical Thinking:
- See implementation for approach
"""

def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        temp_max = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        max_prod = temp_max
        result = max(result, max_prod)
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Maximum Product Subarray...")
    print("✅ Refer to implementation")
