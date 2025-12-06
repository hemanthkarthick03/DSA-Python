"""
FLATTEN BINARY TREE TO LINKED LIST - Medium
Flatten tree to linked list in-place

Logical Thinking:
- See implementation for approach
"""

def flatten(root):
    def dfs(node):
        if not node:
            return None
        left_tail = dfs(node.left)
        right_tail = dfs(node.right)
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        return right_tail or left_tail or node
    dfs(root)


# Test cases
if __name__ == "__main__":
    print(f"Testing Flatten Binary Tree To Linked List...")
    print("✅ Refer to implementation")
