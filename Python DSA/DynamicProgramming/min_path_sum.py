"""
MIN PATH SUM - Medium
Find minimum path sum in grid

Logical Thinking:
- See implementation for approach
"""

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


# Test cases
if __name__ == "__main__":
    print(f"Testing Min Path Sum...")
    print("✅ Refer to implementation")
