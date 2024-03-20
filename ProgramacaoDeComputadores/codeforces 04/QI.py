a, b, c = map(int, input().split())

if (a < b + c and  b < a + c and c < a + b ):
    
    if (a == b and a == c and b == c): 
       print("a")  
   
    else:
        if(b >= a and b >= c):
            if ( pow(b,2) == pow(a,2) + pow(c,2)):
                print("r") 
            else:
                print("o")                    
        elif (c >= a and c >= b):      
            if ( pow(c,2) == pow(a,2) + pow(b,2)):
                print("r") 
            else:
                print("o") 
        else:
            if ( pow(a,2) == pow(b,2) + pow(c,2)):
                print("r") 
            else:
                print("o")
               
else:
    print("n")
    