"""
NUMBER OF ISLANDS - Medium
Count number of islands in grid (1=land, 0=water).

Logical Thinking:
1. DFS/BFS from each unvisited land cell
2. Mark all connected cells as visited
3. Increment island count

Logical Thinking:
def num_islands(grid):
    if not grid:
        return 0
    count = 0
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Number Of Islands...")
    print("Add your test cases here")
