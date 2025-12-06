"""
MAXIMUM DEPTH OF BINARY TREE - Easy
Find maximum depth of binary tree.

Logical Thinking:
1. Recursively calculate depth of left and right
2. Return max + 1
3. Base case: None returns 0

Logical Thinking:
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Maximum Depth Of Binary Tree...")
    print("Add your test cases here")
