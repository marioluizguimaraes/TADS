c = int(input())
a = int(input())
viagens = 0
if ( c > a):
    viagens = 1

elif ( a == c):
    viagens = 2

elif ((a + (a//(c-1)))%c != 0):
    viagens = (a + (a//(c-1)))//c + 1
else:
    viagens = (a + (a//(c-1)))//c

print(viagens)