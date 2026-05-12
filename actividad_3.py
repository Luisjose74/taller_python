# Actividad 3:Clasificador de IMC - SENA ADSO
print("=" * 45)
print ("CLASIFICADOR DE IMC")

print("=" * 45) # Sirve para imprimir una linea de 45 caracteres iguales, 
# input() recibir datos del usuario a través de la consola. 
# En este caso, se utiliza para solicitar al usuario que ingrese su peso en klg, estatura en mts
# float() convierte un texto en decimal.
#PASO 1: Solicitar al usuario que ingrese su peso en kg y su estatura en metros utilizando la función input() 
# y convertirlos a números decimales utilizando float().    
peso = float(input("Ingrese su peso en kg: "))#declaramos una variable para el peso.
estatura = float(input("Ingrese su estatura en metros: "))#declaramos una variable para la estatura
imc = peso / (estatura** 2)# se calcula el IMC dividiendo el peso entre la estatura al cuadrado. 
imc = round(imc, 2)#redondeamos el resultado a dos decimales
print("=" * 45)
#PASO 2: Calcular el IMC utilizando la fórmula: IMC = peso / (estatura^2) y 
# redondear el resultado a dos decimales utilizando la función round().
print(f"Su IMC es: {imc}") #f para formatear cadenas de texto con variables
print("=" * 45)
#PASO 3: Clasificar el IMC utilizando un condicional if/elif/else según las siguientes categorías:
if imc < 18.5:#declaramos una variable para el IMC bajo peso 
    print("Bajo peso")#si el IMC es menor a 18.5, se considera que la persona tiene bajo peso.
elif imc >= 18.5 and imc < 24.9:#and es un operador logico que se utiliza para combinar dos condiciones. 
    print("Peso normal")#si el IMC está entre 18.5 y 24.9, se considera que la persona tiene un peso normal.
elif imc >= 25 and imc < 29.9:#elif es un operador condicional que se utiliza para combinar varias condiciones.
    print("Sobrepeso") #
elif imc >= 30: #si el IMC es mayor o igual a 30, se considera que la persona tiene obesidad.
    print("Obesidad") # si el IMC es mayor o igual a 30, se considera que la persona tiene obesidad.
          