#Triângulos
a, b, c = map(int, input().split())

if (a < b + c and  b < a + c and c < a + b ):
    
    if(b >= a and b >= c):

        if ( b*b == a*a + c*c):
            print("r")

        elif ( a*a + c*c -b*b > 0):
            print("a") 

        elif ( a*a + c*c - b*b < 0):
            print("o")       

    elif (c >= a and c >= b):  

        if ( c*c == a*a + b*b):
            print("r") 
        
        elif ( a*a + b*b - c*c > 0):
            print("a") 

        elif ( a*a + b*b - c*c < 0):
            print("o") 

    elif (a >= b and a >= c):
        
        if ( a*a == b*b + c*c):
            print("r") 

        elif ( b*b + c*c - a*a > 0):
            print("a") 

        elif (  b*b + c*c - a*a < 0):
            print("o")

else:
    print("n")
    