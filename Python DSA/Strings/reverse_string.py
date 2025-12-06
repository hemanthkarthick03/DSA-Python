"""
REVERSE STRING - Easy
Reverse string in-place

Logical Thinking:
- See implementation for approach
"""

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Test cases
if __name__ == "__main__":
    print(f"Testing Reverse String...")
    print("✅ Refer to implementation")
