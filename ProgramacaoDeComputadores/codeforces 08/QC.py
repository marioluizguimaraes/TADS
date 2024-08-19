tamanhoDoPulo, nomeroDeCanos = map(int, input().split())
tamanhoDosCanos = list(map(int, input().split()))
passou = False
 
for i in range(1, len(tamanhoDosCanos)):
    if tamanhoDosCanos[i] > tamanhoDosCanos[i-1] :
        if tamanhoDoPulo >= tamanhoDosCanos[i] - tamanhoDosCanos[i-1]:
            passou = True     
        else:  
            passou = False
            break
    else:
        if tamanhoDoPulo >= (tamanhoDosCanos[i] - tamanhoDosCanos[i-1])*-1:
            passou = True     
        else:
            passou = False
            break
 
if passou:
    print('YOU WIN')
else:
    print('GAME OVER')