b = []
z = 0
def vvod():
    a = int(input())
    b.append(a)
    if a == 0:
        maximum(b)
    else:
        print(b)
        vvod()
def maximum(x):
    x.remove(max(x))
    print(max(x))
vvod()