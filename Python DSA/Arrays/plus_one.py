"""
PLUS ONE - Easy
Add one to array representing number

Logical Thinking:
- See implementation for approach
"""

def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


# Test cases
if __name__ == "__main__":
    print(f"Testing Plus One...")
    print("✅ Refer to implementation")
