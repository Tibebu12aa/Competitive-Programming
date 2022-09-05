class MinStack:

    def __init__(self):
        """
        first we initialize two empty stacks.
        """
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        if not self.stack or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min: return None
        return self.min[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()