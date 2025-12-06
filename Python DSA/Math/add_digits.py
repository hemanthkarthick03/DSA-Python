"""
ADD DIGITS - Easy
Add digits until single digit

Logical Thinking:
- See implementation for approach
"""

def add_digits(num):
    return 1 + (num - 1) % 9 if num else 0


# Test cases
if __name__ == "__main__":
    print(f"Testing Add Digits...")
    print("✅ Refer to implementation")
