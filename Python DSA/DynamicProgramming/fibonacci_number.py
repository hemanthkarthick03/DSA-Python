"""
FIBONACCI NUMBER - Easy
Calculate nth Fibonacci number

Logical Thinking:
- See implementation for approach
"""

def fib(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1


# Test cases
if __name__ == "__main__":
    print(f"Testing Fibonacci Number...")
    print("✅ Refer to implementation")
