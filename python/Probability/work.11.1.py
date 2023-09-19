import numpy as np
import math 
def f(x):
    return (np.exp(-(x*x)/2)/np.sqrt(2*np.pi))
x=np.random.uniform(-10000,10000,20)
p=np.mean(x)
z=f(x)
sum1=0
sum2=0
num=0
for i in z:
    sum1+=(i-p)**3
    sum2+=(i-p)**2
    num=num+1
    while num==20:
        break
sum1=sum1/num
sum2=sum2/num
list=[]
i=0
for i in range(20):
    list.append(sum1/math.pow(sum2,3/2))
    i+=1
list.sort()
print(list[0])
