class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        self.min = None
        self.last = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.min is None):
            self.min = val
        if (val <= self.min): self.min_stack.append(val)
        self.min = min(self.min, val)
        self.last += 1

    def pop(self) -> None:
        top = self.stack[self.last - 1]
        self.stack.pop()
        self.last -= 1
        if (top == self.min_stack[-1]):
            self.min_stack.pop()
            if (self.last == 0):
                self.min = None
            else:
                self.min = self.min_stack[-1]
        

    def top(self) -> int:
        return self.stack[self.last - 1]

    def getMin(self) -> int:
        return self.min
