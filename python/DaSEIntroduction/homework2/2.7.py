c = 10
g = 3
while(abs(g**3-c)>0.000001):
    g = (2*g + c/g**2)*1/3
print(g)
#公式：a[n+1] = 2/3*a[n] + 1/3*c/a[n]^2