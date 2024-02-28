print("Olá! Ecreva aqui, um numero real  " , sep = "" , end = "")
n1 = float(input())

print("Por favor, agora escreva aqui, um segundo numero real: " , sep = "" , end = "")
n2 = float(input())

print("A média aritimética de ", n1 , " e " , n2 , " é igual a " , '{:.2f}'.format((n1 + n2) / 2) , sep = "") 

