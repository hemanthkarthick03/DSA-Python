"""
LONGEST CONSECUTIVE SEQUENCE - Medium
Find length of longest consecutive elements sequence in unsorted array.

Logical Thinking:
1. Convert to set for O(1) lookup
2. For each number, check if it's start of sequence
3. Count consecutive numbers

Logical Thinking:
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)
    return longest
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Consecutive Sequence...")
    print("Add your test cases here")
