distancia  = int(input())
velocidade = int(input())
tempo_h    = distancia//velocidade
tempo_m    = int(((distancia/velocidade) - tempo_h ) *0.6 * 100)

print("{:02d}".format(tempo_h) , "{:02d}".format(tempo_m) , sep=":")
