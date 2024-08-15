Vezes = int(input())
contador = 0
anterior = 0
da_vez = 0
for i in range(Vezes):
    da_vez = int(input())
    if (da_vez != anterior):
        contador += 1
    anterior = da_vez
print(contador)
    
