"""
TRIBONACCI NUMBER - Easy
Calculate nth Tribonacci number

Logical Thinking:
- See implementation for approach
"""

def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


# Test cases
if __name__ == "__main__":
    print(f"Testing Tribonacci Number...")
    print("✅ Refer to implementation")
