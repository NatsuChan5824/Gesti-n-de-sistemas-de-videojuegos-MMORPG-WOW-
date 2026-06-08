
import os

usuario_admin = "forestal"
clave_admin = "sunwell2026"

usuario_nuevo = ""
clave_nueva = ""
existe_registro = False
correr_programa = True
mana_fuente = 750         
defensores_elfos = 120 

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
                input("Presione Enter para ingresar al Panel Táctico...")
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("========================================")
                    print("   PANEL DE CONTROL MILITAR: SILVERMOON")
                    print("========================================")
                    print(f" -> Reserva de Maná: {mana_fuente} MP")
                    print(f" -> Defensores Elfos: {defensores_elfos} activos")
                    print("----------------------------------------")
                    print("1. Reclutar batallón (Suma defensores)")
                    print("2. Canalizar escudo místico (Resta Maná)")
                    print("3. Generar reporte estratégico (Texto)")
                    print("Escriba 'SALIR' para desconectar la sesión.")
                    print("----------------------------------------")
                    
                    opcion_menu = input("Seleccione una accion: ").strip().upper()
                    
                    if opcion_menu == "SALIR":
                        print("\nCerrando sesión táctica... Que la Luz te guíe.")
                        input("Presione Enter para volver al menú de inicio...")
                        break 
                    
                    elif opcion_menu == "1":
                        print("\n--- CONVOCATORIA DE DEFENTORES ---")
                        nuevos = input("¿Cuántos elfos deseas reclutar para las filas?: ").strip()
                        if nuevos.isdigit():
                            cantidad = int(nuevos)
                            defensores_elfos += cantidad 
                            print(f"[ÉXITO] ¡Se han sumado {cantidad} defensores a Quel'Thalas!")
                        else:
                            print("[ERROR] Debe ingresar un número entero válido.")
                        input("Presione Enter para continuar...")
                        
                    elif opcion_menu == "2":
                        print("\n--- BARRERA DEFENSIVA DE LA FUENTE ---")
                        costo = 150
                        if mana_fuente >= costo:
                            mana_fuente -= costo 
                            print(f"[CONCHADO] Escudo activado. Se consumieron {costo} MP de Maná.")
                        else:
                            print("[ALERTA] Maná insuficiente. ¡La Fuente del Sol necesita recargarse!")
                        input("Presione Enter para continuar...")
                        
                    elif opcion_menu == "3":
                        print("\n--- REPORTE DE LA FUENTE DEL SOL ---")
                        
                        info = """ALERTA: Se detectan sombras en el horizonte místico."""
                        
                        info_modificada = info.replace("sombras", "ENEMIGOS DE LA NOCHE")
                        
                        fragmento = info_modificada[0:15]
                        
                        print("Texto Original:  ", info)
                        print("Texto Modificado:", info_modificada)
                        print("Código de rastro (Slicing 0:15):", fragmento)   
                        
                        input("\nPresione Enter para continuar...")
                        
                    else:
                        print("\n[ERROR] Opción no reconocida dentro del panel.")
                        input("Presione Enter para intentar de nuevo...")
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
        confirmar = input("\n¿Seguro que desea SALIR? (SI/NO): ").strip().upper()
        if confirmar == "SI":
            print("Cerrando sistema... Por Quel'Thalas.")
            correr_programa = False          
    else:
        print("Opcion no reconocida.")
        input("Presione Enter para continuar...")