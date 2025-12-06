"""
BINARY TREE ZIGZAG TRAVERSAL - Medium
Return zigzag level order traversal.

Logical Thinking:
1. BFS with level tracking
2. Alternate between left-to-right and right-to-left
3. Use flag to reverse alternate levels

Logical Thinking:
from collections import deque
def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Binary Tree Zigzag Traversal...")
    print("Add your test cases here")
