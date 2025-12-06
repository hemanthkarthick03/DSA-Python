"""
SUBSETS - Medium
Generate all possible subsets.

Logical Thinking:
1. For each element: include or exclude
2. Backtrack to explore both choices
3. Add each subset to result

Logical Thinking:
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Subsets...")
    print("Add your test cases here")
