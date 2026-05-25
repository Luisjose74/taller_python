#bucle for = instrucción de control que itera sobre los elementos de una secuencia (como una lista, una tupla, un diccionario, un conjunto o una cadena) o sobre un rango de números.  
Lenguaje = "Python"#iterar sobre cada letra de la palabra "Python"
for letra in Lenguaje:#
    print(letra) #va a imprimir cada letra de la palabra "Python" en una línea diferente
#recocorer una lista con bucle for
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta) #va a imprimir cada fruta de la lista "frutas" en una línea diferente
#con el condicional "Break" se puede salir del bucle for antes de que termine de iterar sobre todos los elementos de la secuencia.
for fruta in frutas:
    if fruta == "banana":
        break #va a salir del bucle for cuando encuentre la fruta "banana"
    print(fruta) #va a imprimir "manzana" y luego va a salir del bucle for cuando encuentre "banana"
# con el condicional "Continue" se puede saltar la iteración actual del bucle for y pasar a la siguiente iteración.
for fruta in frutas:
    if fruta == "banana":
        continue #va a saltar la iteración actual del bucle for y pasar a la siguiente iteración
    print(fruta) #va a imprimir "manzana" y "naranja" pero va a saltar "banana" cuando la encuentre
#cuando utilice "else" dentro de un bucle for, se ejecutara cuando el bucle for termine de iterar sobre todos los elementos de la secuencia.
for fruta in frutas:        
    print(fruta) #va a imprimir "manzana", "banana" y "naranja"
else:
    print("No hay mas frutas") #va a imprimir "No hay mas frutas" después de que el bucle for termine de iterar sobre todos los elementos de la secuencia       
#recorrer un rango de números con bucle for
for i in range(10): #va a imprimir los números del 0 al 9
    print(i)
for i in range(1, 11): #va a imprimir los números del 1 al 10
    print(i)
for i in range(0, 11, 2): #va a imprimir los números pares del 0 al 10
    print(i)
for i in range (1,6) :#va a imprimir los números del 1 al 5
    print(i)
#aplicar un bucle con un ciclo pass
# Edad = int(input("Ingrese su edad: "))  
# if Edad < 18:
#     pass #va a pasar a la siguiente línea de código sin hacer nada si la edad es menor a 18
# else:
#     print("Eres mayor de edad")
#recorrer una tupla con un bucle for
# colores = ("rojo", "verde", "azul")
# for color in colores:
#     print(color) #va a imprimir cada color de la tupla "colores" en una línea diferente
#recorrer un diccionario con un bucle for
diccionario_apendices = {"nombre": "Juan", "apellido": "Pérez", "edad": 30, "ciudad": "Bogotá"}
for clave, valor in diccionario_apendices.items():#se utiliza un bucle for para recorrer el diccionario "diccionario_apendices"
    print(f"{clave}: {valor}") #va a imprimir cada clave y su valor del diccionario "diccionario_apendices" en una línea diferente
#recorrer un conjunto con el bucle while
