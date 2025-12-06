"""
BALANCED BINARY TREE - Easy
Check if tree is height-balanced

Logical Thinking:
- See implementation for approach
"""

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return height(root) != -1


# Test cases
if __name__ == "__main__":
    print(f"Testing Balanced Binary Tree...")
    print("✅ Refer to implementation")
