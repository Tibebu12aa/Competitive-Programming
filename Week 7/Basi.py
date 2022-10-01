pushed = [1,2,3,1,4,5]
popped = [4,2,3,5,1,2]
stack=[]
j=len(popped)-1
i=0
while stack and i<len(pushed)-1:
    if popped.pop()==pushed[i]:
        stack.pop()
    stack.append(pushed[i])
    i+=1
print(stack)
if len(stack)==0:
    print(True)
else:
    print(False)


