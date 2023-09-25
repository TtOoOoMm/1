import math
import random
def f(x):
    return x**2+4*x*math.sin(x)
n = 1000000
s = 0
for i in range(n+1):
    x = random.uniform(2,3)
    s+=f(x)
print(s/n)