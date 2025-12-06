"""
VALID PARENTHESES - Easy
Check if string of brackets is valid.

Logical Thinking:
1. Use stack
2. Push opening brackets
3. Pop and match closing brackets

Logical Thinking:
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Valid Parentheses...")
    print("Add your test cases here")
