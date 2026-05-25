# =================================================================
# Azeroth Admin - WoW Core Management
# TEMA: Gestión de sistemas de videojuegos MMORPG (WOW)
# =================================================================

## 1. CONFIGURACIÓN INICIAL (Variables y Tipos de Datos)
nombre_reino = "Icecrown"
gm_actual = "Desconocido"
oro_reserva = 1000000
jugadores_online = 450
servidor_activo = True

## Requisito: Uso de Comillas Triples para bloques de texto largo (Lore)
lore_servidor = """
En el gélido trono de Rasganorte, el Rey Exánime observa.
Este sistema gestiona los recursos de la Alianza y la Horda 
para mantener el equilibrio en el servidor privado de Icecrown.
"""

## 2. SEGURIDAD: ACCESO AL NÚCLEO (Requisito: Bucle while)
clave_seguridad = "FOR_THE_HORDE"
intento_acceso = ""

print(">>> INICIANDO PROTOCOLO DE ADMINISTRACIÓN AZEROTH <<<")
print("-" * 55)

# Bucle de bloqueo: no permite pasar hasta que la clave sea exacta
while intento_acceso != clave_seguridad:
    # Requisito: .strip() quita espacios y .upper() normaliza a mayúsculas
    intento_acceso = input("Introduce la Palabra de Poder (Contraseña): ").strip().upper()
    
    if intento_acceso != clave_seguridad:
        print(">> ACCESO DENEGADO: El código es incorrecto. El servidor está protegido.\n")

print("\n" + "="*55)
print(f"¡BIENVENIDO GM! ACCESO CONCEDIDO AL REINO: {nombre_reino.upper()}")
print("="*55 + "\n")


## 3. MENÚ PRINCIPAL INTERACTIVO (Requisito: Bucle while True)
while True:
    print("-" * 45)
    print(f" INTERFAZ GM | Usuario: {gm_actual} | Oro Reino: {oro_reserva}G")
    print("-" * 45)
    print("1. Perfil: Identificarse como Game Master")
    print("2. Economía: Ajustar Oro (Sumar/Restar)")
    print("3. Lore: Modificar historia del servidor (Replace)")
    print("4. Seguridad: Generar Token de Personaje (Slicing)")
    print("5. SALIR")
    
    ## Requisito: Limpieza de la opción ingresada
    opcion = input("\nSelecciona un comando de comando: ").strip()

    ## OPCIÓN 1: MANIPULACIÓN DE TEXTO BÁSICA
    if opcion == "1":
        nuevo_gm = input("Ingresa tu nombre de Game Master: ").strip()
        # .capitalize() asegura que el nombre empiece con mayúscula
        gm_actual = nuevo_gm.capitalize()
        print(f"\n[SISTEMA]: Administrador registrado como: GM {gm_actual}")

    ## OPCIÓN 2: LÓGICA MATEMÁTICA (Requisito: Sumar/Restar)
    elif opcion == "2":
        print(f"\nReserva actual del servidor: {oro_reserva}G")
        accion = input("¿Deseas (S)umar o (R)estar oro?: ").strip().upper()
        
        try:
            cantidad = int(input("Ingresa la cantidad de oro: "))
            
            if accion == "S":
                oro_reserva = oro_reserva + cantidad  # Suma
                print(f"¡Éxito! Nueva reserva: {oro_reserva}G")
            elif accion == "R":
                if cantidad <= oro_reserva:
                    oro_reserva = oro_reserva - cantidad  # Resta
                    print(f"¡Éxito! Nueva reserva: {oro_reserva}G")
                else:
                    print("Error: No puedes retirar más oro del disponible.")
            else:
                print("Acción no válida (Usa S o R).")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    ## OPCIÓN 3: MANIPULACIÓN DE TEXTO (Requisito: .replace())
    elif opcion == "3":
        print("\n--- LORE ACTUAL DEL REINO ---")
        print(lore_servidor)
        cambiar = input("\nPalabra que deseas reemplazar: ")
        nuevo_texto = input("Nueva palabra: ")
        # Requisito: Uso de .replace() para actualizar el texto
        lore_servidor = lore_servidor.replace(cambiar, nuevo_texto.upper())
        print("\n[!] El Lore del reino ha sido actualizado.")

    ## OPCIÓN 4: MANIPULACIÓN DE TEXTO (Requisito: Slicing)
    elif opcion == "4":
        nombre_pj = input("Nombre del héroe para el token: ").strip()
        if len(nombre_pj) >= 3:
            # Requisito: Slicing (Extrae las primeras 3 letras del nombre)
            prefijo = nombre_pj[0:3].upper()
            token = prefijo + "-WOW-" + str(jugadores_online)
            print(f"\n[SISTEMA]: Token de seguridad generado: {token}")
        else:
            print("\nError: El nombre debe tener al menos 3 caracteres.")

    ## OPCIÓN 5: SALIDA DEL PROGRAMA (Requisito: break)
    elif opcion == "5" or opcion.lower() == "salir":
        print(f"\nCerrando Azeroth Admin... Guardando cambios en {nombre_reino}.")
        print("¡Que la luz te acompañe, Game Master!")
        break # Detiene el bucle infinito y cierra el programa

    ## CONTROL DE ERRORES
    else:
        print("\n[!] Comando inválido. Revisa las opciones del menú.")