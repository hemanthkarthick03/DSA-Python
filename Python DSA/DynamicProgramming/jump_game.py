"""
JUMP GAME - Medium
Check if can reach last index from first.

Logical Thinking:
1. Track farthest reachable position
2. For each position, update farthest
3. If farthest >= last index, return True

Logical Thinking:
def can_jump(nums):
    farthest = 0
    for i, num in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + num)
    return True
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Jump Game...")
    print("Add your test cases here")
