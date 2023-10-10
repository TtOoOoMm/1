n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = [0] * n
for i in range(n):
    flag = 1
    for j in range(n):
        if j != i:
            flag *= a[j]
    b[i] = flag
print(b)