#Actividad 1: Inventario Tienda Escolar
#crear una lista o declarar al menos 6 articulos tienda escolar
from math import prod#importar la libreria math para usar la función prod() que calcula el producto de los elementos de una lista   


productos = ["lapices", "cuadernos", "lapiceras", "borrador", "regla", "tijeras"]
print(productos)

#declarar la lista de productos con precios
precios = [500, 12000, 3500, 1500, 2500, 2500,12000]
print(precios)

#declarar cantidad por cada lista de articulos
cantidades = [10, 5, 8, 15, 12, 10]
print(cantidades)

#Imprime tres listas completas y luego usa len para medir la longitud de cada lista
cantidad_de_productos = len(productos) #cantidad de productos
print("Inventario Tienda Escolar"
"\nProductos:", productos, 
"\nPrecios:", precios, 
"\nCantidades:", cantidades,
"\nCantidad de Productos:", cantidad_de_productos)

print(f"El Producto: {productos[0]} tiene un precio de: {precios[0]} y una cantidad disponible de : {cantidades[0]}")
print(f"El Producto: {productos[1]} tiene un precio de: {precios[1]} y una cantidad disponible de : {cantidades[1]}")
print(f"El Producto: {productos[2]} tiene un precio de: {precios[2]} y una cantidad disponible de : {cantidades[2]}")    
print(f"El Producto: {productos[3]} tiene un precio de: {precios[3]} y una cantidad disponible de : {cantidades[3]}")        
print(f"El Producto: {productos[4]} tiene un precio de: {precios[4]} y una cantidad disponible de : {cantidades[4]}")
print(f"El Producto: {productos[5]} tiene un precio de: {precios[5]} y una cantidad disponible de : {cantidades[5]}") 

#Mostrar el tipo de dato utilizando type() para cada lista
print(type(productos))#tipo 'list'

#Mostrtar el tipo de elemento usando type(productos[0]) para cada elemento de la lista productos
print(type(productos[0]))#tipo 'str' para el elemento "lapices"


