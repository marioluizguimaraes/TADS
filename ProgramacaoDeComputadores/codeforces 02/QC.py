nome    = input()
salario = float(input())
vendas  = float(input())

salario = salario + ((15/100)*vendas)

print(nome)
print("R$","{:.2f}".format(salario))