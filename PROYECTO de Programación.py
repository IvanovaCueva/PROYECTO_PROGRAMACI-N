# PROYECTO DE PROGRAMACIÓN

# BUCLE DE LOGIN
while True:
    usuario_tipo = input("¿Es estudiante o docente? (E/D): ").upper()
    if usuario_tipo not in ["E", "D"]:
        print("Opción inválida. Intente nuevamente.\n")
        continue

    usuario_id = input("Ingrese su ID: ")

    if usuario_id != "":
        print(f"Bienvenido, {'Estudiante' if usuario_tipo == 'E' else 'Docente'} {usuario_id}.\n")
        break
    else:
        print("ID no puede estar vacío. Intente nuevamente.\n")


continuar_app = "SI"

while continuar_app.upper() == "SI":

    # MENÚ PRINCIPAL
    print("\nMenú:")
    if usuario_tipo == "E":  # Menú para estudiantes
        print("1. Ver Tareas")
        print("2. Ver Material")
        print("3. Foro")
        print("4. Salir")
    else:  # Menú para docentes
        print("1. Subir Tareas")
        print("2. Subir Material")
        print("3. Foro (para responder)")
        print("4. Salir")

    opcion = input("Ingrese una opción: ")

    # Estudiante
    if usuario_tipo == "E":
        if opcion == "1":
            print("Mostrando Tareas disponibles...")
        elif opcion == "2":
            print("Mostrando Material de la materia...")
        elif opcion == "3":
            mensaje = input("Escriba su mensaje en el foro: ")
            print("Mensaje enviado.")
        elif opcion == "4":
            print("Aplicación cerrada, hasta pronto.")
            break
        else:
            print("Opción inválida.")

    # Docente
    else:
        if opcion == "1":
            archivo_tarea = input("Ingrese nombre del archivo de tarea a subir: ")
            print(f"Tarea '{archivo_tarea}' subida con éxito.")
        elif opcion == "2":
            archivo_material = input("Ingrese nombre del archivo de material a subir: ")
            print(f"Material '{archivo_material}' subido con éxito.")
        elif opcion == "3":
            mensaje = input("Escriba su mensaje en el foro: ")
            print("Mensaje enviado.")
        elif opcion == "4":
            print("Aplicación cerrada, hasta pronto.")
            break
        else:
            print("Opción inválida.")

    continuar_app = input("¿Desea continuar en la aplicación? (SI/NO): ")

print("Aplicación finalizada.")
