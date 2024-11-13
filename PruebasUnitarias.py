from Funciones import *

# -----------------------------------------------
# PRUEBAS UNITARIAS
# -----------------------------------------------

# Pruebas para generar_primo
rango_inferior = 10
rango_superior = 50
for _ in range(10):  # Generar 10 números primos para verificar la validez
   primo = generar_primo(rango_inferior, rango_superior)
   assert primo > 1 and all(primo % i != 0 for i in range(2, int(primo**0.5) + 1)), f"Error: El número {primo} no es primo"
   print(f"Número primo generado: {primo}")

# Pruebas para mcd
assert mcd(54, 24) == 6, "Error: mcd(54, 24) debería ser 6"
assert mcd(17, 31) == 1, "Error: mcd(17, 31) debería ser 1"
assert mcd(101, 103) == 1, "Error: mcd(101, 103) debería ser 1"
print("Pruebas de MCD superadas.")


# Pruebas para inverso_modular
assert inverso_modular(3, 11) == 4, "Error: inverso_modular(3, 11) debería ser 4"
assert inverso_modular(7, 40) == 23, "Error: inverso_modular(7, 40) debería ser 23"

try:
   inverso_modular(6, 9)  # El MCD de 6 y 9 es 3, no coprimos, debería dar error
except ValueError:
   print("Correctamente lanzó un error para inverso_modular(6, 9)")

print("Pruebas de inverso_modular superadas.")


# Pruebas para generar_llaves
llave_publica, llave_privada = generar_llaves(rango_inferior, rango_superior)
if llave_publica is None:
   print("No se pudo generar llaves distintas")
else:
   n_publico, e = llave_publica
   n_privado, d = llave_privada

   # Verificar que las llaves pública y privada tienen el mismo n
   assert n_publico == n_privado, "Error: Las llaves pública y privada no tienen el mismo n"
   assert e != d, "Error: e y d deberían ser diferentes"
   print("Llave pública:", llave_publica)
   print("Llave privada:", llave_privada)
print("Pruebas de generación de llaves superadas.")



# Pruebas para el proceso de encriptación y descriptación:
# Claves de prueba
public_key = (17, 3233)
private_key = (2753, 3233)

# Pruebas para encriptar y desencriptar
message = "SIUUU AMIGOS"
print(f"Mensaje original: {message}")

# Cifrado
blocksEncrypted = encriptar(message, *public_key)
assert isinstance(blocksEncrypted, list) and all(isinstance(block, int) for block in blocksEncrypted), "Error: Los bloques cifrados deben ser una lista de enteros"
print(f"Bloques cifrados: {blocksEncrypted}")

# Descifrado
DescryptedMessage = desencriptar(blocksEncrypted, *private_key)
assert DescryptedMessage == message, f"Error: El mensaje descifrado '{DescryptedMessage}' no coincide con el mensaje original '{message}'"
print(f"Mensaje descifrado: {DescryptedMessage}")

print("Pruebas de encriptación y desencriptación superadas.")