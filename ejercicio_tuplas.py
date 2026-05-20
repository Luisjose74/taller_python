#Ejercicio 1: crear dos tuplas (vectores) y producto escalar
vector_1 = (1, 2, 3)
vector_2 = (-1, 0, 2)
producto_escalar = vector_1 + vector_2
print(f"El producto escalar de los vectores es: {producto_escalar}")#El producto escalar de los vectores es: (0, 2, 5)
# print(sorted (producto_escalar))#El producto escalar de los vectores es: (0, 2, 5) ordenado de menor a mayor
#ejericio 2: Ordenar precios de menor a mayor y mostrar el precio más bajo y el más alto
precios =(50,75,46,80,65,2)
ordenar_precios = sorted(precios)
print (ordenar_precios[0])#El precio más bajo es: 2 donde [0] de la tupla ordenada es el primer elemento que es el más bajo
print (ordenar_precios[-1])#El precio más alto es: 80 donde [-1] de la tupla ordenada es el último elemento que es el más alto


