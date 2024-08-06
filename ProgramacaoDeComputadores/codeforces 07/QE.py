valor = int(input())
numeros = list(map(int,input().split()))
media = sum(numeros)/valor
maior = 0
menor = 0

for i in numeros:
    if (i>=media):
        maior+=1
    else:
        menor+=1

print('{:.1f}'.format(media))
print(menor)
print(maior)




    
