def dia(dia, mes, ano):
    data = ""
    if (dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano > 10000):
        data = "Data Invalida"
    
    
        d = (d%7) + 1
        if(d > 7):
           d = (d%7) 
    elif(h == "Segunda-feira"):
        d = (d%7) + 2
        if(d > 7):
           d = (d%7) 
    elif(h == "Terca-feira"):
        dia = (d%7) + 3
        if(dia > 7):
           dia = (dia%7) 
    elif(h == "Quarta-feira"):
        dia = (d%7) + 4
        if(dia > 7):
           dia = (dia%7) 
    elif(h == "Quinta-feira"):
        dia = (d%7) + 5
        if(dia > 7):
           dia = (dia%7) 
    elif(h == "Sexta-feira"):
        dia = (d%7) + 6
        if(dia > 7):
           dia = (dia%7) 
    elif(h == "Sabado"):
        dia = (d%7) + 7
        if(dia > 7):
           dia = (dia%7) 
 
    if (dia == 1):
        data = "Domingo"
    elif (dia == 2):
        data = "Segunda-feira"
    elif (dia == 3):
        data = "Terca-feira"
    elif (dia == 4):
        data = "Quarta-feira"
    elif (dia == 5):
        data = "Quinta-feira"
    elif (dia == 6):
        data = "Sexta-feira"
    elif (dia == 7):
        data = "Sabado"   
    return data