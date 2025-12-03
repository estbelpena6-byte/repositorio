"""Realiza los siguientes ejercicios con estructuras repetitivas"""

#ESTBEL ELIOENAI PEÑA CALSINO  2025-0343


# 1. Escribe un programa que pida al usuario que ingrese un número entero positivo. El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.


def numeros_repetidos_positivos():

   num = int(input("ingresa un numero entero positivo:"))

   if num > 0:
        contador = 1
        while contador <= num:
            print (contador)
            contador += 1

   else:
        print("El número ingresado no es positivo.") 

numeros_repetidos_positivos()         
print ("fin.")

# 2. Escribe un programa que imprima los números pares entre 1 y 20 (inclusive) utilizando un bucle for.
 
def numeros_pares():
    for numero in range (1,21):
        if numero % 2 == 0:
            print(numero)
numeros_pares()
print("fin.")

# 3. Escribe un programa que pida al usuario un número entero positivo. El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.

def cantidad_de_digitos():
    num = int(input("ingresa un numero positivo:"))
    if num > 0:
        contador = 0
        while num > 0:
            num //= 10
            contador += 1
        print("El numero tiene", contador, "digitos.")
    else:
        print("el numero no es positivo")

cantidad_de_digitos()
print("fin.")

# 4. Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for.

def suma_de_los_numeros_enteros():
    suma = 0

    for numero in range(1,101):
        suma += numero 
        print("La suma de los numeros del 1 al 100 es:", suma)

suma_de_los_numeros_enteros()

#  5. Escribe un programa que pida al usuario un número entero y luego imprima todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.

def numeros_en_orden_decendente():
    num = int(input("ingresa un numero entero:"))

    while num >= 0:
        print(num)
        num -= 1

numeros_en_orden_decendente()
print("fin.")

# 6. Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for

def tabla_de_multiplicar():
    num = int(input("ingresa el numero que quiere multiplicar:"))

    print(f"Tabla de multiplicar del {num}:")
    for i in range(1,11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
tabla_de_multiplicar()

# 7. Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.

def numeros_impares():
    num = int(input("ingrese un numero positivo:"))

    if num > 0:
        contador = 1
        while contador <= num:
            if contador % 2 != 0:
                print(contador)
            contador += 1
    
    else:
        print("El numero no es positivo.")

numeros_impares()

# 8. Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.

def serie_fibonacci():
    n = int(input("ingresa el numero de la serie fibonacci:"))

    if n <= 0:
        print("por favor ingresa un numero positivo:")

    else:
        a, b = 0, 1
        print("serie de fibonacci")
        for i in range(n):
            print(a)
            a, b = b, a + b
serie_fibonacci()

#  9. Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.

def factorial():
    num = int(input("ingresa un numero entero positivo:"))

    if num < 0:
        print("El numero no puede ser negativo")
    else:
        resultado = 1
        contador = 1

        while contador <= num:
            resultado *= contador 
            contador += 1
            print("El factorial de", num, "es", resultado)
factorial()

# 10. Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura while para simular un do while.

def verificar_contraseña(): 
    
    contraseña_correcta = 859063
    while True:
        contraseña =int(input("ingresa la contraseña:"))
        if contraseña == contraseña_correcta:
            print("contraseña valida, acceso permitido")
            break
        else:
            print("la contraseña inválida, intentalo de nuevo")

verificar_contraseña()


# estos son mis diez códigos. 