#ACTIVDADAD CALCULADORA DE NOTAS - SENA ADSO
from ast import Not
import math#libreria para realizar operaciones matematicas
print("=" * 45)
print ("CALCULADORA DE NOTAS")
print("=" * 45)
"""sirve para imprimir una linea de 45 caracteres iguales, 
en este caso el signo igual (=) para separar secciones del programa y mejorar la legibilidad.
#Paso 1: Solicitar al usuario que ingrese las tres calificaciones utilizando la función input() 
# y convertirlas a números decimales utilizando float()"""
nota1 = float(input("Calificacion 1: "))#float() convierte un texto en decimal
nota2 = float(input("Calificacion 2: "))
nota3 = float(input("Calificacion 3: "))

#Paso 2: Verificar si las calificaciones están en el rango de 0 a 5.0 utilizando un if.
"""0r: es un operador logico que se utiliza para combinar varias condiciones. En este caso, 
se verifica si alguna de las calificaciones es menor a 0 o mayor a 5.0 """
if nota1 < 0 or nota1 > 5.0 or nota2 < 0 or nota2 > 5.0 or nota3 < 0 or nota3 > 5.0:
    print("Error: Las calificaciones deben estar entre 0 y 5.0")
    exit()#sale del programa

print("=" * 45)

#Paso 3: Calcular el promedio de las tres calificaciones utilizando la función fsum() y la librería math.
"""#math.fsum() se utiliza para sumar una lista de números de manera precisa, 
evitando errores de redondeo que pueden ocurrir con la función sum() estándar. 
En este caso, se suman las tres calificaciones y luego se divide por 3 para obtener el promedio."""
promedio = math.fsum([nota1, nota2, nota3]) / 3
promedio = round(promedio, 2)
print(f"El promedio es: {promedio}")

print("=" * 45)
#Paso 4: Calcular una nota faltante para alcanzar la nota máxima de 5.0 utilizando un condicional if.
"""declaramos una variable para la nota maxima, esto nos permite cambiar el valor de la nota maxima 
en un solo lugar si es necesario, en lugar de tener que buscar y cambiar cada instancia de 5.0 en el código.
"""
Nota_maxima = 5.0#  en el código.
if promedio < Nota_maxima:
    falta = round(Nota_maxima - promedio, 2)# redondeamos el resultado a dos decimales
    print(f"Para alcanzar la nota maxima te falta: {falta}") # f para formatear cadenas de texto con variables
else:
    print("Ya has alcanzado la nota máxima.") # f para formatear cadenas de texto con variables

print("=" * 45)
#Paso 5: Determinar si el estudiante aprobó o no la materia utilizando un condicional if. 
# La nota mínima para aprobar es 3.0.
Aprobo = 3.0#declaramos una variable para la nota minima para aprobar
if promedio >= Aprobo: #if es un operador condicional que se utiliza para combinar varias condiciones.
    print ("👍 Aprobo la materia")#emoticon: windows +.
else:#else donde se verifica si el promedio es menor a la nota minima para aprobar
    print ("❌ No aprobo la materia")










