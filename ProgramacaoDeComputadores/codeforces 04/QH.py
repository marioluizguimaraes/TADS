c = int(input())
a = int(input())

if ( c > a):
    viagens = 1

elif (a >= c ):
    viagens = (a + a//c) //c + 1

    if (a%c != 0):
        viagens = (a + a//c) //(c-1) 

print(viagens)