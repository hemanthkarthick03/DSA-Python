"""
MIN STACK - Easy
Implement stack that supports getMin in O(1).

Logical Thinking:
1. Use two stacks: main and min
2. Min stack tracks minimum at each level
3. Pop from both when popping

Logical Thinking:
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Min Stack...")
    print("Add your test cases here")
