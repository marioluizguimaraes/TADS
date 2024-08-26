# Escreva uma função recursiva que determine quantos algarismos 
# são necessários para representar um determinado número, 
# ignorando os zeros à esquerda. 

def conta_algarismos(n):
    if (n//10 == False):
        return 1
    else:
        return conta_algarismos(n//10) + 1

numero = int(input())
print(conta_algarismos(numero))
