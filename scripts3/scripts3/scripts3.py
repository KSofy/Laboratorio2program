# _*_ coding: iso-8859-1 _*_
#VerificaciondeAcceso
#if-else o switch
#if-else, debido al tipo de condiciones. 

def verificar_acceso(nombre_usuario, contraseņa):
  nombre_correcto = "sofia"  
  contraseņa_correcta = "123"  

  if nombre_usuario == nombre_correcto and contraseņa == contraseņa_correcta:
    return "Acceso concedido"
  elif nombre_usuario == nombre_correcto:
    return "Contraseņa incorrecta"
  else:
    return "Usuario no registrado"

nombre = input("Ingrese nombre de usuario: ")
clave = input("Ingrese contraseņa: ")

resultado = verificar_acceso(nombre, clave)
print(resultado)
