mae = int(input())
f1  = int(input())
f2  = int(input())
f3  = mae - (f1 + f2)

maiorIdade = f3

if ( f1 >= f2 and f1 >= f3 ):
    maiorIdade = f1

elif(f2 >= f1 and f2 >= f3):
    maiorIdade = f2

print(maiorIdade)
