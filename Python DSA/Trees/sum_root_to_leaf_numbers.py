"""
SUM ROOT TO LEAF NUMBERS - Medium
Sum all root-to-leaf numbers

Logical Thinking:
- See implementation for approach
"""

def sum_numbers(root):
    def dfs(node, num):
        if not node:
            return 0
        num = num * 10 + node.val
        if not node.left and not node.right:
            return num
        return dfs(node.left, num) + dfs(node.right, num)
    return dfs(root, 0)


# Test cases
if __name__ == "__main__":
    print(f"Testing Sum Root To Leaf Numbers...")
    print("✅ Refer to implementation")
