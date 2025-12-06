"""
IPO - Hard
Maximize capital with k projects
"""

def find_maximized_capital(k, w, profits, capital):
    import heapq
    projects = sorted(zip(capital, profits))
    available = []
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(available, -projects[i][1])
            i += 1
        if not available:
            break
        w += -heapq.heappop(available)
    return w


if __name__ == "__main__":
    print("✅ Ipo")
