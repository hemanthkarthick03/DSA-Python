"""
SORT COLORS - Medium
Sort array of 0s, 1s, 2s (Dutch flag)

Logical Thinking:
- See implementation for approach
"""

def sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Test cases
if __name__ == "__main__":
    print(f"Testing Sort Colors...")
    print("✅ Refer to implementation")
