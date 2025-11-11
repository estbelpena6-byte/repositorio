numeros = []

cantidad = int(input("¿cuantos numeros ganadores tiene la loteria?"))

for i in range(cantidad):
    numero = int(input(f"introduce el numero ganador #{i + 1}:"))
    numeros.append(numero)

numeros.sort()

print("\n los numeros ganadores ordenados son:")
print(numeros)