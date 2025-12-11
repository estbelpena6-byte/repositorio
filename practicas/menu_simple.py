def opcion_1():
    print("haz elegido la opcion uno, suma")

def opcion_2():
    print("haz elegido la opcion dos, resta")

while True:
    print("---menu_principal---")
    print("1. suma")
    print("2. resta")
    print("3. salir")
             
    eleccion = input("ingresa tu elección (1, 2 o 3):")

    if eleccion == "1":
        opcion_1()
    elif eleccion == "2":
        opcion_2()
    elif eleccion == "3":
        print("saliste del programa")
        break

    else:
        print("opción inválida, por favor elige una opción del menú")