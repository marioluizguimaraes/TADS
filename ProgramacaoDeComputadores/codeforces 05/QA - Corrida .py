n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

t1 = d1/v1 
t2 = d2/v2

if ( t1 < t2 ):
    print(n1)

elif ( t2 < t1 ):
    print(n2)
