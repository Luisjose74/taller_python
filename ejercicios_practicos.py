import math

#Ejercicio 1:

from tkinter import N


Nombre = "Jorge"
producto =20000
promedio_asignatura = 4.5
print(f"Mi Nombre es: {Nombre}" f"y he comprado un producto que cuesta: {producto} y mi promedio en la asignatura es: {promedio_asignatura}")

#Ejercicio 2:
variable_1_entera = 10
variable_2_entera = 5
Variable_float = 3.14
variable_1_string = "Hola"
variable_2_string = "Mundo"

suma_numeros= variable_1_entera + variable_2_entera + Variable_float
print(f"La suma de los numeros es: {suma_numeros}")

#Ejercicio 3:
base = 5
exponente = 3
resultado =base**exponente
print(f"{base} elevado a la potencia de {exponente} es igual a: {resultado}")

#Ejercicio 4:
Numero1 = input ("Ingrese el numero para calcular su raiz cuadrada: ")
Raiz_cuadrada = float(Numero1) ** 0.5
print(f"La raiz cuadrada de {Numero1} es: {Raiz_cuadrada}")

#Ejercicio 5 Variable Estudiante (Notas Decimales, Promedio)
# nombre_estudiante = input("Introduce el nombre del estudiante: ")
# nota1 = float(input("Introduce la nota 1: "))
# nota2 = float(input("Introduce la nota 2: "))
# nota3 = float(input("Introduce la nota 3: "))
# nota4 = float(input("Introduce la nota 4: "))
# nota5 = float(input("Introduce la nota 5: "))
# calcular_promedio = nota1+nota2+nota3+nota4+nota5
# promedio = calcular_promedio/5
# print("El promedio es:", promedio)

#Ejercicio 6 (Intercambio valores variables con variable auxiliar)
# valor_1 = int(input("Introduce el valor 1: "))
# valor_2 = int(input("Introduce el valor 2: "))
# #Intercambio
# valor_1, valor_2 = valor_2, valor_1
# #Imprimir los valores
# print("El valor 1 es:", valor_1)
# print("El valor 2 es:", valor_2)

# Ejercicio 7 (Variable “Booleana” llamada Estado)
#para determinar si un valor es faso o verdadero
# estado = (input (5==2) is false)
# print("El valor es:", estado)
# estado = (input (2>1) is true)
# print("El valor es:", estado)

#Ejercicio 8 (Variable “Resultado” operaciones aritméticas).
#Crear una variable llamada “Resultado”.
# resultado = int(input("Introduce el valor 1: ")) + int(input("Introduce el valor 2: "))
# print("El resultado es:", resultado)
# #Dentro de la variable “Resultado”, crear una operación aritmética en repetidas ocasiones
# resultado = int(input("Introduce el valor 1: ")) * int(input("Introduce el valor 2: "))
# print("El resultado es:", resultado)
# resultado = int(input("Introduce el valor 1: ")) / int(input("Introduce el valor 2: "))
# print("El resultado es:", resultado)
# resultado = int(input("Introduce el valor 1: ")) - int(input("Introduce el valor 2: "))
# print("El resultado es:", resultado)
# resultado = int(input("Introduce el valor 1: ")) % int(input("Introduce el valor 2: "))
# print("El resultado es:", resultado)

#Ejercicio 9 (Variable “lado_Cuadrado”, “Base_ Traingulo”, “Altura_Triangulo”.
# #Crear una variable entera llamada “ladoCuadrado” de valor 8 y calcular el área y elperímetro del cuadrado a partir de la variable anteriormente creada.
# lado_cuadrado = 8
# area_cuadrado = lado_cuadrado ** 2
# perimetro_cuadrado = lado_cuadrado * 4
# print("El área del cuadrado es:", area_cuadrado)
# print("El perímetro del cuadrado es:", perimetro_cuadrado)
# #Crear una variable entera llamada “base_Triangulo” de valor 5 y una variable entera llamada “altura_Triangulo” de valor 10, calcular el área del triángulo a partir de las variables anteriormente creadas.
# base_triangulo = 5
# altura_triangulo = 10
# area_triangulo = (base_triangulo * altura_triangulo) / 2
# print("El área del triángulo es:", area_triangulo)
# #Crear una variable entera llamada “baseRectangulo” de valor 8 y una variableentera llamada “alturaRectangulo” de valor 6. Calcular el área y el perímetro del rectangulo a partir de las variables anteriormente creadas.
# base_rectangulo = 8
# altura_rectangulo = 6
# area_rectangulo = base_rectangulo * altura_rectangulo
# perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
# print("El área del rectangulo es:", area_rectangulo)    
# print("El perímetro del rectangulo es:", perimetro_rectangulo)

#Ejericicio 10 (Variable Edad Persona).
#Desarrollar un programa que permita por medio de la edad de una persona, calcular su edad en años, meses y dias.
edad_persona = int(input("Introduce la edad de la persona: "))
#rango de edad
if edad_persona < 0 or edad_persona > 5:
    print("infante")
elif edad_persona >= 6 and edad_persona <= 10:
    print("niño")
elif edad_persona >= 11 and edad_persona <= 15:
    print("pre-adolescente")
elif edad_persona >= 16 and edad_persona <= 18:
    print("adolescente")
elif edad_persona >= 19 and edad_persona <= 25:
    print ("pre-adulto")
elif edad_persona >= 26 and edad_persona <= 40:
    print("adulto")
elif edad_persona >= 41 and edad_persona <= 55:
    print("pre-anciano")
else:
    print("anciano")

