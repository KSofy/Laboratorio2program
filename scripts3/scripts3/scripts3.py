# _*_ coding: iso-8859-1 _*_
#VerificaciondeAcceso
#if-else o switch
#if-else, debido al tipo de condiciones. 

def verificar_acceso(nombre_usuario, contrase�a):
  nombre_correcto = "sofia"  
  contrase�a_correcta = "123"  

  if nombre_usuario == nombre_correcto and contrase�a == contrase�a_correcta:
    return "Acceso concedido"
  elif nombre_usuario == nombre_correcto:
    return "Contrase�a incorrecta"
  else:
    return "Usuario no registrado"

nombre = input("Ingrese nombre de usuario: ")
clave = input("Ingrese contrase�a: ")

resultado = verificar_acceso(nombre, clave)
print(resultado)
