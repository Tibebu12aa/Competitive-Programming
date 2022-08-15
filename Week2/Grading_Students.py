list = []
n=int(input())
a=1
while a<=n:
    list.append(int(input()))
    a=a+1
for i in list:
    if i<38:
        print(i)
    elif i%5==0:
        print(i)
    elif i%5==1:
        print(i)
    elif i%5==2:
        print(i)
    elif i%5==3:
        print(i+2)
    else:
        print(i+1)
