
contar = input("agrega una palabra:")
contar = contar.lower()
vocales = "aeiou"
contador_vocales = 0

for caracter in contar:
    if caracter in vocales:
        contador_vocales += 1

print("la cantidad de vocales:", contador_vocales)