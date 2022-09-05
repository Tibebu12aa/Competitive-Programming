from collections import deque
class MyQueue:
    def __init__(self):
        self.MyQueue = deque()
    def push(self, x: int) -> None:
        self.MyQueue.append(x)
    def pop(self) -> int:
        if len(self.MyQueue) > 0:
            return self.MyQueue.popleft()
        else:
            return None
    def peek(self) -> int:
        if len(self.MyQueue) > 0:
            return self.MyQueue[len(self.MyQueue)-2]
        else:
            return None
    def empty(self):
        if len(self.MyQueue)==0:
            return True
        else:
            return False 
        
        
        
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)l
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()