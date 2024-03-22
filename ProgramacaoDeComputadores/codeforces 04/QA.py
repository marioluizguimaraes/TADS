#Frota de Taxi

a, g, ra, rg = map(float, input().split())

alco = ra/a
gasolina = rg/g

if ( alco > gasolina):
    print("A")
else:
    print("G")
    