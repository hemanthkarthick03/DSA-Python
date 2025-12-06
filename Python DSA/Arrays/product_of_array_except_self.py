"""
PRODUCT OF ARRAY EXCEPT SELF - Medium
Return array where output[i] = product of all elements except nums[i].
Cannot use division and must be O(n).

Example: nums = [1,2,3,4] → Output: [24,12,8,6]

Logical Thinking:
1. Build prefix products (left to right)
2. Build suffix products (right to left) 
3. Combine: output[i] = prefix[i-1] * suffix[i+1]
4. Optimize: Use output array to store prefix, then multiply suffix

Key: Prefix/Suffix pattern, no division needed
Time: O(n) | Space: O(1) excluding output
"""

def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    
    return output


# Test cases
if __name__ == "__main__":
    print(f"Testing Product Of Array Except Self...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
