"""
COURSE SCHEDULE - Medium
Check if can finish all courses (detect cycle in directed graph).

Logical Thinking:
1. Build adjacency list
2. DFS with three states: unvisited, visiting, visited
3. If visiting node is encountered again, cycle exists

Logical Thinking:
def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    state = [0] * num_courses
    
    def has_cycle(course):
        if state[course] == 1:
            return True
        if state[course] == 2:
            return False
        state[course] = 1
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        state[course] = 2
        return False
    
    return not any(has_cycle(i) for i in range(num_courses))
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Course Schedule...")
    print("Add your test cases here")
