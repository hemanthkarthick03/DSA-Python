"""
MIDDLE OF LINKED LIST - Easy
Find middle node of linked list.

Logical Thinking:
1. Use slow and fast pointers
2. Fast moves twice as fast
3. When fast reaches end, slow is at middle

Logical Thinking:
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Middle Of Linked List...")
    print("Add your test cases here")
