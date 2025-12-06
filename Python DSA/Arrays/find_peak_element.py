"""
FIND PEAK ELEMENT - Medium
Find peak element in O(log n)

Logical Thinking:
- See implementation for approach
"""

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


# Test cases
if __name__ == "__main__":
    print(f"Testing Find Peak Element...")
    print("✅ Refer to implementation")
