"""
DELETE AND EARN - Medium
Delete and earn points

Logical Thinking:
- See implementation for approach
"""

def delete_and_earn(nums):
    from collections import Counter
    points = Counter(nums)
    max_num = max(nums)
    prev2 = prev1 = 0
    for num in range(max_num + 1):
        curr = max(prev1, prev2 + num * points[num])
        prev2, prev1 = prev1, curr
    return prev1


# Test cases
if __name__ == "__main__":
    print(f"Testing Delete And Earn...")
    print("✅ Refer to implementation")
