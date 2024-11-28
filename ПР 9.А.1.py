def fac(x):
    if x == 0:
         return 1
    return fac(x-1)*x
x = int(input())
n = int(input())
print((x**n)/fac(n))