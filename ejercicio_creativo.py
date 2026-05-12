#Ejericicio Creativo:*
"""Crear un programa que me de facilidad para seleccionar
el tipo de comida que quiero comer y cuantas calorias tiene cada una de las opciones.
Luego de eso calcular el total de calorias que me han consumido en el dia."""
#Enunciado:*
"""se va a llamar "B.L.D Food" y se va a crear un programa que me de facilidad 
para seleccionar el tipo de comida que quiero comer y cuantas calorias tiene 
cada una de las opciones."""

print("=" * 45)
print ("B.L.D FOOD")
print("=" * 45)
#---- Entrada de datos
# input() recibir datos del usuario a través de la consola. 
# En este caso, se utiliza para solicitar al usuario que ingrese el tipo de comida que desea comer y la cantidad de calorias que tiene.
# PASO 1: Solictar al usuario que seleccion la comida si es desayuno, almuerzo o cena utilizando la función input() y almacenar el resultado en una variable.
Tipo_comidda = input("Seleccione el tipo de comida que desea comer: 1) Desayuno 2) Almuerzo 3) Cena: ")
#PASO 2: Solicitar al usuario que ingrese el tipo de comida que desea comer y la cantidad de calorias que tiene utilizando la función input().
menu_desayuno = {#creamos un diccionario con las comidas y sus calorias
    "huevos🥚":    155,
    "pan🍞":       265,
    "leche🥛":      61,
    "hojuela🌾":   379,
    "salchicha🌭": 290,
}

menu_almuerzo = {#creamos un diccionario con las comidas y sus caloria
    "arroz🍚":      130,
    "pollo🐔":      165,
    "carne res牛肉":  250,
    "pescado🐟":    206,
    "legumbres🌱":  116,
}

menu_cena = {
    "te☕":      1,
    "cafe☕":    2,
    "cacao🍫":   228,
    "fruta🍓":   52,
    "verdura🥬": 25,
}
#Paso 3: Calcular el total de calorias consumidas en el dia utilizando un bucle for.
total_dia = 0 
"""declaramos una variable para el total de calorias consumidas en el dia, 
esto nos permite almacenar el valor calculado y utilizarlo posteriormente para mostrar el total 
de calorias consumidas en el dia."""
#Paso 4: Imprimir el total de calorias consumidas en el dia utilizando la función print().  
if Tipo_comidda == "1":#si el tipo de comida es 1, se asigna el diccionario del menu de desayuno a la variable comida.
    comida = menu_desayuno # se asigna el diccionario del menu de desayuno a la variable comida
elif Tipo_comidda == "2":#si el tipo de comida es 2, se asigna el diccionario del menu de almuerzo a la variable comida.
    comida = menu_almuerzo # se asigna el diccionario del menu de almuerzo a la variable comida
elif Tipo_comidda == "3": #si el tipo de comida es 3, se asigna el diccionario del menu de cena a la variable comida.
    comida = menu_cena # se asigna el diccionario del menu de cena a la variable comida
else:
    print("Opcion no valida") # si el tipo de comida no es 1, 2 o 3, se imprime un mensaje de error
    exit() # sale del programa

for comida, calorias in comida.items(): # se utiliza un bucle for para recorrer el diccionario comida
    print(f"{comida}: {calorias} calorias") # se imprime el nombre de la comida y las calorias
    total_dia += calorias # se suma las calorias a la variable total_dia

print(f"Total de calorias consumidas en el dia: {total_dia} calorias") 

# cantidad de calorias en el dia



