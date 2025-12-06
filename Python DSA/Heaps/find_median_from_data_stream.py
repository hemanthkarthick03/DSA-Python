"""
FIND MEDIAN FROM DATA STREAM - Hard
Find median from stream of numbers.

Logical Thinking:
1. Use two heaps: max-heap (lower half) and min-heap (upper half)
2. Balance heaps to ensure size difference <= 1
3. Median is top of larger heap or average of both tops

Logical Thinking:
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    
    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Find Median From Data Stream...")
    print("Add your test cases here")
