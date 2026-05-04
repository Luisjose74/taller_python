#Operadores Aritmeticos

a = 5
b = 10

#Suma
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")
#Resta
resta = a - b
print(f"La resta de {a} y {b} es: {resta}")
#Multiplicacion
multiplicacion = a * b
print(f"La multiplicacion de {a} y {b} es: {multiplicacion}")
#Division flotante o decimal
division = a / b
print(f"La division de {a} y {b} es: {division}")
#Modulo
modulo = a % b
print(f"El modulo de {a} y {b} es: {modulo}")
#Division Entera (quita los decimales)
division_entera = a // b
print(f"La division entera de {a} y {b} es: {division_entera}")
#Exponente
exponente = a ** b
print(f"El exponente de {a} y {b} es: {exponente}")
#Precedencia de los operadores
resultado = a + b * 2 #El resultado de la multiplicacion se realiza primero 10 * 2 = 20 + 5 = 25    
print(f"El resultado de {a} + {b} * 2 es: {resultado}")
resultado2_con_parentesis = (a + b) * 2  #El resultado de la multiplicacion se realiza primero 15 * 2 = 30
print(f"El resultado de ({a} + {b}) * 2 es: {resultado2_con_parentesis}")
resultado3_con_parentesis = a * b // 3 #El resultado de la multiplicacion se realiza primero 50 // 3 = 16.666 = 16
print(f"El resultado de {a} * {b} // 3 es: {resultado3_con_parentesis}")
resultado4_con_parentesis = (a * b ) // 3 #El resultado de la division entera de 50 * 3 = 150 // 3
print(f"El resultado de ({a} * {b} ) // 3 es: {resultado4_con_parentesis}")
resultado5_con_parentesis = a * (b // 3) #El resultado de la division entera de 10 // 3 = 3 * 5 = 15
print(f"El resultado de {a} * ({b} // 3) es: {resultado5_con_parentesis}")
ejericicio = (a + b) * (a - b) / (a * b)  - ((a ** b) % 3)  #El resultado de la suma se realiza primero 15 * -5 / 50 = -75 / 50 = -1.5
# ejercicio = ((5 + 10) * (5 - 10)) / (5 * 10) - ((5 ** 10) % 3)
# ejercicio = (15 * -5) / 50 - ((9765625) % 3)
# ejercicio = -75 / 50 - (1)
# ejercicio = -1.5 - 1
# ejercicio = -2.5
print(f"El resultado de la operacion es: ({a} + {b}) * ({a} - {b}) / ({a} * {b})  - (({a} ** {b}) % 3) es: {ejericicio}")
# Librerias de Matematicas
import math
print(math.pi)# Numero Pi
print(math.e) # Numero de Euler
print(math.sqrt(16)) # para calcular la raiz cuadrada de un numero
# ramdom
import random #Libreria para generar numeros aleatorios
random.random()
numero_aleatorio = random.randint(1, 100) #Genera un numero aleatorio entre 1 y 100
print (numero_aleatorio)

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