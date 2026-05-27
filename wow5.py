## WOW MIDNIGHT
import os

usuario_admin = "forestal"
clave_admin = "sunwell2026"

usuario_nuevo = ""
clave_nueva = ""
existe_registro = False
correr_programa = True

while correr_programa == True:

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("========================================")
    print("    DEFENSA DE QUEL'THALAS: MIDNIGHT")
    print("========================================")
    print("1. Iniciar Sesion")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    print("----------------------------------------")
    
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
      
        bloqueo = True
        
        while bloqueo == True:
            print("\n--- PANTALLA DE LOGIN ---")
            u_ingresado = input("Ingrese Usuario: ").strip().lower()
            c_ingresada = input("Ingrese Clave: ").strip()

            if (u_ingresado == usuario_admin and c_ingresada == clave_admin) or \
               (existe_registro == True and u_ingresado == usuario_nuevo and c_ingresada == clave_nueva):
                
                print("\n[ACCESO CORRECTO] ¡Bienvenido al sistema!")
                bloqueo = False
                print("\n--- REPORTE DE LA FUENTE DEL SOL ---")
                mana = 750
                
                ## REQUISITO: Comillas triples
                info = """ALERTA: Se detectan sombras en el horizonte."""
                
                ##  REQUISITO: .replace() y Slicing
                info_modificada = info.replace("sombras", "ENEMIGOS")
                fragmento = info[0:15]
                
                print("Mana actual:", mana)
                print("Estado:", info_modificada)
                print("ID de rastro:", fragmento)   
                input("\nPresione Enter para cerrar sesion...")
            else:
                print("\n[ERROR] Datos incorrectos.")
                reintentar = input("¿Intentar de nuevo? (s/n): ").strip().lower()
                if reintentar == "n":
                    bloqueo = False
    elif opcion == "2":
        print("\n--- REGISTRO DE NUEVO FORESTAL ---")
        usuario_nuevo = input("Cree su nombre de usuario: ").strip().lower()
        clave_nueva = input("Cree su contraseña: ").strip()
        existe_registro = True
        print("Usuario registrado exitosamente.")
        input("Presione Enter para volver...")
    elif opcion == "3":
        ## REQUISITO: .upper() para confirmar la salida
        confirmar = input("\n¿Seguro que desea SALIR? (SI/NO): ").strip().upper()
        if confirmar == "SI":
            print("Cerrando sistema... Por Quel'Thalas.")
            correr_programa = False         
    else:
        print("Opcion no reconocida.")
        input("Presione Enter para continuar...")