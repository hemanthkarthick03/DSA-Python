"""
PERMUTATIONS - Medium
Generate all permutations of array.

Logical Thinking:
1. Swap elements to generate permutations
2. Backtrack after each swap
3. Use used array or swapping technique

Logical Thinking:
def permute(nums):
    result = []
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    backtrack([])
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Permutations...")
    print("Add your test cases here")
