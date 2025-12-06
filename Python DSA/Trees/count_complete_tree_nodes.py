"""
COUNT COMPLETE TREE NODES - Medium
Count nodes in complete binary tree

Logical Thinking:
- See implementation for approach
"""

def count_nodes(root):
    if not root:
        return 0
    left_depth = right_depth = 0
    l = r = root
    while l:
        left_depth += 1
        l = l.left
    while r:
        right_depth += 1
        r = r.right
    if left_depth == right_depth:
        return (1 << left_depth) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Test cases
if __name__ == "__main__":
    print(f"Testing Count Complete Tree Nodes...")
    print("✅ Refer to implementation")
