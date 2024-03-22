n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

if (d1 <= d2 and d2/v2 <= d1/v1 ):
    print(n2)

elif (d1 >= d2 and d2/v2 >= d1/v1 ):
    print(n1)