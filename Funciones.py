#Generar primo aleatorio
import random as r
def generar_primo(rango_inferior, rango_superior):
      while True:
         numero = r.randint(rango_inferior, rango_superior)
         if numero > 1:
               #Se verifica si el número es primo con su raíz cuadrada
               for i in range(2, int(numero**0.5)+1):
                  if numero % i == 0:
                     break
               else:
                  return numero

def mcd(a, b):
   #Se verifica que los valores ingresados sean positivos
   if a <= 0 or b <= 0:
      print("Los valores ingresados tienen que ser positivos")
      exit()
   #Se intercambian los valores si a < b
   if a < b:
      a, b = b,a
      print("Se han intercambiado los valores: ahora a = " + str(a) + " y b = " + str(b))
   else:
      while b != 0:  # Mientras b no sea 0 se ejecuta el ciclo
         r = a % b # Se calcula el residuo de la división de a entre b
         a = b # Se asigna el valor de b a a
         b = r # Se asigna el valor de r a b
      return a # Se retorna el valor de a

#def inverso_modular(e,n):

#def generar_llaves(rango_inferior, rango_superior):

#def encriptar(caracter, llave_publica):

#def desencriptar(caracter_encriptado, llave_privada):

