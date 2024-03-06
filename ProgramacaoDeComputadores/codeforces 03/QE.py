n = int(input())
resultado = (n + 1)%2
proximopar = 0
if ( resultado == 0):
    proximopar = n + 1
    print(proximopar)
else: 
    proximopar = n + 2
    print(proximopar)