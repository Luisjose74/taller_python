#Operadores Aritmeticos
#Calculadora

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
tipo_de_operacion = input("Ingrese el tipo de operacion: ")

if tipo_de_operacion == "suma":
    print(f"El resultado de la suma es: {num1 + num2}")
elif tipo_de_operacion == "resta":
    print(f"El resultado de la resta es: {num1 - num2}")
elif tipo_de_operacion == "multiplicacion":
    print(f"El resultado de la multiplicacion es: {num1 * num2}")
elif tipo_de_operacion == "division":
    print(f"El resultado de la division es: {num1 / num2}")    
elif tipo_de_operacion == "modulo":
    print(f"El resultado del modulo es: {num1 % num2}")
elif tipo_de_operacion == "division_entera":
    print(f"El resultado de la division entera es: {num1 // num2}")
elif tipo_de_operacion == "exponente":
    print(f"El resultado del exponente es: {num1 ** num2}")     

else:
    print("Operacion no reconocida")
    exit()

print("Gracias por usar la calculadora")