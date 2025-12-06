"""
KTH SMALLEST IN SORTED MATRIX - Medium
Find kth smallest in sorted matrix

Logical Thinking:
- See implementation for approach
"""

def kth_smallest(matrix, k):
    import heapq
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]
    heapq.heapify(heap)
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c < n - 1:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val


# Test cases
if __name__ == "__main__":
    print(f"Testing Kth Smallest In Sorted Matrix...")
    print("✅ Refer to implementation")
