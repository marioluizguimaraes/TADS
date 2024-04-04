lista = list(map(int, input().split()))
soma = sum(lista)

if (soma%2 == 0):
    print('Par')
else:
    print('Impar')
