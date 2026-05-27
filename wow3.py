## WOW MIDNIGHT
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
usuario_registrado = ""
clave_registrada = ""
esta_registrado = False
continuar_programa = True

while continuar_programa:
    limpiar()
    print("--- MENU DE ACCESO: WOW MIDNIGHT ---")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")

## REQUISITO: Uso de .strip() para limpiar la entrada del usuario
    opcion = input("Elija una opción: ").strip()

    if opcion == "1":
        print("\n--- REGISTRO DE NUEVO USUARIO ---")
        ## REQUISITO: Uso de .lower() para el usuario
        usuario_registrado = input("Cree su nombre de usuario: ").strip().lower()
        clave_registrada = input("Cree su contraseña: ").strip()
        esta_registrado = True
        print("Registro completado con éxito.")
        input("Presione Enter para volver al menú...")

    elif opcion == "2":
        if esta_registrado == False:
            print("\nError: Primero debe registrarse.")
            input("Presione Enter para continuar...")
        else:
            ## REQUISITO: Bucle de seguridad (While)
            acceso_correcto = False
            
            while acceso_correcto == False:
                print("\n--- INICIO DE SESIÓN ---")
                user_ingresado = input("Usuario: ").strip().lower()
                pass_ingresada = input("Contraseña: ").strip()

                if user_ingresado == usuario_registrado and pass_ingresada == clave_registrada:
                    print("\n¡Bienvenido al sistema de Quel'Thalas!")
                    acceso_correcto = True
                    
                    ## REQUISITO: Segunda parte (Variables Numéricas y Texto)
                    mana_total = 500 
                    
                    print(f"Estado de la Fuente del Sol: {mana_total} de Maná.")
                    print("\n--- PROCESANDO MENSAJE CORRUPTO ---")
                    
                    ## REQUISITO: Uso de comillas triples
                    mensaje_vacio = """ESTE_ES_UN_MENSAJE_DEL_VACIO"""
                    
                    ## REQUISITO: Uso de .replace() y Slicing (Corte)
                    mensaje_limpio = mensaje_vacio.replace("_", " ")
                    palabra_clave = mensaje_vacio[0:4]
                    
                    print(f"Texto original: {mensaje_vacio}")
                    print(f"Texto corregido: {mensaje_limpio}")
                    print(f"Código detectado: {palabra_clave}")
                    
                    input("\nPresione Enter para salir del sistema...")
                    break 
                else:
                    print("Clave incorrecta. Intente de nuevo.")
                    reintentar = input("¿Quiere intentar otra vez? (s/n): ").lower()
                    if reintentar == "n":
                        break
    elif opcion == "3":
        ## REQUISITO: Uso de .upper() para confirmar salida
        confirmar = input("¿Realmente desea SALIR? (SI/NO): ").strip().upper()
        if confirmar == "SI":
            print("Cerrando sistema... ¡Por Quel'Thalas!")
            continuar_programa = False 
    else:
        print("Opción no válida.")
        input("Presione Enter para intentar de nuevo...")