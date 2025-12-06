"""
ALL PATHS SOURCE TO TARGET - Medium
Find all paths from source to target

Logical Thinking:
- See implementation for approach
"""

def all_paths_source_target(graph):
    result = []
    def dfs(node, path):
        if node == len(graph) - 1:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    dfs(0, [0])
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing All Paths Source To Target...")
    print("✅ Refer to implementation")
