
n =int(input())
list=[]
i=1
while i <= n:
    if i%5 ==0 and i%3:
        list.append("FizzBuzz")
    elif i%3==0:
        list.append("Fizz")
    elif i%5==0:
        list.append("Buzz")
    else:
        list.append(i)
    i+=1 
print(list)
