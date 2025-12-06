"""
CLONE GRAPH - Medium
Deep clone an undirected graph.

Logical Thinking:
1. Use hashmap to store cloned nodes
2. DFS/BFS to traverse graph
3. Clone neighbors recursively

Logical Thinking:
def clone_graph(node):
    if not node:
        return None
    clones = {}
    def dfs(n):
        if n in clones:
            return clones[n]
        clone = Node(n.val)
        clones[n] = clone
        clone.neighbors = [dfs(neighbor) for neighbor in n.neighbors]
        return clone
    return dfs(node)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Clone Graph...")
    print("Add your test cases here")
