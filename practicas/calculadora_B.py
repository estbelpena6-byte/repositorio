


numero1 = float(input("agrega el primer número:"))
numero2 = float(input("agrega el segundo número:"))
operacion = input("elige una de estas operaciones (+, -, *, /)") 

if operacion == "+":
    print(f"la suma es {numero1 + numero2}")

elif operacion == "-":
    print(f"la resta es {numero1 - numero2}")

elif operacion == "*":
    print(f"la multiplicacion es {numero1 * numero2}")

elif operacion == "/":
    if numero2 != 0:
        print(f"la divicion es {numero1 / numero2}")
    else:
        print("no se puede dividir entre cero")

    

    
    