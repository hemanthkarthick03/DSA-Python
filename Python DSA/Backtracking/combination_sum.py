"""
COMBINATION SUM - Medium
Find all combinations that sum to target.

Logical Thinking:
1. Try each candidate
2. Recurse with reduced target
3. Backtrack and try next candidate

Logical Thinking:
def combination_sum(candidates, target):
    result = []
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
    backtrack(0, target, [])
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Combination Sum...")
    print("Add your test cases here")
