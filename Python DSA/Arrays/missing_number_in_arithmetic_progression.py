"""
MISSING NUMBER IN ARITHMETIC PROGRESSION - Easy
Find missing number in AP
"""

def missing_number(arr):
    n = len(arr)
    diff = (arr[-1] - arr[0]) // n
    for i in range(1, n):
        if arr[i] - arr[i-1] != diff:
            return arr[i-1] + diff
    return arr[0]


if __name__ == "__main__":
    print("✅ Missing Number In Arithmetic Progression")
