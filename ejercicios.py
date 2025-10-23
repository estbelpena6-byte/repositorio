
# ESTBEL ELIOENAI PEÑA CALSINO  / MATRICULA: 2025-0343

########################################################################

# 1. Número positivo, negativo o cero Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero

########################################################################

num = int(input("ingresa un numero:"))

if num > 0:
    print("es positivo")
elif num < 0:
    print("es negativo")

else:
    print("es cero")

#######################################################################################################################

# 2. Número par o impar, Pide al usuario que ingrese un número entero y determina si es par o impar.

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

# 3. Mayor de edad, Solicita la edad de una persona e imprime si es mayor o menor de edad (mayor de 18 años).

#========================================================================================================================

Edad = int(input("Agrega tu edad:"))

if Edad >= 18:
    print("Eres mayor de Edad")
else:
    print("no eres mayor de Edad")

#=========================================================================================================================

# 4. Múltiplo de 5, Escribe un programa que pida un número y determine si es múltiplo de 5.

#=========================================================================================================================

num = int(input("ingrese el numero:"))

if num % 5 == 0:
    print("El numero", num, "es multiplo de 5")
else:
    print("este es numero no multiplo de 5")

#=========================================================================================================================

# 5. Descuento por edad Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la edad del usuario y determina si aplica para el descuento.

#=========================================================================================================================

Edad = int(input("agrega la Edad:"))

if Edad >= 60:
    print("Aplicas para el descuento para el 50%")
else:
    print("No aplicas para el 50%")

#=========================================================================================================================

# 6. Calificación aprobatoria Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó

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

# 7 .Día de la semana, Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente    (1 es lunes, 7 es domingo).

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

# 8. Número mayor entre dos, Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.

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

# 9. Mayor entre tres números Pide al usuario tres números y muestra el mayor de ellos.

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

# 10. Clasificación de ángulos, Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).

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

# 11. Cálculo de impuestos

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

# 12. Clasificación de números, Pide al usuario tres números y determina si son todos positivos, todos negativos, mixtos o si hay ceros.

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

#============================================================================================================================

# 13. Verificación de año bisiesto, Solicita al usuario un año y determina si es bisiesto o no. (Es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por 400).

#============================================================================================================================

año = int(input("ingrese un año:"))

if (año % 4 == 0 and año % 100 !=0) or (año % 400 == 0):
    print("El año es", año, "bisiesto.")

else:
    print("El año no es", año, "bisiesto.")

#============================================================================================================================

# 14. Conversión de calificaciones
#Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
#○ 90-100: A
#○ 80-89: B
#○ 70-79: C
#○ 60-69: D
#○ 0-59: F

#============================================================================================================================

nota = int(input("ingresa tu calificación"))

if nota < 0 or nota > 100:
    print("Calificación fuera de rango. Debe estar entre 0 y 100.")
elif nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

#============================================================================================================================

# 15. Comparación de tres longitudes, Solicita tres números que representan longitudes y determina si pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).

#============================================================================================================================

lado1 = float(input("ingresa la primera longitud:"))
lado2 = float(input("ingresa la segunda longitud:"))
lado3 = float(input("ingresa la tercera longitud:"))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado3):
    print("Las lonfitudes pueden formar un triangulo")

else:
    print("las longitudes no pueden formar un triangulo")

#============================================================================================================================

# 16. . Calculadora de descuentos
#Solicita el precio de un producto y aplica descuentos según el monto:
#○ Menos de $50: sin descuento
#○ Entre $50 y $100: 5%
#○ Más de $100: 10%

#============================================================================================================================

precio = float(input("ingrese el precio del producto:"))

if precio < 50:
    descuento = 0

elif precio <= 100:
    descuento = 0.5

else:
    descuento = 0.10

monto_descuento = precio * descuento
precio_final = precio - monto_descuento

print(f"\nDescuento aplicado: {descuento * 100}%")
print(f"Monto del descuento: ${monto_descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")

#============================================================================================================================

# 17. Tipo de triángulo, Pide tres longitudes y determina si el triángulo es equilátero, isósceles o escaleno

#============================================================================================================================

lado1 = float(input("ingresa una primera longitud:"))
lado2 = float(input("ingresa una segunda longitud:"))
lado3 = float(input("ingresa una tercera longitud:"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    
    if lado1 == lado2 == lado3:
        print("es un triangulo equilátero.")
    
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triangulo es isóceles.")

    else:
        print("El triangulo es escaleno.")

else:
    print("las longitudes ingresadas no pueden formar un triangulo.")

#============================================================================================================================

# 18. Evaluación de temperatura
#Solicita la temperatura en grados Celsius e imprime un mensaje dependiendo del
#valor:
#○ Menos de 0°C: “Hace mucho frío”
#○ Entre 0°C y 20°C: “Clima fresco”
#○ Entre 21°C y 30°C: “Clima agradable”
#○ Más de 30°C: “Hace mucho calor”

#============================================================================================================================

temperatura = float(input("ingrese la temperatura en grados celcius:"))


if temperatura < 0:
    print("hace mucho frio")

elif temperatura <= 20:
    print("clima fresco.")

elif 21 <= temperatura <= 30:
    print("clima agradable")

else:
    print("hace mucho calor")

#===========================================================================================================================

# 19. Conversión de horas a turnos, Pide la hora (0-23) y determina si es "Mañana" (6-11), "Tarde" (12-17), "Noche" (18-23) o "Madrugada" (0-5).

#===========================================================================================================================

hora = int(input("ingrese la hora(0 - 23):"))

if 6 <= hora <= 11:
    print("Es mañana")

elif 12 <= hora <= 17:
    print("Es tarde")

elif 18 <= hora <= 23:
    print("Es noche.")

elif 0 <= hora <= 5:
    print("Es madrugada")

else:
    print("Hora no válida. Debe estar entre 0 y 23")

#============================================================================================================================

#20. Clasificación de IMC
#Solicita el peso (kg) y la altura (m) de una persona, calcula su Índice de Masa
#Corporal (IMC = peso / altura²) y clasifícalo:
#○ <18.5: Bajo peso
#○ 18.5-24.9: Normal
#○ 25-29.9: Sobrepeso
#○ 30 o más: Obesidad

#============================================================================================================================

peso = float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altuara:"))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")


# fin de todos los codigos.