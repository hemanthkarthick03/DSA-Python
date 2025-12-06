"""
MERGE K SORTED LISTS - Hard
Merge k sorted linked lists.

Logical Thinking:
1. Use min-heap with (value, index, node)
2. Pop minimum, add next node
3. Build result list

Logical Thinking:
import heapq
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    dummy = ListNode(0)
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Merge K Sorted Lists...")
    print("Add your test cases here")
