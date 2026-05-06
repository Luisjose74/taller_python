#Condicional IF/ELIF/ELSE
if False:
    print("la Condicion es Verdadero")
elif False:
    print("la segunda Condicion es Verdadera en ELIF")
elif True:
    print("la tercera Condicion es Verdadera en ELIF")      
else:           
    print("la Condicion es Falsa")  
# If anidados
#Ejercicio: Clasificacion de edades
edad = 15
if edad < 18:
    print("Eres un menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
# Ejercicio: Clasificacion de edad IF anidados
edad = int(input("Ingrese su edad para ser clasificado: "))
if edad < 18:
    if edad > 12 and edad < 18:
        print("Eres un adolescente")
    else:
        print("Eres un niño")
else:
    if edad >= 18 and edad < 60:
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")
# Ejercicicio: Operador ternario

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("El numero es par" if numero % 2 == 0 else "El numero es impar")