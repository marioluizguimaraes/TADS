lista = list(map(int, input().split()))
tamanho = len(lista)
soma = sum(lista)

if (soma%tamanho == 0):
    print('Sim')
else:
    print('Não')
