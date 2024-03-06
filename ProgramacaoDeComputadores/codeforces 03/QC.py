n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = n1

if (n2 > maior and n2 >n3):
    maior = n2
elif (n3 > maior):
    maior = n3

print(maior)

