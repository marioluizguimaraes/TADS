def maior5 (a,b,c,d,e):
    maior = a
    if (b > a and b > c and b > d and b > e):
        maior = b
    elif (c > a and c > b and c > d and c > e):
        maior = c
    elif (d > a and d > b and d > c and d > e):
        maior = d
    elif (e > a and e > b and e > c and e > d ):
        maior = e
    elif (a > b and a > c and a > d and a > e ):
        maior = a
    return maior

a, b, c, d, e = map(int, input().split())
print(maior5(a,b,c,d,e))