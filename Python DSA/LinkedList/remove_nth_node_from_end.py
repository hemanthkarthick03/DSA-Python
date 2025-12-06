"""
REMOVE NTH NODE FROM END - Medium
Remove nth node from end of list.

Logical Thinking:
1. Use two pointers with n gap
2. Move both until fast reaches end
3. Remove node at slow pointer

Logical Thinking:
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Remove Nth Node From End...")
    print("Add your test cases here")
