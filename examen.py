"""Crea un programa que muestre un menú para un restaurante con 10 productos. El programa debe capturar cada venta en una lista y al final mostrar las ventas por tipo de producto y el total de las ventas. Utiliza algunas funciones para capturar la información y listas para guardar los datos"""

menu =  [
    ("1. papitas", 25),
    ("2. pizza", 150),
    ("3. pica pollo", 100),
    ("4. refresco", 50),
    ("5. pollo al horno",250),
    ("6. yogurt",25),
    ("7. Empanadas",30),
    ("8. cafe",55),
    ("9. helado",20),
    ("10. batida", 60),
]

ventas = []


def mostrar_menu():
    print("\n----- MENÚ DEL RESTAURANTE -----")
    for producto, precio in menu:
        print(f"{producto} - RD{precio}")
        print("0. Salir y ver reporte")
    print("------------------------------")

def registrar_ventas(opcion):
    indice = opcion - 1
    producto = menu[indice][0]
    precio = menu[indice][1]
    ventas.append(precio)
    print(f"ventas registradas {producto} (RD{precio})")

mostrar_menu()

continuar = True
while continuar:
    
    
    opcion = int(input("Seleccione un producto (0 para salir): "))

    if opcion == 0:
        continuar = False
        print("\nSaliendo del sistema...\n")

    elif opcion >= 1 and opcion <= 10:
        registrar_ventas(opcion)

    else:
        print(" fuera de rango, intente de nuevo.")

print("========= REPORTE DE VENTAS =========")


totales_por_producto = [0] * 10  

for precio in ventas:
    for i in range(10):
        if precio == menu[i][1]:
            totales_por_producto[i] += 1

total_general = 0

for i in range(10):
    producto, precio = menu[i]
    cantidad = totales_por_producto[i]
    total_producto = cantidad * precio
    total_general += total_producto

    print(f"{producto}: {cantidad} ventas - RD${total_producto}")