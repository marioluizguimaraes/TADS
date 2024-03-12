l1 = 432
l2 = 468
 
x, y = map(int, input().split())
 
if ( x < 0 or x > l1):
    print("fora")
elif ( y < 0 or y > l2):
    print("fora")
else:
    print("dentro")
