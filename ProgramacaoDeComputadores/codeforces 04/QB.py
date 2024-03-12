a, b, c, d = map(int, input().split())

ab = a + b
ac = a + c
ad = a + d

bc = b + c
bd = b + d

cd = d + c


if (a < bc):
    print("S")
elif ( a < bd):
    print("S")
elif ( a < cd):
    print("S")
    
elif ( b < ac):
    print("S")
elif ( b <  ad):
    print("S")
elif ( b < cd):
    print("S")
    
elif ( c < ab):
    print("S")
elif ( c < bd):
    print("S")
elif ( c < ad):
    print("S")
    
elif ( d < ab):
    print("S")
elif ( d < ac):
    print("S")
elif ( d < ab):
    print("S")
else:
    print("N")