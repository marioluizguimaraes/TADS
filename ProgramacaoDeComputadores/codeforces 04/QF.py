#Maior média ponderada
a11, a12 = map(int, input().split())
a21, a22 = map(int, input().split())
p1, p2   = map(int, input().split())

m1 = (a11*p1 + a12*p2)//(p1+p2)
m2 = (a21*p1 + a22*p2)//(p1+p2)

if (m1 >= m2):
    print("1")
else:
    print("2")