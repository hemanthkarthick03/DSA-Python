"""
SQRT X - Easy
Compute square root (integer part).

Logical Thinking:
1. Binary search between 0 and x
2. Find largest num where num*num <= x
3. Handle overflow with mid*mid

Logical Thinking:
def my_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Sqrt X...")
    print("Add your test cases here")
