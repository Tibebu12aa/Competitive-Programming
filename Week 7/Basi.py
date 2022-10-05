pushed = [1,2,3,4,5,5,3,2,3,23,6,43,2]
n=len(pushed)
lastelement=pushed[-1]
for i in range(1,len(pushed)):
    currNm=pushed[i]
    for j in range(i-1,-1,-1):
        if pushed[j]>currNm:
            pushed[j+1]=pushed[j]
            print(pushed)
        else:
            pushed[j+1]=currNm
            break
print(*pushed)