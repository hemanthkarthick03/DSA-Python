"""
SYMMETRIC TREE - Easy
Check if tree is symmetric around center.

Logical Thinking:
1. Helper function to check if two trees are mirrors
2. Compare left subtree with right subtree
3. Recursive comparison

Logical Thinking:
def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    return is_mirror(root, root)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Symmetric Tree...")
    print("Add your test cases here")
