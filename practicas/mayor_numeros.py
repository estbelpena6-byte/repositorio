
num1 = int(input("agrega el primer numero:"))
num2 = int(input("agrega el segundo numero:"))
num3 = int(input("agrega el tercer numero:"))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1  and num2 >= num3: 
    mayor = num2
else:
    mayor = num3

print (f"el numero mayor es {mayor}")



