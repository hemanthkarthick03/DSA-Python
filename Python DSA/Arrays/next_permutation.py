"""
NEXT PERMUTATION - Medium
Find next lexicographically greater permutation

Logical Thinking:
1. Find first decreasing element from right
2. Swap with next greater
3. Reverse suffix
"""

def next_permutation(nums):
    if not nums:
        return False

    n = len(nums)
    # 1. Find pivot: first index from right where nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i == -1:
        # Entire sequence is non-increasing -> this is the last permutation
        nums.reverse()
        return False

    # 2. Find rightmost successor to pivot in the suffix
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Swap pivot and successor
    nums[i], nums[j] = nums[j], nums[i]

    # 3. Reverse the suffix starting at i+1
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return True


# Test cases
if __name__ == "__main__":
    print("Testing Next Permutation...")
    cases = [
        [1, 2, 3],
        [1, 3, 2],
        [3, 2, 1],
        [1, 1, 5],
        [],
        [1],
    ]
    for case in cases:
        arr = case[:]  # copy to avoid mutating original in display
        changed = next_permutation(arr)
        print(f"input: {case} -> changed: {changed}, next: {arr}")
