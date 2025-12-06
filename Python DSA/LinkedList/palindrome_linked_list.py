"""
PALINDROME LINKED LIST - Easy
Check if linked list is palindrome.

Logical Thinking:
1. Find middle using slow/fast pointers
2. Reverse second half
3. Compare both halves

Logical Thinking:
def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Palindrome Linked List...")
    print("Add your test cases here")
