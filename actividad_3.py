# Actividad 3:Clasificador de IMC - SENA ADSO
print("=" * 45)
print ("CLASIFICADOR DE IMC")
print("=" * 45) # sirve para imprimir una linea de 45 caracteres iguales, en este caso el signo igual (=) para separar secciones del programa y mejorar la legibilidad.
#---- Entrada de datos
# input() recibir datos del usuario a través de la consola. 
# En este caso, se utiliza para solicitar al usuario que ingrese su peso en kilogramos y su estatura en metros.
# float() convierte un texto en decimal.
#PASO 1: Solicitar al usuario que ingrese su peso en kg y su estatura en metros utilizando la función input() y convertirlos a números decimales utilizando float().    
peso = float(input("Ingrese su peso en kg: "))#declaramos una variable para el peso, esto nos permite almacenar el valor ingresado por el usuario y utilizarlo posteriormente en el cálculo del IMC.
estatura = float(input("Ingrese su estatura en metros: "))#declaramos una variable para la estatura, esto nos permite almacenar el valor ingresado por el usuario y utilizarlo posteriormente en el cálculo del IMC.
imc = peso / (estatura** 2)# se calcula el IMC dividiendo el peso entre la estatura al cuadrado. El operador ** se utiliza para elevar la estatura al cuadrado.
imc = round(imc, 2)#redondeamos el resultado a dos decimales
print("=" * 45)
#PASO 2: Calcular el IMC utilizando la fórmula: IMC = peso / (estatura^2) y redondear el resultado a dos decimales utilizando la función round().
print(f"Su IMC es: {imc}") #f para formatear cadenas de texto con variables
print("=" * 45)
#PASO 3: Clasificar el IMC utilizando un condicional if/elif/else según las siguientes categorías:
if imc < 18.5:#declaramos una variable para el IMC bajo peso esto nos permite almacenar el valor calculado y utilizarlo posteriormente en el cálculo del IMC.
    print("Bajo peso")#si el IMC es menor a 18.5, se considera que la persona tiene bajo peso.
elif imc >= 18.5 and imc < 24.9:#and es un operador logico que se utiliza para combinar dos condiciones. En este caso, se verifica si el IMC es mayor o igual a 18.5 y al mismo tiempo menor a 24.9.
    print("Peso normal")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidad")
          