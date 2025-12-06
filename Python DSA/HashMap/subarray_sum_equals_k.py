"""
SUBARRAY SUM EQUALS K - Medium
Find total number of subarrays whose sum equals k.

Logical Thinking:
1. Use prefix sum concept
2. Track cumulative sums in hashmap
3. Check if (current_sum - k) exists

Logical Thinking:
from collections import defaultdict
def subarray_sum(nums, k):
    count = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1
    curr_sum = 0
    for num in nums:
        curr_sum += num
        count += sum_map[curr_sum - k]
        sum_map[curr_sum] += 1
    return count
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Subarray Sum Equals K...")
    print("Add your test cases here")
