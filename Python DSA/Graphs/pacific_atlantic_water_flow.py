"""
PACIFIC ATLANTIC WATER FLOW - Medium
Find cells from which water can flow to both oceans.

Logical Thinking:
1. DFS from Pacific coast cells
2. DFS from Atlantic coast cells
3. Return intersection of reachable cells

Logical Thinking:
def pacific_atlantic(heights):
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(i, j, ocean):
        ocean.add((i, j))
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in ocean and heights[ni][nj] >= heights[i][j]:
                dfs(ni, nj, ocean)
    
    for i in range(m):
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    for j in range(n):
        dfs(0, j, pacific)
        dfs(m - 1, j, atlantic)
    
    return list(pacific & atlantic)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Pacific Atlantic Water Flow...")
    print("Add your test cases here")
