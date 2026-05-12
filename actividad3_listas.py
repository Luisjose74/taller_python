# Ativivdad 3: Gestion de listas de reproduccion de musica (5 canciones))
Canciones_favoritas = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
#metodos de orden y estado lista con append() para agregar una cancion a la lista
Canciones_favoritas.append("Sweet Child O' Mine")
#para agregarla en la segunda posicion
Canciones_favoritas.insert(1, "Like a Rolling Stone")
#para fusionar con otra lista de canciones
nuevas_canciones = ["Bonus track1", "Bonus track1", "Bonus track2", "Bonus track3"]
Canciones_favoritas.extend(nuevas_canciones)
#para eliminar una cancion de la lista
Canciones_favoritas.remove("Hotel California")
#para eliminar la ultima cancion de la lista
Canciones_favoritas.pop()
#para ordenar la lista de canciones alfabeticamente
Canciones_favoritas.sort()
#cuantas canciones hay?
print(f"La playlist tiene {len(Canciones_favoritas)} canciones.")
#en que posicion esta la cancion que agregue
posicion_cancion = Canciones_favoritas.index("Like a Rolling Stone")
print(f"La cancion 'Like a Rolling Stone' esta en la posicion: {posicion_cancion}.")
#cuantas veces aparece "bonus track1" en la lista
veces_bonus_track1 = Canciones_favoritas.count("Bonus track1")
print(f"La cancion 'Bonus track1' aparece {veces_bonus_track1} veces en la playlist.")