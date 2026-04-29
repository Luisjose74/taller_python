print("Hello world")

# Este es un comentario de varias lineas"

"""
Esto es un comentario 
en varias 
lineas
"""

#Consultar el tipo de dato
print(type("Hello world")) #tipo 'str'
print(type(1)) #tipo 'int'

#Tipo de Escritura de Variables
Nombre="Jhon Alexander"
Apellido="Barrero Barrera"
Edad=32
Altura=1.70
Activo=True
Correo = "johnalexanderbarrero@gmail.com"
Telefono = 5555555555
Cedula = 123456789

#imprimir el tipo de dato y la variable
print(type(Nombre),Nombre)#Se coloca una coma para que muestre la informacion del dato
print(type(Apellido),Apellido)
print(type(Edad),Edad)
print(type(Activo),Activo)
print(type(Correo),Correo)
print(type(Telefono),Telefono)


#Casting (Casteo) Conversion de el tipo de dato a una variable ejemlp de un str a un int
Telefono_int = int(Telefono)
#Convertir la Edad que esta entero a float
Edad_float = float(Edad)
Altura_int = int(Altura)
print(type(Edad_float),Edad_float)
print(type(Altura_int),Altura_int)
#Convertir a un int en str
Cedula_str = str(Cedula)
print(type(Cedula_str),Cedula_str)

#Indentacion en Phyton
if 5>2:
    print("5 es mayor que 2")
else:
    print("5 no es menor que 2")

nombre_completo = input("Ingrese su nombre completo:")
print(nombre_completo)

edad = int(input("Ingrese su edad: "))
print(type(edad), edad)

#impresion con formato f-string
print(f"Mi nombre es {nombre_completo} y tengo {edad} años")

