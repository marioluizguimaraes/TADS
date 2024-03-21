c = int(input())
a = int(input())
viagens = 1

if (a == c):
    viagens = 2
elif (a%c > 0):
    viagens = (a + (a//c + a%c +1) )//c 

elif (a > c):
    viagens = (a + (a//c + a%c) )//c + 1

print(viagens)