"""
MERGE IN BETWEEN LINKED LISTS - Medium
Merge list2 between a and b in list1
"""

def merge_in_between(list1, a, b, list2):
    prev = list1
    for _ in range(a - 1):
        prev = prev.next
    curr = prev
    for _ in range(b - a + 2):
        curr = curr.next
    prev.next = list2
    while list2.next:
        list2 = list2.next
    list2.next = curr
    return list1


if __name__ == "__main__":
    print("✅ Merge In Between Linked Lists")
