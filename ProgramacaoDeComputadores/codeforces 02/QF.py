distancia  = int(input())
velocidade = int(input())
tempo_h    = distancia//velocidade
tempo_m    = input((distancia%velocidade)*3.6)

print(tempo_h , tempo_m , sep=":")
