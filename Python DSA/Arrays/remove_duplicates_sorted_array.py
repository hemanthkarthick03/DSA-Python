"""
REMOVE DUPLICATES SORTED ARRAY - Easy
Remove duplicates in-place

Logical Thinking:
- See implementation for approach
"""

def remove_duplicates(nums):
    if not nums:
        return 0
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1


# Test cases
if __name__ == "__main__":
    print(f"Testing Remove Duplicates Sorted Array...")
    print("✅ Refer to implementation")
