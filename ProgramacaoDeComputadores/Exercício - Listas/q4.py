lista = list(map(int, input().split()))

lista.append(lista[0])

n = len(lista) - 2
lista.insert(1, lista[n])

lista.remove(lista[0])
n = len(lista) - 2

del(lista[n])

print(lista)
