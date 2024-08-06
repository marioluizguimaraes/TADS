numero = int(input())
divisores = []

for i in range(1, numero + 1):
    if (numero%i == 0):
        divisores.append(i)

print(' '.join(map(str, divisores)))
