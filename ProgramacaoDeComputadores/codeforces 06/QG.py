

    
def dia(dia, mes, ano):
    d = int(dia)
    m = int(mes)
    a = int(ano)
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (a > 31 or a < 1 or m < 1 or m > 12 or a > 10000):
        data = "Data Invalida"
    
    for i in range(0, 12):
        if(m - 1 == i):
            ms = meses[i]
            dx = dias[i]
    if(d > dx):
        data = "Data Invalida"
    else:
        data = f'{d:02d} de {ms} de {ano}'
        
    return data
    

d,m,a = map(str, input().split("/"))
print(dia(d,m,a))