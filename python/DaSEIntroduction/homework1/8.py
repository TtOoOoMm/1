x=int(input())
a=[]
for i in range(x):
    a.append(int(input()))
for j in range(x):
    print(a[x-j-1],end=' ')