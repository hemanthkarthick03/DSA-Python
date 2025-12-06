"""
ODD EVEN LINKED LIST - Medium
Group odd and even nodes

Logical Thinking:
- See implementation for approach
"""

def odd_even_list(head):
    if not head:
        return None
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


# Test cases
if __name__ == "__main__":
    print(f"Testing Odd Even Linked List...")
    print("✅ Refer to implementation")
