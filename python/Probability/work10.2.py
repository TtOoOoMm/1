import numpy as np
import math 
def f(x):
    return (np.exp(x))
def n(N):
    x=np.random.uniform(-1,1,N)
    y=f(x)
    return y.mean()*1
print(n(10000))