n = int(input())
medicoes = []
medicoesDiferentes = 0

for i in range(n):
    b = int(input())
    medicoes.append(b)

media = sum(medicoes)//n  

for x in range(len(medicoes)):
    
    dif = (100 * medicoes[x])/media

    
    if (dif % 1 == 0):
        dif = int(dif) 
    else:
        dif = int(dif) + 1

    if (dif - 100 < 0):
        if (abs(dif - 100) > 10):
            medicoesDiferentes += 1
    else:
        if (dif - 100 > 10):
            medicoesDiferentes += 1

print(media)
print(medicoesDiferentes)