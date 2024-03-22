n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

vmd1 = d1/v1
vmd2 = d2/v2

if (d1 > d2 and vmd2 >= vmd1 ):
    print(n2)
else:
    print(n1)