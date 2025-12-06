"""
INVERT BINARY TREE - Easy
Invert a binary tree (mirror image).

Logical Thinking:
1. Swap left and right children
2. Recursively invert left and right subtrees
3. Return root

Logical Thinking:
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Invert Binary Tree...")
    print("Add your test cases here")
