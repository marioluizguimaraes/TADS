nome        = input()
n_hora      = int(input())
valor_hora  = float(input())
salario     = n_hora*valor_hora

print(nome)
print("R$", "{:.2f}".format(salario))