"""
REMOVE DUPLICATES FROM SORTED LIST - Easy
Remove duplicates from sorted list

Logical Thinking:
- See implementation for approach
"""

def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


# Test cases
if __name__ == "__main__":
    print(f"Testing Remove Duplicates From Sorted List...")
    print("✅ Refer to implementation")
