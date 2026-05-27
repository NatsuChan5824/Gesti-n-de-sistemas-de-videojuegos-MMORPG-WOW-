##  WOW MIDNIGHT
import os

usuario_guardado = "admin"
clave_guardada = "sunwell"
esta_registrado = True
continuar = True

while continuar == True:

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("========================================")
    print("    SISTEMA DE ACCESO: WOW MIDNIGHT")
    print("========================================")
    print("1. Iniciar Sesion")
    print("2. Registrarte")
    print("3. Salir")
    print("----------------------------------------")
    
    # REQUISITO: Uso de .strip() para limpiar la entrada
    opcion = input("Elija una opcion (1-3): ").strip()

    if opcion == "1":

        if esta_registrado == False:
            print("Error: No hay usuarios registrados.")
            input("Presione Enter para volver...")
        else:
            acceso = False
            # REQUISITO: Bucle while para validar hasta que sea correcto
            while acceso == False:
                print("\n--- LOGIN ---")
                # REQUISITO: Uso de .lower() para el usuario
                user_ingresado = input("Usuario: ").strip().lower()
                pass_ingresada = input("Clave: ").strip()

                if user_ingresado == usuario_guardado and pass_ingresada == clave_guardada:
                    print("\nAcceso concedido. ¡Bienvenido Forestal!")
                    acceso = True
                    
                    # REQUISITO: Muestra de datos del sistema (Semana 1)
                    print("\n--- INFORMACION DEL SISTEMA ---")
                    mana_cristal = 1000
                    # REQUISITO: Uso de comillas triples
                    mensaje = """ALERTA: El Vacio esta cerca de la Fuente del Sol"""
                    
                    # REQUISITO: Uso de .replace() y Slicing
                    mensaje_nuevo = mensaje.replace("Vacio", "ENEMIGO")
                    abreviacion = mensaje[0:6]
                    
                    print("Mana disponible:", mana_cristal)
                    print("Mensaje:", mensaje_nuevo)
                    print("Codigo:", abreviacion)
                    
                    input("\nPresione Enter para cerrar sesion...")
                else:
                    print("\nUsuario o clave incorrectos.")
                    reintentar = input("¿Quiere intentar otra vez? (s/n): ").lower()
                    if reintentar != "s":
                        break
    elif opcion == "2":

        print("\n--- REGISTRO DE NUEVO USUARIO ---")
        usuario_guardado = input("Cree su usuario: ").strip().lower()
        clave_guardada = input("Cree su clave: ").strip()
        esta_registrado = True
        print("¡Registro exitoso!")
        input("Presione Enter para volver al menu...")
    elif opcion == "3":
        # REQUISITO: Uso de .upper() para confirmar salida
        confirmar = input("\n¿Seguro que quiere SALIR? (SI/NO): ").strip().upper()
        if confirmar == "SI":
            print("Cerrando sistema... Por Quel'Thalas.")
            continuar = False       
    else:
        print("Opcion no valida.")
        input("Presione Enter para continuar...")