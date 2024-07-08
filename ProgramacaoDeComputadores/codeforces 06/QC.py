def maior2 (a,b):
    
    maior = a
    if (b > a):
        maior = b
    return maior

a, b = map(int, input().split())
print(maior2(a,b))