
import random as r
import numpy as np

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
      raise ValueError("Los valores ingresados tienen que ser positivos")
   
   #Se intercambian los valores si a < b
   if a < b:
      a, b = b,a
   
   #Ecuación de Euclides
   while b != 0:  # Mientras b no sea 0 se ejecuta el ciclo
      r = a % b # Se calcula el residuo de la división de a entre b
      a = b # Se asigna el valor de b a a
      b = r # Se asigna el valor de r a b
   return a # Se retorna el valor de a

def inverso_modular(e, n):
   # Verificar que los valores ingresados sean positivos
   if e <= 0 or n <= 0:
      raise ValueError("Los valores ingresados tienen que ser positivos")
   
   # Verificar que el mcd sea 1 (es decir, que e y n sean coprimos)
   if mcd(e, n) != 1:
      raise ValueError("Los valores ingresados no son coprimos, por lo tanto no tienen inverso modular")
   
   # Inicialización del Algoritmo Extendido de Euclides
   c, d = n, e
   t1, t2 = 0, 1  # Inicialmente t1 = 0, t2 = 1, estos representan los coeficientes de la combinación lineal

   while d > 0:
      q = c // d  # Cociente de la división entera
      r = c % d   # Residuo de la división
      c, d = d, r  # Actualizar residuos

      # Actualizar los coeficientes t
      t = t1 - q * t2
      t1, t2 = t2, t

   # Ajustar el valor del inverso si es negativo
   if t1 < 0:
      t1 = t1 + n

   return t1


def generar_llaves(rango_inferior, rango_superior):
   #Generar primos p y q
   p = generar_primo(rango_inferior, rango_superior)
   q = generar_primo(rango_inferior, rango_superior)

   #verificar que p y q sean diferentes
   while p == q:
      q = generar_primo(rango_inferior, rango_superior)

   #Calcular n
   n = p*q

   #Calcular phi
   phi = (p-1)*(q-1)

   #Generar e aleatorio entre 1 < e < phi y el mcd(e,phi) == 1
   e = r.randint(2,phi - 1)
   while mcd(e,phi)!=1:
      e = r.randint(2,phi - 1)
   
   #Calcular d el inverso modular de e
   d = inverso_modular(e,phi)

   if d == None:
      e = r.randint(2,phi - 1)
      while mcd(e,phi)!=1:
         e = r.randint(2,phi - 1)
      d = inverso_modular(e,phi)
   
   #Llaves
   llave_publica = (n,e)
   llave_privada = (n,d)

   #Se retornan las llaves
   return llave_publica, llave_privada

def encriptar(caracter, e, n): 
   concatValues = ""
   blocks = []
   for char in caracter:
      concatValues += str(ord(char))
   print(concatValues)
      
   if int(concatValues) > n:
      strMessage = str(concatValues)
      blockSize = len(str(n)) - 1 #Tamaño del bloque menor a n
      blocks = [int(strMessage[i:i+blockSize]) for i in range(0, len(strMessage), blockSize)]
   else:
      blocks.append(int(concatValues))
      
   encryptedBlocks = [pow(block, e, n) for block in blocks]
   return encryptedBlocks
# Compuesto por e y n
public_key = (65454, 999989)
e, n = public_key
print(encriptar("Holaa", e, n))

#def desencriptar(caracter_encriptado, llave_privada):

