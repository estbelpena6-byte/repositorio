palabra = input("Escribe una palabra:")

palabra = palabra.lower()

palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print("es palidromo")
else:
    print("no es palidromo")
