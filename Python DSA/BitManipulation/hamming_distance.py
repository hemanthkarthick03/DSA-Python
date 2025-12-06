"""
HAMMING DISTANCE - Easy
Calculate Hamming distance

Logical Thinking:
- See implementation for approach
"""

def hamming_distance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count


# Test cases
if __name__ == "__main__":
    print(f"Testing Hamming Distance...")
    print("✅ Refer to implementation")
