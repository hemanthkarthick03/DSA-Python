"""
INTERSECTION OF TWO LINKED LISTS - Easy
Find node where two linked lists intersect.

Logical Thinking:
1. Calculate lengths of both lists
2. Align starting points
3. Move together until nodes match

Logical Thinking:
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Intersection Of Two Linked Lists...")
    print("Add your test cases here")
