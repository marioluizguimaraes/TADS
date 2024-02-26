print("Escreva sua nota: ", end ="")
notas = input().split()

n1, n2 = map(float, notas)

media = (n1*2 + n2*3)/5
print("Sua média final é: " , media, sep = "")