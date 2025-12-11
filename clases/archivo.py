
import os

def crear_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe.")
    else:
        with open(nombre_archivo, "w") as file:
            file.write("")  
        print("Archivo creado correctamente.")

def guardar_registros(nombre_archivo):
    nombre = input("Ingrese el nombre: ")
    matricula = input("Ingrese la matrícula: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")

    with open(nombre_archivo, "a") as file:
        file.write(f"NOMBRE: {nombre}\n")
        file.write(f"MATRICULA: {matricula}\n")
        file.write(f"CORREO: {correo}\n")
        file.write(f"TELEFONO: {telefono}\n")
        file.write("---------------\n")

    print("Registros guardados correctamente.")

def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("El archivo no existe.")
        return
    
    with open(nombre_archivo, "r") as file:
        print("\n--- CONTENIDO DEL ARCHIVO ---")
        print(file.read())

def actualizar_nombre(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("El archivo no existe.")
        return

    nombre_actual = input("Escriba el nombre que desea buscar: ")
    nuevo_nombre = input("Escriba el nuevo nombre: ")

    with open(nombre_archivo, "r") as file:
        contenido = file.read()

    if nombre_actual in contenido:
        contenido = contenido.replace(f"NOMBRE: {nombre_actual}", f"NOMBRE: {nuevo_nombre}")
        with open(nombre_archivo, "w") as file:
            file.write(contenido)
        print("Nombre actualizado correctamente.")
    else:
        print("El nombre no fue encontrado.")

def menu():
    nombre_archivo = "registros.txt"

    while True:
        print("\n--- MENÚ ---")
        print("1. Crear archivo")
        print("2. Guardar registros")
        print("3. Leer archivo")
        print("4. Actualizar nombre")
        print("5. Cerrar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_archivo(nombre_archivo)
        elif opcion == "2":
            guardar_registros(nombre_archivo)
        elif opcion == "3":
            leer_archivo(nombre_archivo)
        elif opcion == "4":
            actualizar_nombre(nombre_archivo)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
