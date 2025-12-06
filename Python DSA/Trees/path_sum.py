"""
PATH SUM - Easy
Check if tree has root-to-leaf path with target sum.

Logical Thinking:
1. Subtract current value from target
2. Check if leaf node with sum 0
3. Recurse on children

Logical Thinking:
def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    target_sum -= root.val
    return has_path_sum(root.left, target_sum) or has_path_sum(root.right, target_sum)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Path Sum...")
    print("Add your test cases here")
