b = int(input())
t = int(input())

trapezio = ((b + t)*70)/2
print(trapezio)

if ( (b == 80 and t == 80 ) or (160 - t == b  and 160 - b == t )):
    print("0")

elif( b < 80 and t < 80):
    print("2")

elif( b > 80 and t > 80):
    print("1")

S
