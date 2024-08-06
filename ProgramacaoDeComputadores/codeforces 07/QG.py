valor = int(input())
numeros = list(map(int,input().split()))
media = sum(numeros)/valor
maiores = []
menores = []

for i in numeros:
    if (i>=media):
        maiores.append(i)
    else:
        menores.append(i)

print('{:.1f}'.format(media))
print(len(menores), ' '.join(map(str, menores)))
print(len(maiores), ' '.join(map(str, maiores)))
