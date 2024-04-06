lista = list(map(int, input().split()))
tamanho = len(lista)

if ( tamanho > 1 and tamanho%2 == 0):
    media = sum(lista)/tamanho
    print(media)

elif(tamanho > 1 and tamanho%2 != 0):
    mediana = tamanho//2
    print(lista[mediana])
else:
    print(lista)