# WORLD OF WARCRAFT
reino_nombre = "Icecrown"
password_gm = "AZEROTH"
entrada = ""

print(">>> SISTEMA DE GESTIÓN GM - WORLD OF WARCRAFT <<<")
print("Estado del Servidor: [PROTEGIDO]")
print("-" * 45)

while entrada != password_gm:
    # strip() elimina espacios accidentales
    # upper() convierte todo a mayúsculas para evitar errores de escritura
    entrada = input("Introduce la Palabra de Poder (Contraseña): ").strip().upper()
    
    if entrada == password_gm:
        print("\n" + "="*45)
        print("¡ACCESO CONCEDIDO, GAME MASTER!")
        print(f"Conectado al Reino: {reino_nombre}")
        print("="*45)
    else:
        print(">> CLAVE INCORRECTA. El acceso al servidor permanece sellado.")
        print("Pista: Es el nombre del mundo de WoW.\n")

print("\n[Cargando base de datos de personajes...]")
print("[Cargando logs de hermandades...]")
print("\nListo para recibir comandos.")