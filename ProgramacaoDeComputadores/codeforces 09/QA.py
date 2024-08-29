numeroJogadores, rodadas = map(int, input().split())
pontos = list(map(int, input().split()))
pontosJogadores = []

for i in range(numeroJogadores):
    somaPontos = pontos[i]
    indice = i

    for x in range(1, rodadas):
            indice = indice + numeroJogadores
            somaPontos = somaPontos + pontos[indice]
    
    pontosJogadores.append(somaPontos)

if (pontosJogadores.count(max(pontosJogadores)) > 1):
   
    for i in range(len(pontosJogadores)):
        if (pontosJogadores[i] == max(pontosJogadores)):
             ind_maior = i

    print(ind_maior+1)      

else:
    print(pontosJogadores.index(max(pontosJogadores))+1)