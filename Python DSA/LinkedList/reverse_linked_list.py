"""
REVERSE LINKED LIST - Easy
Reverse a singly linked list.

Logical Thinking:
1. Use three pointers: prev, curr, next
2. Iterate through list
3. Reverse links one by one

Logical Thinking:
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Reverse Linked List...")
    print("Add your test cases here")
