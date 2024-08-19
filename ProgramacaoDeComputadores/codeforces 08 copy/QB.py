tempo, massag = map(int, input().split())
 
dias    = 0
horas   = 0
minutos = 0
segundos = 0
 
while (massag>=0.5):
    massag = massag/2
    segundos += tempo
 
dias = segundos//86400
segundos = segundos%86400
horas = segundos//3600
segundos = segundos%3600
minutos = segundos//60
segundos = segundos%60
 
 
print(f"{dias} dias {horas:02d}:{minutos:02d}:{segundos:02d}")