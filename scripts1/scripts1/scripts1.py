# _*_ coding: iso-8859-1 _*_
#clasificaiondeedad

#¿if-else o switch?
#if-else, ya que hay rangos de edad y condiciones que no son mutuamente excluyentes.

edad = int(input( "Ingrese la edad: "))

if edad < 12:
 print("Niño")
elif edad < 18:
 print("Adolescente")
elif edad < 60:
 print("Adulto")
else:
 print("Adulto Mayor")

