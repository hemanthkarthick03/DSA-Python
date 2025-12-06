"""
NUMBER OF 1 BITS - Easy
Count number of 1 bits in integer.

Logical Thinking:
1. Use Brian Kernighan's algorithm
2. n & (n-1) removes rightmost 1 bit
3. Count iterations

Logical Thinking:
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Number Of 1 Bits...")
    print("Add your test cases here")
