t = int(input())
sequencia = list(map(int, input().split()))
contador = 0

if (t == 1 or len(sequencia) == 2):
    print('1')
else:
    diferenca = sequencia[1] - sequencia[0]
    
    for i in range(len(sequencia)):
        if (i == len(sequencia)-1):
            contador += 1
        elif (sequencia[i+1] - sequencia[i] != diferenca):
            diferenca = sequencia[i+1] - sequencia[i]
            contador += 1
    print(contador)
