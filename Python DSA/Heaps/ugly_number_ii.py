"""
UGLY NUMBER II - Medium
Find nth ugly number

Logical Thinking:
- See implementation for approach
"""

def nth_ugly_number(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    for _ in range(n - 1):
        next2 = ugly[i2] * 2
        next3 = ugly[i3] * 3
        next5 = ugly[i5] * 5
        next_ugly = min(next2, next3, next5)
        ugly.append(next_ugly)
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1
    return ugly[-1]


# Test cases
if __name__ == "__main__":
    print(f"Testing Ugly Number Ii...")
    print("✅ Refer to implementation")
