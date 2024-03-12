c, q = map(int, input().split())
valor = 0
if(c == 1):
    valor = 4.00 * q

elif( c == 2):  
    valor = 4.50 * q 

elif( c == 3):
    valor = 5.00 * q 

elif( c == 4):
    valor = 2.00 * q

elif( c == 5):
    valor = 1.50 * q 

print("Total: R$", "{:.2f}".format(valor))
