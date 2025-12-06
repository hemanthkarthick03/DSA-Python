"""
IMPLEMENT QUEUE USING STACKS - Easy
Implement queue using two stacks.

Logical Thinking:
1. Stack1 for enqueue
2. Stack2 for dequeue
3. Transfer elements when stack2 is empty

Logical Thinking:
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, x):
        self.s1.append(x)
    
    def pop(self):
        self._move()
        return self.s2.pop()
    
    def peek(self):
        self._move()
        return self.s2[-1]
    
    def _move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Implement Queue Using Stacks...")
    print("Add your test cases here")
