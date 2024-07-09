def sublista_sem_menor(lista):
    pmenor = lista.index(min(lista))
    lista2 = lista.copy()
    del(lista2[pmenor])

    return lista2

lista = [2, 4, 6, 8, 1, 3, 5, 7]
print(sublista_sem_menor(lista))