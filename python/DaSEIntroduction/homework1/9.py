s=input()
length=len(s)
flag=0
for i in range(length-1):
    if(s[i]==s[i+1]):
        flag=1
print(flag)