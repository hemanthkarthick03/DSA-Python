"""
4SUM II - Medium
Count 4-element tuples with sum 0

Logical Thinking:
- See implementation for approach
"""

def four_sum_count(A, B, C, D):
    from collections import Counter
    ab_sum = Counter(a + b for a in A for b in B)
    return sum(ab_sum[-c - d] for c in C for d in D)


# Test cases
if __name__ == "__main__":
    print(f"Testing 4Sum Ii...")
    print("✅ Refer to implementation")
