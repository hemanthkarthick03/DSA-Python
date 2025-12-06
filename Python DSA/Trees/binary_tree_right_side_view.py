"""
BINARY TREE RIGHT SIDE VIEW - Medium
Return values of nodes visible from right side.

Logical Thinking:
1. BFS level order traversal
2. Last node in each level is visible
3. Collect rightmost nodes

Logical Thinking:
from collections import deque
def right_side_view(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Binary Tree Right Side View...")
    print("Add your test cases here")
