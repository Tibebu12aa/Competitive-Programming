class Solution:
    def isValid(self, s: str) -> bool:
        #first i crated two lists containg both open and close parentheses with each parenthesis in openlist
        # have the same index in the closed list
        open_list = ["{","[","("]
        closed_list = ["}","]",")"]
        #then i created an empty stack 
        My_stack = []
        #now for every element in the list s this programm will iterate the valdity by appending and poping elments in to My_stack
        for i in s:
            #in the loop first i is from the opend list it will append(push) it to the empty stack  
            if i in open_list:
                My_stack.append(i)
            ### else if if i is from the closed list it will check if its the same kinda of parenthesis by 
            # by setting the index of the element in the closed list to a variable named checkindex
            # and then check if its the same as the last stack element
            elif i in closed_list:
                checkindex=closed_list.index(i)
                if len(My_stack)>0 and open_list[checkindex]==My_stack[len(My_stack)-1]:
                    #then if it is it will pop the last element in the stack making it an empty stack
                    My_stack.pop()
                else:
                    return False
        #finallly if the stack is not empty then it doesn't have a valid parentheses
        if len(My_stack)==0:
            return True
        else:
            return False