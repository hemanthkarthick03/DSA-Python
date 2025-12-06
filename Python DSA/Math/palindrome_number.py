"""
PALINDROME NUMBER - Easy
Check if integer is palindrome

Logical Thinking:
- See implementation for approach
"""

def is_palindrome(x):
    if x < 0:
        return False
    reversed_num = 0
    original = x
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return reversed_num == original


# Test cases
if __name__ == "__main__":
    print(f"Testing Palindrome Number...")
    print("✅ Refer to implementation")
