import random as r
import numpy as np

def generar_primo(rango_inferior, rango_superior):
      """
         Genera un número primo aleatorio dentro de un rango dado.

      Args:
         rango_inferior (int): Límite inferior del rango de búsqueda.
         rango_superior (int): Límite superior del rango de búsqueda.

      Returns:
         int: Un número primo aleatorio dentro del rango especificado.

      Raises:
         ValueError: Si no se puede encontrar un número primo dentro del rango.
      """
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
   """
   Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.

   Args:
      a (int): Primer número entero positivo.
      b (int): Segundo número entero positivo.

   Returns:
      int: El MCD de los números proporcionados.

   Raises:
      ValueError: Si los valores ingresados no son positivos.
   """
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
   """
   Calcula el inverso modular de e módulo n utilizando el algoritmo extendido de Euclides.

   Args:
      e (int): Número entero cuyo inverso modular se calcula.
      n (int): Módulo de la operación.

   Returns:
      int: Inverso modular de e módulo n.

   Raises:
      ValueError: Si los valores ingresados no son positivos o no son coprimos.
   """
   #verificar que sean positivos
   if e <= 0 or n <= 0:
      raise ValueError("Los valores ingresados tienen que ser positivos")
   
   #Verificamos que el mcd sea 1
   if mcd(e, n) != 1:
      raise ValueError("Los valores ingresados no son coprimos, por lo tanto no tienen inverso modular")
   
   #Algoritmo extendido de Euclides
   c = e
   d = n
   #Matriz identidad
   m = np.array([
         [1, 0],
         [0, 1]
   ], dtype=int)

   while d != 0:
      q = c // d # División entera
      r = c % d # Residuo
      c, d = d, r # Actualización de c y d

      # Matriz de transformación
      Q1 = np.array([
         [0, 1],
         [1, -q]
      ], dtype=int)

      # Multiplicación de matrices
      m = Q1 @ m

   x = int(m[0][0])

   if x < 0:
      x = (x + n) % n

   return x

def generar_llaves(rango_inferior, rango_superior):
   """
   Genera un par de claves RSA (pública y privada).

   Args:
      rango_inferior (int): Límite inferior para la búsqueda de números primos.
      rango_superior (int): Límite superior para la búsqueda de números primos.

   Returns:
      tuple: Una tupla que contiene:
         - llave_publica (tuple): La llave pública (n, e).
         - llave_privada (tuple): La llave privada (n, d).

   Raises:
      ValueError: Si no se pueden generar llaves válidas en el rango dado.
   """
   #Generar primos p y q
   p = generar_primo(rango_inferior, rango_superior)
   q = generar_primo(rango_inferior, rango_superior)

   #verificar que p y q sean diferentes
   while p == q:
      q = generar_primo(rango_inferior, rango_superior)

   #Calcular n
   n = p * q

   #Calcular phi
   phi = (p - 1) * (q - 1)

   #Generar e aleatorio entre 1 < e < phi y el mcd(e, phi) == 1
   e = r.randint(2, phi - 1)
   while mcd(e, phi) != 1:
      e = r.randint(2, phi - 1)
   
   #Calcular d el inverso modular de e
   d = inverso_modular(e, phi)

   if d is None:
      e = r.randint(2, phi - 1)
      while mcd(e, phi) != 1:
         e = r.randint(2, phi - 1)
      d = inverso_modular(e, phi)
   
   #Llaves
   llave_publica = (n, e)
   llave_privada = (n, d)

   #Se retornan las llaves
   return llave_publica, llave_privada

def encriptar(mensaje, e, n):
   """
      Encripta un número utilizando la llave pública RSA.

   Args:
      mensaje (int): El número a encriptar.
      e (int): Exponente público.
      n (int): Módulo público.

   Returns:
      int: Número encriptado.

   Raises:
      ValueError: Si el número a encriptar es mayor o igual a n.
   """
   if int(mensaje) >= n:
      raise ValueError("El número a encriptar debe ser menor que n.")
   # Aplicamos la fórmula de encriptación
   mensaje_encriptado = pow(int(mensaje), e, n)
   return mensaje_encriptado
   # concatValues = ""
   # blocks = []
   # # Converte cada caracter en valor ASCII con al menos 3 digitos
   # for char in caracter:
   #    concatValues += str(ord(char)).zfill(3) 
   # # Dividir en bloques si el número es mayor que n
   # if int(concatValues) > n:
   #    blockSize = len(str(n)) - 1  
   #    blocks = [int(concatValues[i:i+blockSize]) for i in range(0, len(concatValues), blockSize)]
   # else:
   #    blocks.append(int(concatValues))
   # # Cifrar cada bloque con formula c = m^e mod(n) usando pow(base, exp, mod)
   # encryptedBlocks = [pow(block, e, n) for block in blocks]
   # return encryptedBlocks

def desencriptar(mensaje_encriptado, d, n):
   """
   Desencripta un número encriptado utilizando la llave privada RSA.

   Args:
      mensaje_encriptado (int): El número encriptado.
      d (int): Exponente privado.
      n (int): Módulo público.

   Returns:
      int: Número desencriptado.
   """
   mensaje_desencriptado = pow(int(mensaje_encriptado), d, n)
   return mensaje_desencriptado
   #Codigo para palabras
   # # Descifrar con formula m = c^d mod(n) usando pow(base, exp, mod)
   # decrypt_blocks = [pow(int(block), int(d), int(n)) for block in blocks]
   # full_message = ''.join(str(block).zfill(3) for block in decrypt_blocks) # Mantener longitud mínima de 3
   
   # # Convertir cada grupo de 3 dígitos en el carácter ASCII correspondiente
   # decrypted_message = ''
   # for i in range(0, len(full_message), 3):
   #    try:
   #       ascii_value = int(full_message[i:i + 3])
   #       # Asegurarse de que el valor ASCII esté en el rango válido
   #       if 32 <= ascii_value <= 126:  # Solo caracteres imprimibles
   #          decrypted_message += chr(ascii_value)
   #       else:
   #          print(f"Error: valor {ascii_value} fuera del rango ASCII imprimible.")
   #          return None
   #    except ValueError:
   #       # Capturar un error si el valor no está dentro del rango ASCII
   #       print(f"Error: valor {full_message[i:i + 3]} fuera del rango ASCII.")
   #       return None
   #    except OverflowError:
   #       # Capturar un error si el valor es demasiado grande para convertirse en un carácter
   #       print(f"Error: valor {full_message[i:i + 3]} es demasiado grande.")
   #       return None

   # return decrypted_message