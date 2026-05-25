# =================================================================
# Azeroth Admin - WoW Core Management
# OBJETIVO: Gestionar servidores MMORPG (World of Warcraft)
# =================================================================

reino_nombre = "Icecrown"
gm_nombre = "Desconocido"
gold_global = 1000000  # Stock total de oro del servidor
stats_personaje = 100   # Vida o Nivel base
lore_server = """Bienvenido al servidor privado de Icecrown. 
Aquí, los héroes se enfrentan al Rey Exánime por la gloria..."""

# 1. SEGURIDAD: PORTAL DE ACCESO
password_gm = "AZEROTH"
entrada = ""

print(">>> SISTEMA DE GESTIÓN GM - WORLD OF WARCRAFT <<<")
while entrada != password_gm:
    # .strip() para limpiar espacios y .upper() para estandarizar clave
    entrada = input("Introduce la Palabra de Poder (Password): ").strip().upper()
    if entrada != password_gm:
        print("Clave incorrecta. El acceso al servidor está bloqueado.\n")

print("\n¡Bienvenido, Game Master! Acceso al reino concedido.\n")

# 2. BUCLE PRINCIPAL (Menú Infinito)
while True:
    print("-" * 40)
    print(f" PANEL DE COMANDO - REINO: {reino_nombre.upper()} ")
    print("-" * 40)
    print("1. Registrar GM y Nombre de Servidor")
    print("2. Gestionar Economía (Suma/Resta de Gold)")
    print("3. Editar Lore y Títulos del Reino")
    print("4. Generar ID de Personaje (Slicing)")
    print("5. SALIR")
    
    opcion = input("\nElige una opción: ").strip()

    if opcion == "1":
        gm_nombre = input("Ingresa tu nombre de GM: ").strip().capitalize()
        nuevo_reino = input("Ingresa el nuevo nombre del servidor: ").strip()
        reino_nombre = nuevo_reino.lower().replace(" ", "_")
        print(f"\nServidor actualizado: {reino_nombre} | Administrado por: GM {gm_nombre}")

    elif opcion == "2":
    
        print(f"\nReserva de Gold actual: {gold_global}G")
        operacion = input("¿Deseas SUMAR oro o RESTAR oro? (sumar/restar): ").strip().lower()
        cantidad = int(input("Cantidad de oro a procesar: "))
        
        if operacion == "sumar":
            gold_global += cantidad
            print(f"¡Oro añadido! Nuevo total: {gold_global}G")
        elif operacion == "restar":
            if cantidad <= gold_global:
                gold_global -= cantidad
                print(f"Oro retirado. Nuevo total: {gold_global}G")
            else:
                print("Error: No hay suficiente oro en la reserva del reino.")

    elif opcion == "3":
    
        print("\n=== LORE ACTUAL DEL REINO ===")
        print(lore_server)
        cambio = input("\n¿Qué palabra quieres actualizar en el lore?: ")
        nueva_p = input("Ingresa la nueva palabra: ")
        lore_server = lore_server.replace(cambio, nueva_p.upper())
        print("\n¡Lore actualizado satisfactoriamente!")

    elif opcion == "4":
    
        char_name = input("Ingresa el nombre del personaje: ").strip()
        if len(char_name) >= 3:
    
            char_id = char_name[0:3].upper() + "-" + reino_nombre[0:3].upper()
            print(f"\nID de Personaje generado: {char_id}")
        else:
            print("\nNombre muy corto para generar ID.")

    elif opcion == "5" or opcion.lower() == "salir":
        print("\nCerrando Azeroth Admin... ¡Que la luz te acompañe!")
        break

    else:
        print("\nComando desconocido. Revisa el manual del Game Master.")
