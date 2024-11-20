from Funciones import *

def main():
    print("=== Sistema de Encriptación RSA ===\n")
    
    llave_publica = None
    llave_privada = None
    mensaje_encriptado = None

    while True:
        print("\nMenú:")
        print("1. Generar llaves")
        print("2. Encriptar un mensaje")
        print("3. Desencriptar un mensaje")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                rango_inferior = int(input("Ingrese el rango inferior para generar primos: "))
                rango_superior = int(input("Ingrese el rango superior para generar primos: "))
                llave_publica, llave_privada = generar_llaves(rango_inferior, rango_superior)
                print("\nLlaves generadas correctamente:")
                print(f"Clave pública: {llave_publica}")
                print(f"Clave privada: {llave_privada}")
            except ValueError:
                print("Error: Asegúrese de ingresar números enteros válidos.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        elif opcion == '2':
            if llave_publica is None:
                print("Primero debe generar las llaves.")
                continue
            mensaje = input("Ingrese el mensaje a encriptar: ")
            mensaje_encriptado = encriptar(mensaje, llave_publica[1], llave_publica[0])
            print(f"\nMensaje encriptado: {mensaje_encriptado}")
        
        elif opcion == '3':
            if llave_privada is None or mensaje_encriptado is None:
                print("Primero debe generar las llaves y encriptar un mensaje.")
                continue
            mensaje_desencriptado = desencriptar(mensaje_encriptado, llave_privada[1], llave_privada[0])
            print(f"\nMensaje desencriptado: {mensaje_desencriptado}")
        
        elif opcion == '4':
            print("Saliendo del programa. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
