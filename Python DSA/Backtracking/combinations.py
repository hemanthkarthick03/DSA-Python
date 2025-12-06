"""
COMBINATIONS - Medium
Generate all combinations of k numbers from 1 to n

Logical Thinking:
- See implementation for approach
"""

def combine(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Combinations...")
    print("✅ Refer to implementation")
