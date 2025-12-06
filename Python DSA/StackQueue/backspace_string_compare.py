"""
BACKSPACE STRING COMPARE - Easy
Compare strings with backspaces

Logical Thinking:
- See implementation for approach
"""

def backspace_compare(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return ''.join(stack)
    return build(s) == build(t)


# Test cases
if __name__ == "__main__":
    print(f"Testing Backspace String Compare...")
    print("✅ Refer to implementation")
