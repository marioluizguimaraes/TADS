preco       = int(input())
quantidade  = int(input())
valor       = int(input())

total = preco*quantidade
troco = valor - total

print("A pagar:", total)
print("Troco  :", troco)
