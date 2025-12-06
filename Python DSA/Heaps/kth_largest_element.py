"""
KTH LARGEST ELEMENT - Medium
Find kth largest element in array.

Logical Thinking:
1. Use min-heap of size k
2. Maintain k largest elements
3. Root is kth largest

Logical Thinking:
import heapq
def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Kth Largest Element...")
    print("Add your test cases here")
