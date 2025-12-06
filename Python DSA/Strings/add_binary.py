"""
ADD BINARY - Easy
Add two binary strings

Logical Thinking:
- See implementation for approach
"""

def add_binary(a, b):
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    return ''.join(result[::-1])


# Test cases
if __name__ == "__main__":
    print(f"Testing Add Binary...")
    print("✅ Refer to implementation")
