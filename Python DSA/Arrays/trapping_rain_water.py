"""
TRAPPING RAIN WATER - Hard
Given elevation map, compute how much water can be trapped after raining.

Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] → Output: 6

Logical Thinking:
1. Water at position i = min(max_left, max_right) - height[i]
2. Precompute max heights from left and right
3. For each position, calculate trapped water
4. Alternative: Two pointers with tracking max heights

Key: DP or Two Pointers, understand water level concept
Time: O(n) | Space: O(n) or O(1)
"""

def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water


# Test cases
if __name__ == "__main__":
    print(f"Testing Trapping Rain Water...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
