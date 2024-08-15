numCaixa = int(input())
saldo = 100

caixas = []
for i in range(numCaixa):
    caixas.append(int(input()))

caixas.reverse()
for i in caixas:
    if(sum(caixas) < 0):
        
        del(caixas[i])
        print(caixas)
    else:
        saldo = saldo + sum(caixas)
        print('vale a pena')
        break
print(saldo)
    





        



