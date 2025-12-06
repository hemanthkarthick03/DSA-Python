"""
PARTITION EQUAL SUBSET SUM - Medium
Check if array can be partitioned into two equal sum subsets.

Logical Thinking:
1. Target = sum / 2 (if odd, impossible)
2. Subset sum problem: can we make target?
3. DP: track all possible sums

Logical Thinking:
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = {0}
    for num in nums:
        dp = dp | {num + x for x in dp}
    return target in dp
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Partition Equal Subset Sum...")
    print("Add your test cases here")
