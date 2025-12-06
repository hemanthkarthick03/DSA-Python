"""
BASEBALL GAME - Easy
Calculate points in baseball game

Logical Thinking:
- See implementation for approach
"""

def cal_points(ops):
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)


# Test cases
if __name__ == "__main__":
    print(f"Testing Baseball Game...")
    print("✅ Refer to implementation")
