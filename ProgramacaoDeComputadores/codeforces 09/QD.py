cifra = list(input().strip())
palavra = list(input().strip())

contador = 0

for i in range(0, (len(cifra)-len(palavra))+1):
   
    for x in range(len(palavra)):
        
        if (palavra[x] == cifra[x+i]):
            break

        elif (x == len(palavra)-1):
            contador += 1

print(contador)