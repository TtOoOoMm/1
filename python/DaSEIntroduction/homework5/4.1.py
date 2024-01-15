a = int(input())
flag = 0
for i in range(2,a-1):
    if(a % i == 0):
        flag += 1
if flag == 0:
    print("True")
else:
    print("False")