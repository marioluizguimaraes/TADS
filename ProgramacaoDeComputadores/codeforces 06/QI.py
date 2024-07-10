def lista_troca_menor_primeiro(lista):
    vezes = 1
    menor = min(lista)
    pm = lista.index(menor)
    if (menor == lista[0]):
        vezes = 0
    else:
        n = lista[0]
        lista[0] = min(lista)
        lista[pm] = n

    return vezes

lista = [91, 58, -41, 85, -81, 87, 9, 10, -49, 39]
print(lista_troca_menor_primeiro(lista))
