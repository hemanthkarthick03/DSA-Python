"""
SLIDING WINDOW MEDIAN - Hard
Find median in each sliding window
"""

from sortedcontainers import SortedList
def median_sliding_window(nums, k):
    window = SortedList(nums[:k])
    medians = []
    for i in range(k, len(nums) + 1):
        medians.append((window[k//2] + window[(k-1)//2]) / 2)
        if i < len(nums):
            window.remove(nums[i-k])
            window.add(nums[i])
    return medians


if __name__ == "__main__":
    print("✅ Sliding Window Median")
