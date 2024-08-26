# Escreva uma função recursiva que receba um número inteiro, 
# não negativo, e retorne se ele é primo. 
# Assinatura da função: def primo(n)

def primo_r(n, div): 
    if(div == 1):
        return 1
    else:
        if (n%div == 0):
            return primo_r(n, div-1) + 1
        else:
            return primo_r(n, div-1) + 0
            
def primo(n):

    verificador = primo_r(n,n)

    if(verificador == 2):
        return "É um número primo"  
    else:
        return "Não é um número primo"

print(primo(int(input("Escreva um número: "))))