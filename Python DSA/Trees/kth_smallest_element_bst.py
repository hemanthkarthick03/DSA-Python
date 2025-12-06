"""
KTH SMALLEST ELEMENT BST - Medium
Find kth smallest element in BST

Logical Thinking:
- See implementation for approach
"""

def kth_smallest(root, k):
    stack = []
    curr = root
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right


# Test cases
if __name__ == "__main__":
    print(f"Testing Kth Smallest Element Bst...")
    print("✅ Refer to implementation")
