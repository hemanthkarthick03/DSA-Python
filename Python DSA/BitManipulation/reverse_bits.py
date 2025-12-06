"""
REVERSE BITS - Easy
Reverse bits of 32-bit unsigned integer.

Logical Thinking:
1. Extract bits from right
2. Add to result from left
3. Process all 32 bits

Logical Thinking:
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Reverse Bits...")
    print("Add your test cases here")
