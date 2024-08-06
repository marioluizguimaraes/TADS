valor, limite = map(int, input().split())
multiplos = []
for i in range(1, limite+1):
    if (valor*i<= limite):
        multiplos.append(valor*i)

print(' '.join(map(str, multiplos))) 
