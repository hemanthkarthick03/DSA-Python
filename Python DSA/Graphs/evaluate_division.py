"""
EVALUATE DIVISION - Medium
Evaluate division queries with variable equations
"""

def calc_equation(equations, values, queries):
    from collections import defaultdict
    graph = defaultdict(dict)
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val
    
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return graph[start][neighbor] * result
        return -1.0
    
    return [dfs(a, b, set()) for a, b in queries]


if __name__ == "__main__":
    print("✅ Evaluate Division")
