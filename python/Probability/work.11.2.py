import numpy as np
import math 
def f(x):
    return (np.exp(-x*x/2)/np.sqrt(2*np.pi))
x=np.random.uniform(-10000,10000,3)
p=np.mean(x)
z=f(x)
sum1=0
sum2=0
num=0
for i in z:
    sum1+=(i-p)**4
    sum2+=(i-p)**2
    num=num+1
sum1=sum1/num
sum2=sum2/num
print(sum1/sum2**2-3)