b = int(input())
t = int(input())

trapeziobt = ((b + t)*70)/2

if ( trapeziobt == 80*70  ):
    print("0")

elif( trapeziobt < 80*70 ):
    print("2")

elif( trapeziobt > 80*70):
    print("1")