class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.dq = collections.deque(maxlen=k)
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size<self.k:
            self.dq.appendleft(value)
            self.size+=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.size<self.k:
            self.dq.append(value)
            self.size+=1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.size>0:
            pop = self.dq.popleft()
            self.size-=1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.size>0:
            pop = self.dq.pop()
            self.size-=1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.size>0:
            return self.dq[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.size>0:
            return self.dq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size==self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()