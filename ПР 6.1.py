n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = a[0]
for i in a:
    if i > max:
        max = i
print(max)