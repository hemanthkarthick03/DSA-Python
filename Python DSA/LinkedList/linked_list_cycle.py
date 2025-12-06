"""
LINKED LIST CYCLE - Easy
Detect if linked list has cycle.

Logical Thinking:
1. Use Floyd's cycle detection (slow/fast pointers)
2. If fast catches slow, cycle exists
3. If fast reaches end, no cycle

Logical Thinking:
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Linked List Cycle...")
    print("Add your test cases here")
