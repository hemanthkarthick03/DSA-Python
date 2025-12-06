"""
LOWEST COMMON ANCESTOR BST - Easy
Find LCA of two nodes in BST.

Logical Thinking:
1. Use BST property
2. If both nodes less than root, go left
3. If both greater, go right
4. Otherwise, current is LCA

Logical Thinking:
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Lowest Common Ancestor Bst...")
    print("Add your test cases here")
