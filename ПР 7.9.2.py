a = [2, 4, 6, 2, 1,5]
b = [2, 7, 6, 6, 9,5]
c = [4, 1, 6, 2, 6,8]
summA = 0
summB = 0
summC = 0
for i in range(len(a)):
    summA += a[i]
for i in range(len(b)):
    summB += a[i]
for i in range(len(c)):
    summC += a[i]
cr_znA = summA/len(a)
cr_znB = summA/len(b)
cr_znC = summA/len(c)
print(summA, summB, summC, cr_znA, cr_znB, cr_znC )

