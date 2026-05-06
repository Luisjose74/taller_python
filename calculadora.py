#Operadores Aritmeticos
#Calculadora

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
tipo_de_operacion = input("Ingrese el tipo de operacion: " \
"1) suma " \
"2) resta 3) " \
"3) multiplicacion " \
"4) division " \
"5) modulo " \
"6) division_entera " \
"7) exponente: ")

if tipo_de_operacion == "1":
    suma = num1+num2
    print(f"El resultado de la suma es: {num1} + {num2} = {suma}")
elif tipo_de_operacion == "2":
    resta = num1 - num2
    print(f"El resultado de la resta es: {num1} - {num2} = {resta}")
elif tipo_de_operacion == "3":
    multiplicacion = num1 * num2
    print(f"El resultado de la multiplicacion es: {num1} * {num2} = {multiplicacion}")
elif tipo_de_operacion == "4": 
    if num2 == 0:
        print("Error: No se puede dividir por cero")
    else:
        division = num1 / num2
        print(f"El resultado de la division es: {num1} / {num2} = {division}")  
elif tipo_de_operacion == "5":
    modulo = num1 % num2    
    print(f"El resultado del modulo es: {num1} % {num2} = {modulo}")
elif tipo_de_operacion == "6":
    division_entera = num1 // num2
    print(f"El resultado de la division entera es: {num1} // {num2} = {division_entera}")
elif tipo_de_operacion == "7":
    exponente = num1 ** num2
    print(f"El resultado del exponente es: {num1} ** {num2} = {exponente}")  

else:
    print("Operacion no reconocida")
    exit()

print("Gracias por usar la calculadora")