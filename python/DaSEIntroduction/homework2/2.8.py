import random
n = 1000000
s = 0
for i in range(n+1):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if(x**2+y**2<=1):
        s+=1
print(s/n*4)