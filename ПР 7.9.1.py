def summ(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
num = int(input())
kolvo = 0
while num > 0:
    num -= summ(num)
    kolvo += 1
print(kolvo)