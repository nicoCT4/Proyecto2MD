
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

def inverso_modular(e,n):
   #verificar que sean positivos
   if e <=0 or n <=0:
      raise ValueError("Los valores ingresados tienen que ser positivos")
   
   #Verificamos que el mcd sea 1
   if mcd(e,n)!=1:
      raise ValueError("Los valores ingresados no son coprimos, por lo tanto no tienen inverso modular")
   
   #Algoritmo extendido de Euclides
   c = e
   d = n
   #Matriz identidad
   m = np.array([
         [1,0],
         [0,1]
   ])


   while d != 0:
      q = c//d #División entera
      r = c%d #Residuo
      c = d #Se asigna el valor de d a c
      d = r #Se asigna el valor de r a d

      #Matriz de transformación
      Q1 = np.array([
         [0,1],
         [1,-q]
      ])

      #Multiplicación de matrices
      m = Q1@m

   x = m[0][0]

   if x < 0:
      x = (x+n)%n

   return x


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
   # Converte cada caracter en valor ASCII con al menos 3 digitos
   for char in caracter:
      concatValues += str(ord(char)).zfill(3) 
   # Dividir en bloques si el número es mayor que n
   if int(concatValues) > n:
      blockSize = len(str(n)) - 1  
      blocks = [int(concatValues[i:i+blockSize]) for i in range(0, len(concatValues), blockSize)]
   else:
      blocks.append(int(concatValues))
   # Cifrar cada bloque con formula c = m^n mod(n) pow(base, exp, mod)
   encryptedBlocks = [pow(block, e, n) for block in blocks]
   return encryptedBlocks

def desencriptar(blocks, d, n):
   # Descifrar con formula m = c^d mod(n) pow(base, exp, mod)
   decryptBlocks = [pow(block, d, n) for block in blocks]
   fullMessage = ''.join(str(block).zfill(3) for block in decryptBlocks) # Mangener lontitud minima de 3
   # Convierte en ASCII de nuevo los valores.
   descryptMessage = ''.join(
      chr(int(fullMessage[i:i+3])) for i in range(0, len(fullMessage), 3)
   )
   return descryptMessage

