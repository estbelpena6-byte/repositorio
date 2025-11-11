abecedario = list("abcdefghijklmnñoprstuvwxyz")

resultado = []

for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])

print("letras restantes despues de eliminar letras en multiplo de 3")
print(resultado)