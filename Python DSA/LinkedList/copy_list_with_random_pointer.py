"""
COPY LIST WITH RANDOM POINTER - Medium
Deep copy linked list with random pointer.

Logical Thinking:
1. Create copy nodes interleaved
2. Set random pointers for copies
3. Extract copy list

Logical Thinking:
def copy_random_list(head):
    if not head:
        return None
    curr = head
    while curr:
        copy = Node(curr.val, curr.next)
        curr.next = copy
        curr = copy.next
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    curr = head
    copy_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next
    return copy_head
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Copy List With Random Pointer...")
    print("Add your test cases here")
