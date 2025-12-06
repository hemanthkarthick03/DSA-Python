"""
SIMPLIFY PATH - Medium
Simplify Unix file path

Logical Thinking:
- See implementation for approach
"""

def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part == '..' and stack:
            stack.pop()
        elif part and part != '.' and part != '..':
            stack.append(part)
    return '/' + '/'.join(stack)


# Test cases
if __name__ == "__main__":
    print(f"Testing Simplify Path...")
    print("✅ Refer to implementation")
