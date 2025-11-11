

texto = input("Escribe varios números separados por comas: ")


numeros = [float(x) for x in texto.split(",")]


suma = sum(numeros)
cantidad = len(numeros)
media = suma / cantidad

diferencias = 0
for n in numeros:
    diferencias += (n - media) ** 2

desviacion = (diferencias / cantidad) ** 0.5

print(f"Los números que escribiste fueron: {numeros}")
print(f"La media es:{media}")
print(f"La desviación típica es: {desviacion}")