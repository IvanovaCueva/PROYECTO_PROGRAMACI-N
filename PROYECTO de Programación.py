# PROYECTO DE PROGRAMACIÓN

usuarios = {
    "Dome": {"password": "1234", "rol": "E"},
    "Iva": {"password": "abcd", "rol": "E"},
    "Lilian": {"password": "admin", "rol": "D"},
}
plataforma = {
    "tareas": [],       
    "materiales": [],   
    "foro": []          
}

CATEGORIAS_MATERIAL = ("PDF", "PPT", "LINK", "VIDEO", "OTRO")

def pausar():
    input("\nPresione ENTER para continuar...")


def mostrar_tareas():
    if not plataforma["tareas"]:
        print("No hay tareas disponibles todavía.")
        return
    print("\n--- TAREAS DISPONIBLES ---")
    for i, t in enumerate(plataforma["tareas"], start=1):
        print(f"{i}. {t['titulo']} | Archivo: {t['archivo']} | Fecha: {t['fecha']} | Por: {t['subido_por']}")

def mostrar_material():
    if not plataforma["materiales"]:
        print("No hay material disponible todavía.")
        return
    print("\n--- MATERIAL DISPONIBLE ---")
    for i, m in enumerate(plataforma["materiales"], start=1):
        print(f"{i}. {m['titulo']} | Tipo: {m['tipo']} | Archivo/Link: {m['archivo']} | Por: {m['subido_por']}")

def publicar_foro(autor_id, rol):
    mensaje = input("Escriba su mensaje en el foro: ").strip()
    if mensaje == "":
        print("No se envió: el mensaje está vacío.")
        return
    plataforma["foro"].append((autor_id, rol, mensaje))
    print("Mensaje enviado.")

def ver_foro():
    if not plataforma["foro"]:
        print("El foro está vacío.")
        return
    print("\n--- FORO ---")
    for i, (autor, rol, msg) in enumerate(plataforma["foro"], start=1):
        print(f"{i}. [{rol}] {autor}: {msg}")

def subir_tarea(docente_id):
    titulo = input("Título de la tarea: ").strip()
    archivo = input("Nombre del archivo: ").strip()
    fecha = input("Fecha de entrega (ej: 2025-12-20): ").strip()

    if titulo == "" or archivo == "" or fecha == "":
        print("Error: Título/archivo/fecha no pueden estar vacíos.")
        return
    tarea = {
        "titulo": titulo,
        "archivo": archivo,
        "fecha": fecha,
        "subido_por": docente_id
    }
    plataforma["tareas"].append(tarea)
    print(f"Tarea '{titulo}' subida con éxito.")

def editar_tarea():
    mostrar_tareas()
    if not plataforma["tareas"]:
        return
    try:
        idx = int(input("Ingrese el número de la tarea a editar: ")) - 1
        if idx < 0 or idx >= len(plataforma["tareas"]):
            print("Número inválido.")
            return
    except ValueError:
        print("Debe ingresar un número.")
        return

    t = plataforma["tareas"][idx]
    print("Deje en blanco para mantener el valor actual.")

    nuevo_titulo = input(f"Nuevo título ({t['titulo']}): ").strip()
    nuevo_archivo = input(f"Nuevo archivo ({t['archivo']}): ").strip()
    nueva_fecha = input(f"Nueva fecha ({t['fecha']}): ").strip()

    if nuevo_titulo != "":
        t["titulo"] = nuevo_titulo
    if nuevo_archivo != "":
        t["archivo"] = nuevo_archivo
    if nueva_fecha != "":
        t["fecha"] = nueva_fecha

    print("Tarea actualizada.")

def eliminar_tarea():
    mostrar_tareas()
    if not plataforma["tareas"]:
        return
    try:
        idx = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if idx < 0 or idx >= len(plataforma["tareas"]):
            print("Número inválido.")
            return
    except ValueError:
        print("Debe ingresar un número.")
        return

    eliminada = plataforma["tareas"].pop(idx)
    print(f"Tarea '{eliminada['titulo']}' eliminada.")

def subir_material(docente_id):
    titulo = input("Título del material: ").strip()
    archivo = input("Archivo o link: ").strip()

    print("Tipo de material:", CATEGORIAS_MATERIAL)
    tipo = input("Ingrese tipo (PDF/PPT/LINK/VIDEO/OTRO): ").strip().upper()

    if titulo == "" or archivo == "":
        print("Error: Título/archivo no pueden estar vacíos.")
        return

    if tipo not in CATEGORIAS_MATERIAL:
        print("Tipo inválido. Se guardará como 'OTRO'.")
        tipo = "OTRO"

    material = {
        "titulo": titulo,
        "archivo": archivo,
        "tipo": tipo,
        "subido_por": docente_id
    }
    plataforma["materiales"].append(material)
    print(f"Material '{titulo}' subido con éxito.")

def editar_material():
    mostrar_material()
    if not plataforma["materiales"]:
        return
    try:
        idx = int(input("Ingrese el número del material a editar: ")) - 1
        if idx < 0 or idx >= len(plataforma["materiales"]):
            print("Número inválido.")
            return
    except ValueError:
        print("Debe ingresar un número.")
        return

    m = plataforma["materiales"][idx]
    print("Deje en blanco para mantener el valor actual.")

    nuevo_titulo = input(f"Nuevo título ({m['titulo']}): ").strip()
    nuevo_archivo = input(f"Nuevo archivo/link ({m['archivo']}): ").strip()
    nuevo_tipo = input(f"Nuevo tipo ({m['tipo']}): ").strip().upper()

    if nuevo_titulo != "":
        m["titulo"] = nuevo_titulo
    if nuevo_archivo != "":
        m["archivo"] = nuevo_archivo
    if nuevo_tipo != "":
        if nuevo_tipo in CATEGORIAS_MATERIAL:
            m["tipo"] = nuevo_tipo
        else:
            print("Tipo inválido: se mantiene el tipo actual.")

    print("Material actualizado.")

def eliminar_material():
    mostrar_material()
    if not plataforma["materiales"]:
        return

    try:
        idx = int(input("Ingrese el número del material a eliminar: ")) - 1
        if idx < 0 or idx >= len(plataforma["materiales"]):
            print("Número inválido.")
            return
    except ValueError:
        print("Debe ingresar un número.")
        return

    eliminado = plataforma["materiales"].pop(idx)
    print(f"Material '{eliminado['titulo']}' eliminado.")

def menu_estudiante(usuario_id, rol_visible):
    while True:
        print("\n--- MENÚ ESTUDIANTE ---")
        print("1. Ver Tareas")
        print("2. Ver Material")
        print("3. Foro (publicar)")
        print("4. Ver Foro")
        print("5. Volver")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            mostrar_tareas()
            pausar()
        elif opcion == "2":
            mostrar_material()
            pausar()
        elif opcion == "3":
            publicar_foro(usuario_id, rol_visible)
            pausar()
        elif opcion == "4":
            ver_foro()
            pausar()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            pausar()

def menu_docente(usuario_id):
    while True:
        print("\n--- MENÚ DOCENTE ---")
        print("1. Subir Tareas")
        print("2. Editar Tareas")
        print("3. Eliminar Tareas")
        print("4. Subir Material")
        print("5. Editar Material")
        print("6. Eliminar Material")
        print("7. Foro (publicar)")
        print("8. Ver Foro")
        print("9. Modo Estudiante (vista previa)")
        print("10. Volver")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            subir_tarea(usuario_id)
            pausar()
        elif opcion == "2":
            editar_tarea()
            pausar()
        elif opcion == "3":
            eliminar_tarea()
            pausar()
        elif opcion == "4":
            subir_material(usuario_id)
            pausar()
        elif opcion == "5":
            editar_material()
            pausar()
        elif opcion == "6":
            eliminar_material()
            pausar()
        elif opcion == "7":
            publicar_foro(usuario_id, "Docente")
            pausar()
        elif opcion == "8":
            ver_foro()
            pausar()
        elif opcion == "9":
            # VALIDACIÓN ADICIONAL: docente entra a la parte de estudiantes
            menu_estudiante(usuario_id, "Docente (vista estudiante)")
        elif opcion == "10":
            break
        else:
            print("Opción inválida.")
            pausar()

while True:
    usuario_id = input("Ingrese su ID: ").strip()

    if usuario_id not in usuarios:
        print("ID no registrado. Intente nuevamente.\n")
        continue

    password = input("Ingrese su contraseña: ").strip()

    if password != usuarios[usuario_id]["password"]:
        print("Contraseña incorrecta. Intente nuevamente.\n")
        continue

    usuario_tipo = usuarios[usuario_id]["rol"]  # "E" o "D"
    print(f"\nBienvenido/a, {'Estudiante' if usuario_tipo == 'E' else 'Docente'} {usuario_id}.")
    break

continuar_app = "SI"

while continuar_app.upper() == "SI":
    if usuario_tipo == "E":
        menu_estudiante(usuario_id, "Estudiante")
    else:
        menu_docente(usuario_id)

    continuar_app = input("\n¿Desea continuar en la aplicación? (SI/NO): ").strip()

print("Aplicación finalizada.")
