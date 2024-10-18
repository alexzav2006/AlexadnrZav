a = [0, 2, 3, 5, 0, 0, 6, 25, 0]
summ = 0
for i in range(len(a)):
    summ += a[i]
cr_zn = summ/len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = cr_zn
print(a)