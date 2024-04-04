lista = list(map(int, input().split()))
tamanho = len(lista)

if (tamanho%2 == 0):
    media = sum(lista)//tamanho
    print(media)
