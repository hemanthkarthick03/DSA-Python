"""
MOVE ZEROES - Easy
Move all zeros to end

Logical Thinking:
- See implementation for approach
"""

def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


# Test cases
if __name__ == "__main__":
    print(f"Testing Move Zeroes...")
    print("✅ Refer to implementation")
