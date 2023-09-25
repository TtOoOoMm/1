n = int(input())
flag = [0] * (n+1)
flag[2] = 1
for i in range(3,n+1):
    for j in range(1,i-1):
        flag[i] = max(flag[i],max((i-j)*j,flag[i-j]*j))
print(flag[n])