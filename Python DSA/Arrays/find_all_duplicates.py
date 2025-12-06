"""
FIND ALL DUPLICATES - Medium
Find all duplicates in array where 1 ≤ a[i] ≤ n
"""

def find_duplicates(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(index + 1)
        nums[index] = -nums[index]
    return result


if __name__ == "__main__":
    print("✅ Find All Duplicates")
