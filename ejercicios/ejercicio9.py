palabra = input("Escribe una palabra:")

palabra = palabra.lower()

vocales = ["a","e","i","o","u"]

for vocal in vocales:
    cantidad = palabra.count(vocal)
    print(f"la vocal {vocal} aparece {cantidad} veces")