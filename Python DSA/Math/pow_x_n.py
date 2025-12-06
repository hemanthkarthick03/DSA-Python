"""
POW X N - Medium
Implement power function x^n.

Logical Thinking:
1. Use fast exponentiation (divide and conquer)
2. Handle negative exponent
3. O(log n) complexity

Logical Thinking:
def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n:
        if n % 2:
            result *= x
        x *= x
        n //= 2
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Pow X N...")
    print("Add your test cases here")
