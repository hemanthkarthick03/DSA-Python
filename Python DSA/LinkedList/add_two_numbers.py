"""
ADD TWO NUMBERS - Medium
Add two numbers represented as linked lists (reversed order).

Logical Thinking:
1. Traverse both lists simultaneously
2. Add values with carry
3. Create new nodes for result

Logical Thinking:
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Add Two Numbers...")
    print("Add your test cases here")
