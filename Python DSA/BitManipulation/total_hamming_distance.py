"""
TOTAL HAMMING DISTANCE - Medium
Total Hamming distance between all pairs
"""

def total_hamming_distance(nums):
    total = 0
    for bit in range(32):
        ones = sum((num >> bit) & 1 for num in nums)
        zeros = len(nums) - ones
        total += ones * zeros
    return total


if __name__ == "__main__":
    print("✅ Total Hamming Distance")
