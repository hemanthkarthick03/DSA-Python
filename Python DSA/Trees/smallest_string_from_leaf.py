"""
SMALLEST STRING FROM LEAF - Medium
Find lexicographically smallest string from leaf to root
"""

def smallest_from_leaf(root):
    def dfs(node, path):
        if not node:
            return
        path.append(chr(ord('a') + node.val))
        if not node.left and not node.right:
            result.append(''.join(reversed(path)))
        dfs(node.left, path)
        dfs(node.right, path)
        path.pop()
    result = []
    dfs(root, [])
    return min(result)


if __name__ == "__main__":
    print("✅ Smallest String From Leaf")
