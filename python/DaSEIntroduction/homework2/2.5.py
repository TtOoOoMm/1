c = 2000
g = c/2
while(abs(g**2-c)>0.000001):
    g = (g + c/g)/2
print(g)