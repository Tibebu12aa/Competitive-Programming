import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # first we need to define each operators functions since it is listed as a string 
        # so we created a dictionry containing each operartion and its fuv=ction
        operators={"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a*b, "/": lambda a,b:int(a/b)}
        # now we create an empty stack
        stack=[]
        # for every element in tokens we proceed to iterate 
        for j in tokens:
            if j in operators:
                a=stack.pop()
                b=stack.pop()
                stack.append(operators[j](a,b))
            else:
                stack.append(int(j))
        return stack[0]
            
        
                         
            