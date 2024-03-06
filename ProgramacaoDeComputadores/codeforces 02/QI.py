l, d = map(int, input().split())
k, p = map(int, input().split())
custo = (k*l) + (p*(l//d))
print(custo)