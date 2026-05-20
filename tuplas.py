#crear una tupla con unn solo elemento
#estrucutra
#indice:   0           1           2
from flask.config import T


tupla = ("objeto_1","objeto_2","objeto_3") 
print(type(tupla))
#
tupla_2 = "a", "b", "c"#se debe agregar una coma al final para indicar que es una tupla con un solo elemento
print(type(tupla_2))
#tupla_3 = ("a") #se debe agregar una coma al final para indicar que es una tupla con un solo elemento
tupla_3 = ("a",) 
print(type(tupla_3))
#tupla_4 = ("hola") #se debe agregar una coma al final para indicar que es una tupla con un solo elemento
tupla_4 = ("hola",)
print(type(tupla_4))

#tupla mixta
tupla_mixta = ("hola", 123, 3.14, True, (1,2,3))
print(type(tupla_mixta))

#tupla de Aprendices Sena ADSO
#indice:        0          1         2         3        4
aprendices_adso =("Giselle", "Felipe", "Sofia", "camilo", "luisa")
print(aprendices_adso[3]) #acceder a un elemento de la tupla con indice 3

#modificar un elemento de la tupla
# aprendices [2] = "maria" #las tuplas son inmutables, no se pueden modificar sus elementos una vez creada la tupla

#consultar rangos de elementos de la tupla slicing o rebanado de la tupla para obtener un rango de elementos
print(aprendices_adso[1:4])#el rango maximo no se incluye
print(aprendices_adso[0:])#no se incluye el indice de inicio, se muestra desde el indice 0 hasta el final de la tupla

# Sumar dos tuplas con el operador + para concatenar tuplas
tupla_1 = ("a", "b", "c")   
tupla_2 = ("d", "e", "f")
tupla_3 = tupla_1 + tupla_2
print(tupla_3) #('a', 'b', 'c', 'd', 'e', 'f')

#multiplicar una tupla por un entero para repetir sus elementos
tupla_4 = tupla_1 * 3
print(tupla_4) #('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# medir el largo con len() de una tupla
print(len(tupla_3)) #6 elementos en la tupla_3

#contar el numero de veces que un elemento se repite en una tupla con count()  
print(tupla_3.count("a")) #2 veces el elemento "a" en la tupla_3

#obtener el indice de un elemento con index()
print(tupla_3.index("b")) #el indice del elemento "b" en la tupla_3

#modificar un TUPLA en una lista con list() y luego convertirla nuevamente a tupla con tuple()
print(type(aprendices_adso))#tipo 'tuple'
lista_aprendices_adso = list(aprendices_adso)
print(type(lista_aprendices_adso))
lista_aprendices_adso.append("jose")#agregar un elemento a la lista
print(lista_aprendices_adso)
#convertirt la lista nuevamente a tupla con tuple()
aprendices_adso = tuple(lista_aprendices_adso)
print(type(aprendices_adso))

#comprobar pertenece a una tupla con el operador in
print("camilo" in aprendices_adso) #True
print("maria" in aprendices_adso) #False

#empaquetar tuplas con zip() para combinar elementos de dos o mas tuplas en una sola tupla de tuplas
programa_1 = "Adso"
programa_2 = "SST"
programa_3 = "topografia"
tupla_programas = (programa_1, programa_2, programa_3)
print(list(tupla_programas)) # ('Adso', 'SST', 'topografia')

#desempaquetar tuplas con unpacking
tupla_desempaquetada = ("Adso", "SST", "topografia")
programa_1, programa_2, programa_3 = tupla_desempaquetada
print(programa_1) #Adso

#Ejercicio 2 didactico del principio de desempaquetar
tupla_ciudades = ("Bogota", "Medellin", "Cali")
ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades
print(ciudad_1) #Bogota
print(ciudad_2) #Medellin   
print(ciudad_3) #Cali

#ejercicio 3 con asterisco para desempaquetar tuplas con un numero variable de elementos
tupla_numeros = (1, 2, 3, 4, 5)
numero_1, *numeros_restantes = tupla_numeros
print(numero_1) #1
print(numeros_restantes) #[2, 3, 4, 5]  
#recorer tuplas con for para iterar sobre los elementos de una tupla
for ciudad in tupla_ciudades:#guarda cada elemento de la tupla_ciudades en la variable ciudad en cada iteracion del ciclo for
    print(ciudad)


