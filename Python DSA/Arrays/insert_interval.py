"""
INSERT INTERVAL - Medium
Insert interval and merge if needed

Logical Thinking:
- See implementation for approach
"""

def insert(intervals, new):
    result = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    result.append(new)
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Insert Interval...")
    print("✅ Refer to implementation")
