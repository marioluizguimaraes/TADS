def verifc_mes(m):
    mes = ""
    if( m == 1):
        mes = "janeiro"
    elif(m == 2):
        mes = "fevereiro"
    elif(m == 3):
        mes = "março"
    elif(m == 4):
        mes = "abriu"
    elif(m == 5):
        mes = "maio"
    elif(m == 6):
        mes = "junho"
    elif(m == 7):
        mes = "julho"
    elif(m == 8):
        mes = "agosto"
    elif(m == 9):
        mes = "setembro"
    elif(m == 10):
        mes = "outubro"
    elif(m == 11):
        mes = "novembro"
    elif(m == 12):
        mes = "dezembro" 
    return mes
    
def dia(dia, mes, ano):
    d = int(dia)
    m = int(mes)
    a = int(ano)
    data = ""

    if (d > 31 or d < 1 or m > 12 or m < 1 or a > 10000):
        data = "Data Invalida"
    
    else:
        a = str(ano)
        if (d > 10):
            d = "0" + str(dia)
            data = d + " de " + verifc_mes(m) + " de " + a
        else: 
            data = dia + " de " + verifc_mes(m) + " de " + a

    return data
    

d,m,a = map(str, input().split("/"))
print(dia(d,m,a))