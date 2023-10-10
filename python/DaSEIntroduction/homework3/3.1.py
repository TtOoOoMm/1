x = float(input())
a = int(x)
b = x - a
A = bin(a)[2:]
B = ""
while(b > 0):
    b *= 2
    b0 = int(b)
    B += str(b0)
    b -= b0
print(f"{A}.{B}")