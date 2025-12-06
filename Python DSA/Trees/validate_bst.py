"""
VALIDATE BST - Medium
Validate if tree is valid BST.

Logical Thinking:
1. Use bounds (min, max) for each node
2. Left child must be less than node
3. Right child must be greater than node

Logical Thinking:
def is_valid_BST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return is_valid_BST(root.left, min_val, root.val) and is_valid_BST(root.right, root.val, max_val)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Validate Bst...")
    print("Add your test cases here")
