a, b, c, d = map(int, input().split())

if (a < b + c and  b < a + c and c < a + b ):
    print("S")
    
elif (a < b + d and  b < a + d and d < a + b ):
    print("S")
    
elif (b < d + c and  c < d + b and d < c + b ):
    print("S")

elif (a < d + c and  c < d + a and d < c + a ):
    print("S")
    
else:
    print("N")