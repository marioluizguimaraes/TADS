def convercao(v, contador):
    if(v<2):
        return contador.append(str(v))
     
    elif (v%2 == 0):
        contador.append(str(0))
        print(v//2)
        return convercao(v//2)
    
    else:
        contador.append(str(1))
        print(v//2)
        return convercao(v//2)


def conta_bits(n):
    lista_binario = []
    return convercao(n, lista_binario)

conta_bits(32)
