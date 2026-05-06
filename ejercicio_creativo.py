#Ejericicio Creativo:*
"""Crear un programa que me de facilidad para seleccionar
el tipo de comida que quiero comer y cuantas calorias tiene cada una de las opciones.
Luego de eso calcular el total de calorias que me han consumido en el dia."""
#Enunciado:*
"""se va a llamar "B.L.D Food" y se va a crear un programa que me de facilidad 
para seleccionar el tipo de comida que quiero comer y cuantas calorias tiene 
cada una de las opciones."""
from tkinter import Menu


print("=" * 45)
print ("B.L.D FOOD")
print("=" * 45)
#---- Entrada de datos
# input() recibir datos del usuario a través de la consola. 
# En este caso, se utiliza para solicitar al usuario que ingrese el tipo de comida que desea comer y la cantidad de calorias que tiene.
# PASO 1: Solictar al usuario que seleccion la comida si es desayuno, almuerzo o cena utilizando la función input() y almacenar el resultado en una variable.
Tipo_comidda = input("Seleccione el tipo de comida que desea comer: 1) Desayuno 2) Almuerzo 3) Cena: ")
#PASO 2: Solicitar al usuario que ingrese el tipo de comida que desea comer y la cantidad de calorias que tiene utilizando la función input().
menu_desayuno = {
    "huevos🥚":    155,
    "pan🍞":       265,
    "leche🥛":      61,
    "hojuela🌾":   379,
    "salchicha🌭": 290,
}

menu_almuerzo = {
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

total_dia = 0

if Tipo_comidda == "1":
    comida = menu_desayuno
elif Tipo_comidda == "2":
    comida = menu_almuerzo
elif Tipo_comidda == "3":
    comida = menu_cena
else:
    print("Opcion no valida")
    exit()

for comida, calorias in comida.items():
    print(f"{comida}: {calorias} calorias")
    total_dia += calorias

print(f"Total de calorias consumidas en el dia: {total_dia} calorias")



