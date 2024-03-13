c = int(input())
a = int(input())

viagens = (a//c) 

if ( c > a):
    viagens = 1

elif (a >= c):
    viagens = (( a + viagens)//c) + 1

print(viagens)