lista1 = list(map(int, input().split()))
tamanho = len(lista1)
n = tamanho - 1
lista2 = sorted(lista1)
menor = lista2[0]
maior = lista2[n]
print(menor, maior)