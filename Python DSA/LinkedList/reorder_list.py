"""
REORDER LIST - Medium
Reorder list to L0→Ln→L1→Ln-1→L2→Ln-2...

Logical Thinking:
1. Find middle
2. Reverse second half
3. Merge two halves alternately

Logical Thinking:
def reorder_list(head):
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev, curr = None, slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    
    first, second = head, prev
    while second.next:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Reorder List...")
    print("Add your test cases here")
