# listas

#estructura

#indice:   0           1           2
from itertools import count


listas =["objeto_1", "objeto_2", "objeto_3"]
print(type(listas))

#lista mixta
lista_mixta = ["hola", 123, 3.14, True]
print(type(lista_mixta))


#lista de aprendices sena adso

#indice:        0          1         2         3        4
aprendices =["Giselle", "Felipe", "Sofia", "camilo", "luisa"]
print(aprendices)

#acceder a un elemento de la lista
print(aprendices[1])

#modificar un elemento de la lista
aprendices[2] = "maria"
print(aprendices)

#consultar rangos de elementos de la lista
print(aprendices[0:2])  # Muestra los elementos desde el índice 0 hasta el 1
print(aprendices[1::4])
print(aprendices[:3])


aprendices_ficha_3321349  = ["camilo", "andres", "maria", "pedro", "jorge","felipe"]
aprendices_ficha_1254785 = ["luisa", "sofia", "felipe", "ana", "carlos","messi"]

#concatenar listas (+)
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_1254785
print(aprendices_adso)

#unir listas con extend
aprendices_ficha_3321349.extend(aprendices_ficha_1254785)
print(aprendices_ficha_3321349)

#medir la longitud de una lista con len()
print(len(aprendices_adso)) #10 elementos en la lista aprendices_adso

longitud_aprendices_adso = len(aprendices_adso)
print(f"La longitud de la lista aprendices_adso es: {longitud_aprendices_adso}")

#elementos repetidos en una lista count()
print(aprendices_adso.count("felipe"))

count_felipe = aprendices_adso.count("felipe")
print(f"El nombre 'felipe' se repite {count_felipe} veces en la lista aprendices_adso.")

#obtener el índice de un elemento con index()
index_ana = aprendices_adso.index("ana")
print(f"El índice de 'ana' en la lista aprendices_adso es: {index_ana}")

#Copiar una lista con copy()
nueva_lista_adso = aprendices_adso.copy()
print(nueva_lista_adso)

#agregar elementos al final de la lista con append()
nueva_lista_adso.append("Radamel Falcao")
print(nueva_lista_adso)

#agregar en el septimo elemento de la lista con insert()
nueva_lista_adso.insert(7, "James Rodriguez")
print(nueva_lista_adso)

#borrar o remover un elemento de la lista con remove() o pop()
nueva_lista_adso.remove("Radamel Falcao")
print(nueva_lista_adso)

#borrar el septimo elemento de la lista con pop() con un índice específico que 7 es el índice del elemento "James Rodriguez"
nueva_lista_adso.pop(7)
print(nueva_lista_adso)

#comprobar si un elemento existe en la lista con in "pertinencia"
if "messi" in nueva_lista_adso:
    print("El nombre 'messi' se encuentra en la lista nueva_lista_adso.")
else:    
    print("El nombre 'messi' no se encuentra en la lista nueva_lista_adso.")

#ordenar una lista con sort() organizar de forma alfabetica los elementos de la lista
nueva_lista_adso.sort()
print(nueva_lista_adso)

#ordenar una lista revertida con reverse() organizar de forma inversa los elementos de la lista
nueva_lista_adso.reverse()
print(nueva_lista_adso)

#limpiar una lista con clear()
nueva_lista_adso.clear()
print(nueva_lista_adso)

print(aprendices_adso)


