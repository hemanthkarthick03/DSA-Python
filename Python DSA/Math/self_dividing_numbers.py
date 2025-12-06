"""
SELF DIVIDING NUMBERS - Easy
Find self-dividing numbers in range
"""

def self_dividing_numbers(left, right):
    def is_self_dividing(num):
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
    return [num for num in range(left, right + 1) if is_self_dividing(num)]


if __name__ == "__main__":
    print("✅ Self Dividing Numbers")
