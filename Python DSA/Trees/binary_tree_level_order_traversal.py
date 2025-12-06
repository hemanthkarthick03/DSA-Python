"""
BINARY TREE LEVEL ORDER TRAVERSAL - Medium
Return level order traversal of binary tree.

Logical Thinking:
1. Use BFS with queue
2. Process nodes level by level
3. Store each level in separate list

Logical Thinking:
from collections import deque
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Binary Tree Level Order Traversal...")
    print("Add your test cases here")
