class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ["{","[","("]
        closed_list = ["}","]",")"]
        stack = []
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in closed_list:
                pos = closed_list.index(i)
                
                if((len(stack)>0) and open_list[pos] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False