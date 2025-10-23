
# ESTBEL ELIOENAI PEÑA CALSINO  / MATRICULA: 2025-0343

########################################################################

# Número positivo, negativo o cero Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero

########################################################################

num = int(input("ingresa un numero:"))

if num > 0:
    print("es positivo")
elif num < 0:
    print("es negativo")

else:
    print("es cero")

#######################################################################################################################

# Número par o impar, Pide al usuario que ingrese un número entero y determina si es par o impar.

#######################################################################################################################

while True:
    inicio = int(input("ingrese un número entero:"))
    if inicio >= 0:
        num = int(inicio)
        break
    else:
        print("numero inválido, intentelo de nuevo")

if num % 2 == 0:
    print("es par")
else:
    print("es impar")

#========================================================================================================================

# Mayor de edad, Solicita la edad de una persona e imprime si es mayor o menor de edad (mayor de 18 años).

#========================================================================================================================

Edad = int(input("Agrega tu edad:"))

if Edad >= 18:
    print("Eres mayor de Edad")
else:
    print("no eres mayor de Edad")

#=========================================================================================================================

#Múltiplo de 5, Escribe un programa que pida un número y determine si es múltiplo de 5.

#=========================================================================================================================

num = int(input("ingrese el numero:"))

if num % 5 == 0:
    print("El numero", num, "es multiplo de 5")
else:
    print("este es numero no multiplo de 5")

#=========================================================================================================================

# Descuento por edad Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la edad del usuario y determina si aplica para el descuento.

#=========================================================================================================================

Edad = int(input("agrega la Edad:"))

if Edad >= 60:
    print("Aplicas para el descuento para el 50%")
else:
    print("No aplicas para el 50%")

#=========================================================================================================================

#Calificación aprobatoria Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó

#=========================================================================================================================

calificación = int(input("ingresa la calificación:"))

if calificación == 100:
    print(calificación, "Felicidades, Maxima calificación")

elif calificación >= 90:
    print(calificación, "Sobresaliente")

elif calificación >= 80:
    print(calificación, "Excelente")

elif calificación >= 70:
    print(calificación, "Buen rendimiento")

elif calificación >= 60:
    print(calificación, "Mejora necesaria")

else:
    print( calificación, "Estas reprobado, intentalo para la proxima")

#============================================================================================================================

# Día de la semana, Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente    (1 es lunes, 7 es domingo).

#============================================================================================================================

Día = int(input("ingrese un numero del (1-7):"))

if Día == 1:
    print(" Día", Día, "lunes")
elif Día == 2:
    print("Día", Día, "martes")
elif Día == 3:
    print("Día", Día, "miercoles")
elif Día == 4:
    print("Día", Día, "jueves")
elif Día == 5:
    print("Día", Día, "viernes")
elif Día == 6:
    print("Día", Día, "sábado")
elif Día == 7:
    print("Día", Día, "domingo")

#============================================================================================================================

#Número mayor entre dos, Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.

#============================================================================================================================

num1 = int(input("ingresa el primer numero:"))
num2 = int(input("ingresa el segundo numero:"))

if num1 > num2:
    print(num1, "es mayor")

elif num1 < num2:
    print(num1, "es menor")

else:
    print(num1, "y", num2, "son iguales" )

#============================================================================================================================

# Mayor entre tres números Pide al usuario tres números y muestra el mayor de ellos.

#============================================================================================================================

def El_mayor_de_3_números():
    print("El mayor de 3 números")

num1 = int(input("agrega el primer número:"))
num2 = int(input("agrega el segundo número:"))
num3 = int(input("agrega el tercero número:"))

if num1 >= num2 and num1 >= num3:
    mayor = num1 
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"el numero mayor es: {mayor}")

El_mayor_de_3_números()

#============================================================================================================================

# Clasificación de ángulos, Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).

#============================================================================================================================

angulo = float(input("Agrega el angulo en grados:"))

if angulo < 90:
    print("el angulo es agudo.")

elif angulo == 90:
    print("el angulo es recto.")

elif angulo > 90 and  angulo < 180:
    print("es un angulo obtuso")

elif angulo == 180:
    print("es un angulo llano")

else:
    print("El angulo no entra en ninguna de estas categorias (es mayor a 180°)")

#============================================================================================================================

# . Cálculo de impuestos

#Pide al usuario su salario mensual y aplica los siguientes impuestos:
#○ Menos de 10,000: 0%
#○ Entre 10,000 y 30,000: 10%
#○ Más de 30,000: 20%

#============================================================================================================================

salario = float(input("ingresa tu salario:"))

if salario < 10000:
    impuesto = 0

elif salario <= 30000:
    impuesto = salario * 0.10

else:
    impuesto = salario * 0.20

print("tu salario es:", salario, "pesos.")
print("tu impuesto a pagar", impuesto, "pesos.")

#============================================================================================================================

# Clasificación de números, Pide al usuario tres números y determina si son todos positivos, todos negativos, mixtos o si hay ceros.

#============================================================================================================================

num1 = int(input("agrega el primer número:"))
num2 = int(input("agrega el segundo número:"))
num3 = int(input("agrega el tercer número:"))

if num1 == 0 or num2 == 0 or num3 == 0:
    print("hay al menos un numero igual a cero")

elif num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos los números positivos")

elif num1 < 0 and num2 < 0 and num3 < 0:
    print("Todos los números son negativos")

else:
    print("Los números son mixtos (positivos y negativos)")

