# (WOW MIDNIGHT)
import os

usuario_admin = "forestal"
clave_admin = "sunwell2026"

usuario_nuevo = ""
clave_nueva = ""
existe_registro = False
correr_programa = True

## VARIABLES DE ESTADO INICIAL (REQUISITO 4 - SEMANA 2)
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
                
                ## [CÓDIGO DE LA SEMANA 2] - MENÚ PRINCIPAL OPERATIVO (Requisitos 2, 3 y 4)
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("========================================")
                    print("   PANEL DE CONTROL MILITAR: SILVERMOON")
                    print("========================================")
                    print(f" -> Reserva de Maná: {mana_fuente} MP")
                    print(f" -> Defensores Elfos: {defensores_elfos} activos")
                    print("----------------------------------------")
                    print("1. Gestionar batallón (Suma / Resta defensores)")
                    print("2. Gestionar nexo místico (Suma / Resta Maná)")
                    print("3. Generar reporte estratégico (Texto)")
                    print("Escriba 'SALIR' para desconectar la sesión.")
                    print("----------------------------------------")
                    
                    ## Limpieza de datos con .strip() y .upper()
                    opcion_menu = input("Seleccione una accion: ").strip().upper()
                    
                    ## Validación explícita de salida del menú continuo
                    if opcion_menu == "SALIR":
                        print("\nCerrando sesión táctica... Que la Luz te guíe.")
                        input("Presione Enter para volver al menú de inicio...")
                        break 
                    
                    ## ESTRUCTURA IF-ELIF-ELSE PARA ALTERACIÓN NUMÉRICA
                    elif opcion_menu == "1":
                        print("\n--- GESTIÓN DE BATALLÓN DE FORESTALES ---")
                        print("A. Reclutar nuevo batallón (Suma)")
                        print("B. Desplegar batallón a las fronteras (Resta)")
                        sub_opcion = input("Seleccione una acción (A/B): ").strip().upper()
                        
                        if sub_opcion == "A":
                            nuevos = input("¿Cuántos elfos deseas reclutar para las filas?: ").strip()
                            if nuevos.isdigit():
                                cantidad = int(nuevos)
                                defensores_elfos += cantidad 
                                print(f"[ÉXITO] ¡Se han sumado {cantidad} defensores a Quel'Thalas!")
                            else:
                                print("[ERROR] Debe ingresar un número entero válido.")
                                
                        elif sub_opcion == "B":
                            bajas = input("¿Cuántos elfos vas a desplegar/retirar del nexo?: ").strip()
                            if bajas.isdigit():
                                cantidad = int(bajas)
                                # Validación matemática protectora
                                if cantidad <= defensores_elfos:
                                    defensores_elfos -= cantidad 
                                    print(f"[DESPLIEGUE] {cantidad} forestales marcharon a la batalla.")
                                else:
                                    print(f"[ERROR] No puedes retirar {cantidad} defensores. Solo posees {defensores_elfos} activos.")
                            else:
                                print("[ERROR] Debe ingresar un número entero válido.")
                        else:
                            print("[ERROR] Opción secundaria inválida.")
                            
                        input("Presione Enter para continuar...")
                        
                    elif opcion_menu == "2":
                        print("\n--- GESTIÓN DEL NEXO MÍSTICO ---")
                        print("A. Meditar en la Fuente del Sol (Suma Maná)")
                        print("B. Canalizar escudo místico (Resta Maná)")
                        sub_opcion_mana = input("Seleccione una acción (A/B): ").strip().upper()
                        
                        if sub_opcion_mana == "A":
                            recarga = input("¿Cuánto maná deseas canalizar para la Fuente?: ").strip()
                            if recarga.isdigit():
                                cantidad_mana = int(recarga)
                                mana_fuente += cantidad_mana
                                print(f"[FUERZA] Se han restaurado +{cantidad_mana} MP a la reserva.")
                            else:
                                print("[ERROR] Debe ingresar un número entero válido.")
                        
                        elif sub_opcion_mana == "B":
                            costo_input = input("¿Cuánto maná deseas gastar en el escudo místico?: ").strip()
                            if costo_input.isdigit():
                                costo = int(costo_input)
                                if mana_fuente >= costo:
                                    mana_fuente -= costo 
                                    print(f"[CONJURADO] Escudo activado. Se consumieron {costo} MP de Maná.")
                                else:
                                    print(f"[ALERTA] Maná insuficiente. No puedes gastar {costo} MP (Posees {mana_fuente} MP).")
                            else:
                                print("[ERROR] Debe ingresar un número entero válido.")
                        else:
                            print("[ERROR] Opción secundaria inválida.")
                            
                        input("Presione Enter para continuar...")
                        
                    elif opcion_menu == "3":
                        ## SEMANA 3: MANIPULACIÓN DE CADENAS DE TEXTO (TEXTO LARGO Y DINÁMICO)
                        print("\n--- REPORTE DE LA FUENTE DEL SOL ---")
                        
                        info = """ALERTA DE ALTO RANGO: Los vigías forestales informan que se detectan densas sombras avanzando rápidamente desde las fronteras de las Tierras Fantasma. La Fuente del Sol ha manifestado una ligera fluctuación en su nexo de poder místico. Se recomienda a todos los defensores elfos preparar sus arcos y canalizar los escudos rúnicos de inmediato ante la inminente llegada de la medianoche."""
                        
                        print("====================================================================================================")
                        print("TEXTO ACTUAL DEL REPORTE EMITIDO POR LOS VIGÍAS:")
                        print("====================================================================================================")
                        print(info)
                        print("====================================================================================================\n")
                        
                        palabra_buscar = input("¿Qué palabra deseas cambiar del reporte militar?: ").strip()
                        palabra_nueva = input("¿Por qué nueva palabra o frase la vas a reemplazar?: ").strip()
                        
                        info_modificada = info.replace(palabra_buscar, palabra_nueva)
                        
                        fragmento = info_modificada[0:50]
                        
                        print("\n====================================================================================================")
                        print("REPORTE MODIFICADO EN TIEMPO REAL:")
                        print("====================================================================================================")
                        print(info_modificada)
                        print("====================================================================================================")
                        print(f"CÓDIGO DE ENCRIPTACIÓN MILITAR (Slicing [0:50]):\n-> {fragmento}...")   
                        print("====================================================================================================")
                        
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