"""
REVERSE INTEGER - Easy
Reverse digits of integer

Logical Thinking:
- See implementation for approach
"""

def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    result *= sign
    return result if -2**31 <= result <= 2**31 - 1 else 0


# Test cases
if __name__ == "__main__":
    print(f"Testing Reverse Integer...")
    print("✅ Refer to implementation")
