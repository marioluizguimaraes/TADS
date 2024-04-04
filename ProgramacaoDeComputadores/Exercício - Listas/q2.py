lista1 = list(map(int, input().split()))

lista1.insert(2, lista1[0])
lista1.remove(lista1[0])

print(lista1)
