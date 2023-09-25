c = 2
g = 0
for i in range(0, c+1):
    if(i**2 > c):
        g = i - 1
        break
while(abs(g**2-2)>0.00001):
    g+=0.000001
print(g)
#笨办法