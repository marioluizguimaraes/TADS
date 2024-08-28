# Escreva uma função recursiva que receba um inteiro n, 
# não negativo, e retorne a quantidade de divisores de n. 
# Assinatura da função: def conta_divisores(n)

def conta_divisores_r(n, d):
    if (d == 1):
        return 1
    else:
        if (n % d == 0):
            return conta_divisores_r(n, d - 1) + 1
        else:
            return conta_divisores_r(n, d - 1)

def conta_divisores(n):
    return conta_divisores_r(n, n)

numero = int(input())
print(conta_divisores(numero))

