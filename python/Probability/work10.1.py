import numpy as np
import math 
def f(x):
    return ((np.exp(x)-1)/(np.exp(1)-1))
def n(N):
    x=np.random.uniform(0,1,N)
    y=f(x)
    sum=0
    for i in y:
        sum+=i
    sum=sum/N
    return sum
print(n(10000))