#BUCLE WHILE = instruccion de control cuando es una variable true
i = 0 # incia la variable de control
while i < 5: # mientras la variable de control sea menor a 5
    print("hola soy un bucle WHILE") # va a imprimir el valor de la variable de control
    if i == 3: # va a incrementar la variable de control en 1 cada vez que se ejecute el bucle while    
        i += 1
        continue # va a saltar la iteración actual del bucle while y pasar a la siguiente iteración cuando i sea igual a 3
    i += 1

# Juego de pokemon
puntos_vida = 100
pokemon = input ("Elige tu pokemon: pikachu, charmander, squirtle: ") # se pide al usuario que ingrese el nombre de su pokemon

#mientras los puntos de vida sean mayores a 0, el juego sigue
while puntos_vida > 0:
    print(f"Tu pokemon {pokemon} tiene {puntos_vida} puntos de vida") # se muestra al usuario los puntos de vida de su pokemon
    ataque = input("ingresa el daño de tu ataque: ") # se pide al usuario que ingrese el daño de su ataque
    puntos_vida -= int(ataque) # se resta el daño del ataque a los  puntos de vida del pokemon
print(f"Tu pokemon {pokemon} ha sido derrotado") # se muestra al usuario que su pokemon ha sido derrotado cuando los puntos de vida sean menores o iguales a 0