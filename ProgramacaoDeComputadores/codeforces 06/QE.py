def dia_da_semana(h,d):
    dia = 0
    data = ""
    if (h == "Domingo"):
        dia = (d%7) + 1
        if(dia > 7):
           dia = (dia%7) 
    elif(h == "Segunda-feira"):
        dia = (d%7) + 2
        if(dia > 7):
           dia = (dia%7) 
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


hj = input()
dias = int(input())

print(dia_da_semana(hj,dias))
    


    
