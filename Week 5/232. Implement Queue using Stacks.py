class MyQueue:
    def __init__(self):
        # first i created two empty stacks
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        # define the push function meaning for x vlaue enterd append it to stack1
        self.stack1.append(x)
    def pop(self) -> int:
        # now for the pop function the function Removes the element from the front of queue and returns that element.
        # so remove all the elments from stack1(excpet from elment 1) and find the last poped elment
        length = len(self.stack1) - 1
        for i in range(length):
            """
            each time we pop an elment from stack1 we append it to the to stack inoreder to be able to                   restore it it later 
            """ 
            self.stack2.append(self.stack1.pop())
        poped_val = self.stack1.pop()
        # after that we undo the pop by returning it from the stack2(last elemnt)
        for i in range(length):
            self.stack1.append(self.stack2.pop())
        return poped_val
    def peek(self) -> int:
        # for the peek function we want to Get the front element 
        length = len(self.stack1)
        """
        so we remove all the elemnents from stack 1 then append them to stack2 and return the last value of         stack2
        """
        for i in range(length):
            self.stack2.append(self.stack1.pop())
        peek_val = self.stack2[-1]
        for i in range(length):
            self.stack1.append(self.stack2.pop())
        return peek_val
    def empty(self):
        # this funtion just checks if stack one is empty and return true or flase
        if len(self.stack1)==0:
            return True
        else:
            return False 
        
        
        
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)l
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()