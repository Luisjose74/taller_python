# #FUNCION: es unn bloque de código reutilizable que realiza una tarea específica. Se define utilizando la palabra clave "def" seguida del nombre de la función y paréntesis que pueden contener parámetros. Las funciones pueden devolver un valor utilizando la palabra clave "return".
# #llamo la funcion
# def nombre_funcion():
#     print("Hola, soy una función") #defino la función "nombre_funcion" que imprime un mensaje en la consola

# #llamo la funcion
# nombre_funcion() #ejecuto la función "nombre_funcion" que imprime el mensaje en la consola
# #funcion con parametros
# def saludar(nombre): #defino la función "saludar" que recibe un parámetro "nombre"  
#     return f"Hola, {nombre}, Bienvenido a la Programación con funciones"#devuelve un mensaje de saludo utilizando el valor del parámetro "nombre" y la cadena de texto "Bienvenido a la Programación con funciones"  
# print(saludar("Juan"))
# print(saludar("Pedro"))
# print(saludar("Maria")) #ejecuto la función "saludar" pasando el argumento "Juan" que se asigna al parámetro "nombre" y devuelve el mensaje de saludo con el nombre "Juan"      

# #operacion matematica con funciones
# def sumar(num_1, num_2): #defino la función "suma" que recibe dos parámetros "numero1" y "numero2"
#     sumar = num_1 + num_2#devuelve la suma de los parámetros "numero1" y "numero2"
#     return sumar #devuelve el resultado de la suma   
# suma = sumar(5, 3)#ejecuto la función "suma" pasando los argumentos 5 y 3 que se asignan a los parámetros "numero1" y "numero2" respectivamente, y devuelve el resultado de la suma que se asigna a la variable "resultado" 
# print(suma)#funcion con parametros por defecto  

# #restar
# def restar(num_1,num_2):
#     restar = num_1 - num_2
#     return restar
# resta = restar(10,4)

# #multiplicar
# def multiplicar(num_1,num_2):
#     resultado = num_1 * num_2
#     return resultado
# multiplicacion = multiplicar(5,3)

# #division
# def dividir(num_1,num_2):
#     division = num_1 / num_2
#     return division
# division = dividir(10,2)

# #ejericico para validar edad
# # def clasificar_edad(edad):
# #     if edad < 18:
# #      if edad > 12 and edad < 18:
# #         print("Adolescente")
# #     else:
# #         if edad >= 18 and edad <= 60:
# #             print("Adulto")
# #         else:
# #             print("Adulto mayor")
# # #llamar la funcion
# # edad = int(input("Ingrese su edad: "))
# # clasificar_edad(edad)

#Usuarios Sofia plus
aprendices_ficha_1 = ["Juan", "Pedro", "Maria", "Luisa", "Carlos", "Ana", "Sofia", "Andres", "Santiago", "Valentina"]
def mostrar_aprendices(ficha_1):
    print(f"los aprendices de la ficha 1 son: {ficha_1}") #defino la función "mostrar_aprendices" que recibe un parámetro "ficha_1" y devuelve un mensaje con la lista de aprendices
    for aprendiz in ficha_1:
        print(aprendiz)
mostrar_aprendices(aprendices_ficha_1)

#agreegar aprendiz a la ficha
# def agregar_aprendiz(ficha_1, aprendiz):
#     ficha_1.append(aprendiz)
#     return ficha_1
# # aprendiz = input("Ingrese el nombre del aprendiz a agregar: ")
# agregar_aprendiz(aprendices_ficha_1, aprendiz)
# print(f"el aprendiz {aprendiz} ha sido agregado a la ficha 1")#ejecuto la función "agregar_aprendiz" 
# print(f"los aprendices de la ficha 1 son: {aprendices_ficha_1}") #imprimo la lista de aprendices actualizada con el nuevo aprendiz agregado a la ficha 1    

#modificar un elemento de una lista
def modificar_aprendiz(ficha_1, aprendiz_viejo, aprendiz_nuevo):
    if aprendiz_viejo in ficha_1:
        index = ficha_1.index(aprendiz_viejo)
        ficha_1[index] = aprendiz_nuevo
        print(f"El aprendiz {aprendiz_viejo} ha sido modificado por {aprendiz_nuevo} en la ficha 1")
    else:
        print(f"El aprendiz {aprendiz_viejo} no se encuentra en la ficha 1")

modificar_aprendiz(aprendices_ficha_1, "Juan", "Miguel")
print(f"los aprendices de la ficha 1 son: {aprendices_ficha_1}")

#eliminar un elemento de una lista
def eliminar_aprendiz(ficha_1, aprendiz):
    if aprendiz in ficha_1:
        ficha_1.remove(aprendiz)
        print(f"El aprendiz {aprendiz} ha sido eliminado de la ficha 1")
    else:
        print(f"El aprendiz {aprendiz} no se encuentra en la ficha 1")

eliminar_aprendiz(aprendices_ficha_1, "Pedro")
print(f"los aprendices de la ficha 1 son: {aprendices_ficha_1}")
