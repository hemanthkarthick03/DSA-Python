"""
SLIDING WINDOW MAXIMUM - Hard
Return max value in each sliding window of size k.

Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]

Logical Thinking:
1. Use deque to maintain indices of useful elements
2. Keep deque in decreasing order of values
3. Remove indices outside current window
4. Front of deque always has maximum

Key: Monotonic deque, sliding window
Time: O(n) | Space: O(k)
"""

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        
        if dq[0] == i - k:
            dq.popleft()
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Sliding Window Maximum...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
