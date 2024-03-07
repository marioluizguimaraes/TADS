n1 = int(input())
n2 = int(input())
resto = 0
 
if (n1 > n2):
    resto = n1%n2
    if (resto == 0):
        print("Multiplos")
    else:
        print("Nao multiplos")
else:
    resto = n2%n1
    if (resto == 0):
        print("Multiplos")
    else:
        print("Nao multiplos")
