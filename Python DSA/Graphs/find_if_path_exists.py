"""
FIND IF PATH EXISTS - Easy
Check if path exists in graph

Logical Thinking:
- See implementation for approach
"""

def valid_path(n, edges, source, destination):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False


# Test cases
if __name__ == "__main__":
    print(f"Testing Find If Path Exists...")
    print("✅ Refer to implementation")
