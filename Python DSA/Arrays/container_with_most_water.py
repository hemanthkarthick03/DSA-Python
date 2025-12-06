"""
CONTAINER WITH MOST WATER - Medium
Given array height, find two lines that form container with most water.

Example: height = [1,8,6,2,5,4,8,3,7] → Output: 49

Logical Thinking:
1. Two pointers at both ends (widest container)
2. Calculate area = min(height[left], height[right]) * width
3. Move pointer with smaller height (potential for taller line)
4. Keep track of maximum area found

Key: Two pointers, greedy move shorter height
Time: O(n) | Space: O(1)
"""

def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


# Test cases
if __name__ == "__main__":
    print(f"Testing Container With Most Water...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
