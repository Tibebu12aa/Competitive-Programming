class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # first we create an empty stack
        # now for each elemnt if the element is not an operator we append it to the stack
        stack = []      
        for i in tokens:
            """
            else if the element is not an operator then for each operator we run the operation for the last two elements in the stack and store the result as the 
            last element by removing the previous last element using pop
            """ 
            if i == "+":
                stack[-1] = stack[-2] + stack.pop()
            elif i == "-":
                stack[-1] = stack[-2] - stack.pop()
            elif i == "*":
                stack[-1] = stack[-2] * stack.pop()
            elif i == "/":
                stack[-1] = int(stack[-2] / stack.pop())
            else:
                stack.append(int(i))
                
        return stack.pop()
