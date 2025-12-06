"""
SAME TREE - Easy
Check if two binary trees are same.

Logical Thinking:
1. If both None, return True
2. If one None, return False
3. Check values and recurse on children

Logical Thinking:
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Same Tree...")
    print("Add your test cases here")
