import math
n,m,a = map(int,input().split())
A = math.ceil(n/a)
B = math.ceil(m/a)
print(int(A*B))