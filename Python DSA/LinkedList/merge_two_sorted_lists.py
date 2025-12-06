"""
MERGE TWO SORTED LISTS - Easy
Merge two sorted linked lists.

Logical Thinking:
1. Create dummy node
2. Compare values and append smaller
3. Handle remaining nodes

Logical Thinking:
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Merge Two Sorted Lists...")
    print("Add your test cases here")
