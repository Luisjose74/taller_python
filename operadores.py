#Operadores Aritmeticos


a = 20
b = 10

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
division_entera = a // b
exponente = a ** b

print(f"Suma: {suma}")

#Calculadora

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
tipo_de_operacion = input("Ingrese el tipo de operacion: ")

if tipo_de_operacion == "suma":
    print(f"El resultado de la suma es: {suma}")
elif tipo_de_operacion == "resta":
    print(f"El resultado de la resta es: {resta}")
elif tipo_de_operacion == "multiplicacion":
    print(f"El resultado de la multiplicacion es: {multiplicacion}")
elif tipo_de_operacion == "division":
    print(f"El resultado de la division es: {division}")    
elif tipo_de_operacion == "modulo":
    print(f"El resultado del modulo es: {modulo}")
elif tipo_de_operacion == "division_entera":
    print(f"El resultado de la division entera es: {division_entera}")
elif tipo_de_operacion == "exponente":
    print(f"El resultado del exponente es: {exponente}")     

else:
    print("Operacion no reconocida")
    exit()

print("Gracias por usar la calculadora")