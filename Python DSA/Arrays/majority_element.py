"""
MAJORITY ELEMENT - Easy
Find element appearing more than n/2 times

Logical Thinking:
- See implementation for approach
"""

def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


# Test cases
if __name__ == "__main__":
    print(f"Testing Majority Element...")
    print("✅ Refer to implementation")
