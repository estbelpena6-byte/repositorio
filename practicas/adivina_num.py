import random

min_numero = 1
max_numero = 10

numero_secreto = random.randint(min_numero, max_numero)

intentos = 0
adivinado = False

print(f"adivina el número, Está entre {min_numero} y {max_numero}")

while not adivinado:
    try:
        adivinanza = int(input("agrega el numero que crees que es:"))
        intentos += 1
    except ValueError:
        print("Error, ingrese el número de nuevo.")
        continue

    if adivinanza == numero_secreto:
        print(f"felicidades, adivinaste el número {numero_secreto} en")
        adivindado = True

    elif adivinanza < numero_secreto:
        print("el número secreto es mayor. intenta de nuevo")
    else:
        print("el numero secreto es menor. intentelo de nuevo")

print("\n--- fin del juego---")






