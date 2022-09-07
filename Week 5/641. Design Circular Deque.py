class MyCircularDeque:

    def __init__(self, k: int):
        # first we intialize the queque and set max size of the deque to k
        # and also we initialize the size
        self.k = k
        self.My_deque = collections.deque(maxlen=k)
        self.size = 0

    def insertFront(self, value: int) -> bool:
        # to insert new value in the front if deque hasn't passed max size
        # we use the append.left to insert the value
        # and also we increase the size by one and return True
        # else we return false
        if self.size<self.k:
            self.My_deque.appendleft(value)
            self.size+=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        # to insert new value to the last of the deque if deque hasn't passed max size
        # we use the append to insert the value
        # and also we increase the size by one and return True
        # else we return false
        if self.size<self.k:
            self.My_deque.append(value)
            self.size+=1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        # to delete value from the front of the deque if deque is not empty
        # we use the pop.left() to delete the value
        # and also we decrease the size by one and return True
        # else we return false
        if self.size>0:
            pop = self.My_deque.popleft()
            self.size-=1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        # to delete value from the from last of the deque if deque is not empty
        # we use the pop() to delete the value
        # and also we decrease the size by one and return True
        # else we return false
        if self.size>0:
            pop = self.My_deque.pop()
            self.size-=1
            return True
        else:
            return False
    def getFront(self) -> int:
        # to get the front value  of the deque if deque is not empty
        # we return the 0 index of the deque
        # else we return -1
        if self.size>0:
            return self.My_deque[0]
        else:
            return -1
    def getRear(self) -> int:
        # to get the rear value  of the deque if deque is not empty
        # we return the -1 index of the deque
        # else we return -1
        if self.size>0:
            return self.My_deque[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        #inorder to check id the  deque is ful we check if size is equal to k
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