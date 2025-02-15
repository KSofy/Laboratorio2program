# _*_ coding: iso-8859-1 _*_
#Dia de la semana

#if-else o switch
#switch, ya que es mas eficiente cuando hay mas opciones, pero usare if-else debido a que switch no existe como tal.


def dia_semana(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return "No válido"

numero = int(input("Ingrese un numero del 1 al 7: "))
dia = dia_semana(numero) 
print (dia)