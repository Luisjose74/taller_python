#Actividad 2 Analisis de Temperaturas Semanales
#Ejercicio 1: Crear una lista de temperaturas semanales (14 días) y calcular el promedio.
from operator import index

temperaturas_dias_mayo = [25, 23, 22, 31, 27, 24, 24, 29, 31, 23, 22, 26, 28, 24]
# index:
# 0 = dia 1 usando indices positivos como negativos
print(f"Temperatura del día 1: {temperaturas_dias_mayo[0]}°C")

#6 = dia 7 usando indices positivos como negativo
print(f"Temperatura del día 7: {temperaturas_dias_mayo[-6]}°C")

#12 = penultimo dia 12 usando indices positivos como negativos
print(f"Temperatura del dia 12: {temperaturas_dias_mayo[12]}°C")

#13 = ultimo dia usando indices positivos como negativos
print(f"Temperatura del dia 14: {temperaturas_dias_mayo[13]}°C")

#Slicing o rebanado de la lista para obtener un rango de temperaturas
print(temperaturas_dias_mayo[0:7])  # Muestra las temperaturas desde el día 1 hasta el día 7
print(temperaturas_dias_mayo[7:14]) # Muestra las temperaturas desde el día 8 hasta el día 14

#para llamar los dias pares e impares usando slicing con un paso de 2
Modulo = 0
if Modulo == 0:
    print(temperaturas_dias_mayo[1::2]) # Muestra las temperaturas de los días pares (día 2, 4, 6, etc.)
else:
    print(temperaturas_dias_mayo[0::2]) # Muestra las temperaturas de los días impares (día 1, 3, 5, etc.)

#calcular el promedio de las temperaturas de cada semana usando (sum() y len())
promedio_semana_1 = sum(temperaturas_dias_mayo[0:7]) / len(temperaturas_dias_mayo[0:7])
promedio_semana_2 = sum(temperaturas_dias_mayo[7:14]) / len(temperaturas_dias_mayo[7:14])
print(f"El promedio de temperaturas de la semana 1 es: {promedio_semana_1}°C")
print(f"El promedio de temperaturas de la semana 2 es: {promedio_semana_2}°C")

#Cual semamna tuvo la temperatura promedio mas alta
if promedio_semana_1 > promedio_semana_2:
    print("La semana 1 tuvo la temperatura promedio más alta.")
else:    print("La semana 2 tuvo la temperatura promedio más alta.")  # se realiza con un condicional if para un mensaje mas descriptivo del resultado obtenido.  


