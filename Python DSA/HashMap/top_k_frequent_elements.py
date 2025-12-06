"""
TOP K FREQUENT ELEMENTS - Medium
Return k most frequent elements from array.

Logical Thinking:
1. Count frequencies using Counter
2. Use heap or sort by frequency
3. Return top k elements

Logical Thinking:
from collections import Counter
import heapq
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Top K Frequent Elements...")
    print("Add your test cases here")
