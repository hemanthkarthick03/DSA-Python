"""
MERGE INTERVALS - Medium
Merge all overlapping intervals.

Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

Logical Thinking:
1. Sort intervals by start time
2. Compare current interval with last merged interval
3. If overlaps: merge by extending end
4. If doesn't overlap: add as new interval

Key: Sorting, interval merging pattern
Time: O(n log n) | Space: O(n)
"""

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    return merged


# Test cases
if __name__ == "__main__":
    print(f"Testing Merge Intervals...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
