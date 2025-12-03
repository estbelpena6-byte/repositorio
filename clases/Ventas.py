ventas = []
msg = "Programa para capturar cantidad de ventas"
print("Registro de ventas:\n")

numero_ventas = int(input("ingrese el numero de ventas a registrar: \n"))

for i in range(numero_ventas):
    print(f'venta{ i +1}')
    Articulo = input("ingrese el nombre del articulo: \n")
    precio= float(input("ingrese el precio: \n"))   
    ventas.append({"Articulo": Articulo, "Precio": precio})

precio_total = 0
for venta in ventas:
    print(f"venta \n")
    print(f"Articulo: {venta['Articulo']} \n")
    print(f"precio: {venta['Precio']} \n")

    precio_total += venta['Precio']
def entradaDatos(txt,tipo):
    """
    Devuelve la @entrada en el formato escogido (S: string, B: booleano, E: entero)

    Parameters
    ----------
    entrada : string
        el texto a devolver
    tipo : string
        el tipo de dato que quieres devolver (S: string, B: booleano, E: entero)

    Returns
    -------
    indefinido
        Segun el tipo de dato retorna string, boolean o entero
    """

    if str.upper(tipo) == 'S':
        return txt 
    elif str.upper(tipo) == 'B':
        return bool(txt)
    elif str.upper(tipo) == 'E':
        if txt.isdigit():
            return int(txt)
        else:
            return "Error"    


print(f"el total es {precio_total}")