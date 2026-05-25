# # #Ejericicio 1: Funcion lista de calificaciones 
# # # ── Ingrear Notas ─────────────────────────────────────
# # Notas = []
# # # for i in range(1,6):# va a ingresar 5 notas del 1 al 5
# # #     nota =float (input(f"Ingresa las Notas {i}: "))
# # #     Notas.append(nota)
# # def calcular_calificaciones(calificaciones):# def: define una función
# #     promedio = sum(calificaciones) / len(calificaciones) # es la ecuacion para sacar promedio
# # #sacar la nota mas alta y la mas baja
# # #---la Nota mas alta---------------------
# #     mas_alta = max(calificaciones) # es la ecuacion para sacar la nota mas alta
# # #---la Nota mas baja----------------
# #     mas_baja = min(calificaciones) # es la ecuacion para sacar la nota mas
# #     return promedio, mas_alta, mas_baja
# # # ----Resultados----------------------
# # promedio, alta, baja = calcular_calificaciones(Notas)
# # print(f"Promedio: {promedio}")
# # print(f"Nota más alta: {alta}")
# # print(f"Nota más baja: {baja}")

# #Ejercicio 2: lista de compras interactiva
# lista_compras = []

# while True:
#     print("\n--- Menu ---")
#     print("1. Agregar item")    
#     print("2. Eliminar item")
#     print("3. Mostrar lista")
#     print("4. Salir")
#     print("------------")

#     opcion = input("Ingrese una opcion: ")
#     if opcion == "1":
#         item = input("Ingrese el item: ")
#         lista_compras.append(item)
#         print(f"{item} agregado.")

#     elif opcion == "2":
#         if len(lista_compras) == 0:
#             print("La lista esta vacia.")
#         else:
#             item = input("Ingrese el item a eliminar: ")
#             if item in lista_compras:
#                 lista_compras.remove(item)
#                 print(f"{item} eliminado.")
#             else:
#                 print(f"{item} no esta en la lista.")

#     elif opcion == "3":
#         if len(lista_compras) == 0:
#             print("La lista esta vacia.")
#         else:
#             print("\n--- Lista de compras ---")
#             for item in lista_compras:
#                 print(f"  - {item}")
#             print("------------------------")
#             print(f"Total de items: {len(lista_compras)}")
#             input("Presione Enter para continuar...")   
#     elif opcion == "4":
#         print("Hasta luego.")
#         break

#     else:
#         print("Opcion no valida.")

# # Ejercicio 3: Agenda de Contactos con Diccionario

# agenda = {}

# # ── Funciones ─────────────────────────────────

# def agregar_contacto(nombre, telefono):        # añade un contacto al diccionario
#     agenda[nombre] = telefono                  # clave: nombre, valor: telefono
#     print(f"Contacto '{nombre}' agregado.")

# def buscar_contacto(nombre):                   # busca un contacto por nombre
#     if nombre in agenda:                       # verifica si el nombre existe
#         print(f"{nombre}: {agenda[nombre]}")
#     else:
#         print(f"'{nombre}' no esta en la agenda.")

# def mostrar_contactos():                       # muestra todos los contactos
#     if len(agenda) == 0:
#         print("La agenda esta vacia.")
#     else:
#         print("\n--- Agenda de Contactos ---")
#         for nombre, telefono in agenda.items():  # .items(): recorre clave y valor
#             print(f"  {nombre}: {telefono}")
#         print(f"  Total: {len(agenda)} contactos")
#         print("---------------------------")

# # ── Menú principal ────────────────────────────
# while True:
#     print("\n--- Menu ---")
#     print("1. Agregar contacto")
#     print("2. Buscar contacto")
#     print("3. Mostrar todos los contactos")
#     print("4. Salir")
#     print("------------")
#     opcion = input("Ingrese una opcion: ")

# # ── Opción 1: Agregar ─────────────────────
#     if opcion == "1":
#         nombre   = input("Ingrese el nombre: ")
#         telefono = input("Ingrese el telefono: ")
#         agregar_contacto(nombre, telefono)

#  # ── Opción 2: Buscar ──────────────────────
#     elif opcion == "2":
#         nombre = input("Ingrese el nombre a buscar: ")
#         buscar_contacto(nombre)

# # ── Opción 3: Mostrar ─────────────────────
#     elif opcion == "3":
#         mostrar_contactos()
#         input("Presiona Enter para volver al menu...")

#  # ── Opción 4: Salir ───────────────────────
#     elif opcion == "4":
#         print("Hasta luego.")
#         break

# # ── Opción no válida ──────────────────────
#     else:
#         print("Opcion no valida.")

# Ejercicio 4: Conversor de Unidades

# # Factores de conversion a metros
# conversiones = {
#     "metros"      : 1.0,
#     "pies"        : 0.3048,
#     "pulgadas"    : 0.0254,
#     "centimetros" : 0.01,
#     "kilometros"  : 1000.0,
#     "millas"      : 1609.34,
#     "yardas"      : 0.9144
# }

# def convertir(cantidad, origen, destino):
#     if origen not in conversiones:
#         print(f"'{origen}' no es una unidad valida.")
#         return None
#     if destino not in conversiones:
#         print(f"'{destino}' no es una unidad valida.")
#         return None
#     en_metros = cantidad * conversiones[origen]
#     resultado = en_metros / conversiones[destino]
#     return resultado

# while True:
#     print("\n=============CONVERSOR DE UNIDADES=============")
#     print("Unidades disponibles:")
#     for unidad in conversiones:
#         print(f"  - {unidad}")
#     print("===============================================")

#     cantidad = input("\nIngrese la cantidad (o 'salir'): ")
#     if cantidad.lower() == "salir":
#         print("Hasta luego.")
#         break

#     cantidad = float(cantidad)
#     origen   = input("Unidad de origen  : ").lower()
#     destino  = input("Unidad de destino : ").lower()

#     resultado = convertir(cantidad, origen, destino)
#     if resultado is not None:
#         print(f"\n{cantidad} {origen} = {resultado:.4f} {destino}")

# Ejercicio 5: Mini Sistema de Gestion de Inventario

inventario = []

def agregar_producto():
    nombre   = input("Nombre del producto: ")
    precio   = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en inventario: "))
    producto = {
        "nombre"   : nombre,
        "precio"   : precio,
        "cantidad" : cantidad
    }
    inventario.append(producto)
    print("Producto agregado al inventario.")

def realizar_venta():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    nombre = input("Nombre del producto a vender: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] == 0:
                print("No hay stock disponible.")
                return
            cantidad_venta = int(input("Cuantas unidades? "))
            if cantidad_venta > producto["cantidad"]:
                print("No hay suficientes unidades.")
                return
            producto["cantidad"] -= cantidad_venta
            total = cantidad_venta * producto["precio"]
            print("Venta realizada. Total: $" + str(total))
            return
    print("Producto no encontrado.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    print("\n=============INVENTARIO=============")
    for producto in inventario:
        print("  Nombre   : " + producto["nombre"])
        print("  Precio   : $" + str(producto["precio"]))
        print("  Cantidad : " + str(producto["cantidad"]) + " unidades")
        print("  ----------------------------------")
    print("  Total de productos: " + str(len(inventario)))
    print("====================================")
    input("Presiona Enter para continuar...")

while True:
    print("\n=============GESTION DE INVENTARIO=============")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("===============================================")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_venta()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("Hasta luego.")
        break
    else:
        print("Opcion no valida.")

    input("Presiona Enter para continuar...")
