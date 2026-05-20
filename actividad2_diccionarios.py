grupo_ADSO = {
    "3321349": {
        "aprendiz_1": {
            "nombre": "Camilo",
            "edad": 25,
            "notas": [4.5, 3.8, 4.0, 4.2],
            "ciudad": "Bogotá"
        },
        "aprendiz_2": {
            "nombre": "Laura",
            "edad": 22,
            "notas": [2.5, 3.0, 2.8, 2.6],
            "ciudad": "Medellín"
        },
        "aprendiz_3": {
            "nombre": "Sara",
            "edad": 21,
            "notas": [4.8, 4.9, 5.0, 4.7],
            "ciudad": "Cali"
        },
        "aprendiz_4": {
            "nombre": "Pedro",
            "edad": 23,
            "notas": [3.0, 2.9, 3.1, 3.2],
            "ciudad": "Cartagena"
        },
    }
}
# Reporte usando .items()
print("==================================================")
print("         REPORTE DE APRENDICES")
print("==================================================")

for aprendiz, datos in grupo_ADSO["3321349"].items():
    promedio = sum(datos["notas"]) / len(datos["notas"])   # Formula calcular promedio
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    print(f"El aprendiz {datos['nombre']} tiene un promedio de: {round(promedio, 2)} y su estado es: {estado}")

#Agregando un nuevo aprendiz con nueva ficha 3321350
grupo_ADSO["3321350"] = {
    "aprendiz_1": {
        "nombre": "Andres",
        "edad": 24,
        "notas": [3.5, 3.8, 4.0, 3.9],
        "ciudad": "Bucaramanga"
    },
}
print("\n==================================================")
print("         APRENDICES ACTUALIZADOS")
print("==================================================")

for aprendiz, datos in grupo_ADSO["3321350"].items():
    promedio = sum(datos["notas"]) / len(datos["notas"])   # Formula calcular promedio
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    print(f"El aprendiz {datos['nombre']} tiene un promedio de: {round(promedio, 2)} y su estado es: {estado}")             
#Luego actualiza la ciudad de uno de los aprendices existentes con dicc[ficha]["ciudad"]
grupo_ADSO["3321349"]["aprendiz_2"]["ciudad"] = "Barranquilla"
print("\n==================================================")
print("         APRENDICES ACTUALIZADOS")
print("==================================================")


ranking = sorted(grupo_ADSO["3321349"].items(), key=lambda item: sum(item[1]["notas"]) / len(item[1]["notas"]), reverse=True)

posicion = 1
for aprendiz, datos in ranking:
    promedio = sum(datos["notas"]) / len(datos["notas"])
    print(posicion, "-", datos["nombre"], "->", round(promedio, 2))
    posicion = posicion + 1


