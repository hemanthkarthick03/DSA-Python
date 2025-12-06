"""
N QUEENS - Hard
Place n queens on n×n chessboard.

Logical Thinking:
1. Try placing queen in each row
2. Check if position is safe (no attacks)
3. Backtrack if no valid position

Logical Thinking:
def solve_n_queens(n):
    def is_safe(row, col):
        return not (cols[col] or diag1[row - col] or diag2[row + col])
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                cols[col] = diag1[row - col] = diag2[row + col] = True
                backtrack(row + 1)
                board[row][col] = '.'
                cols[col] = diag1[row - col] = diag2[row + col] = False
    
    result = []
    board = [['.'] * n for _ in range(n)]
    cols = [False] * n
    diag1 = {}
    diag2 = {}
    backtrack(0)
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing N Queens...")
    print("Add your test cases here")
