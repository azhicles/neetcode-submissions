from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.stack.appendleft(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.minimum:
            self.stack.popleft()
            self.minimum = self.stack[0] if self.stack else float('inf')


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
