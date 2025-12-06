"""
EVALUATE REVERSE POLISH NOTATION - Medium
Evaluate RPN expression.

Logical Thinking:
1. Use stack
2. Push numbers
3. Pop two operands for operators

Logical Thinking:
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Evaluate Reverse Polish Notation...")
    print("Add your test cases here")
