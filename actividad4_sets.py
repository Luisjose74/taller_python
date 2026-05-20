# Crear conjuntos de aprendices matriculados por programa
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# Total de aprendices únicos en los tres programas (unión triple)
aprendices_unicos = python_curso.union(java_curso).union(bd_curso)
print("Total de aprendices únicos en los tres programas:", aprendices_unicos)

# Aprendices que cursan Python Y Java simultáneamente
aprendices_python_java = python_curso.intersection(java_curso)
print("Aprendices que cursan Python Y Java simultáneamente:", aprendices_python_java)

# Aprendices que solo están en Python (no en Java ni en BD)
aprendices_python = python_curso.difference(java_curso).difference(bd_curso)
print("Aprendices que solo está en Python (no en Java ni en BD):", aprendices_python)

# Aprendices que están en exactamente dos programas (ni en uno solo ni en los tres)
aprendices_dos_programas = python_curso.intersection(java_curso).intersection(bd_curso)
print("Aprendices que está en exactamente dos programas (ni en uno solo ni en los tres):", aprendices_dos_programas)

"""A partir de la siguiente lista con duplicados — inscripciones =
['Ana','Luis','Ana','Marta','Carlos','Luis','Sofia','Pedro','Ana'] — usa un conjunto para
determinar cuántos aprendices únicos se inscribieron y quiénes son."""
inscripciones = ['Ana','Luis','Ana','Marta','Carlos','Luis','Sofia','Pedro','Ana']
aprendices_unicos = set(inscripciones)
print("Número de aprendices únicos que se inscribieron:", len(aprendices_unicos))
print("Aprendices únicos:", aprendices_unicos)
"""Crea un diccionario conteo_programas donde cada clave sea el nombre de un
aprendiz (de la unión) y el valor sea el número de programas en los que está
matriculado. Usa comprensión de diccionario."""
conteo_programas = {aprendiz: sum(1 for curso in [python_curso, java_curso, bd_curso] 
    if aprendiz in curso) for aprendiz in python_curso.union(java_curso).union(bd_curso)}
print("Conteo de programas por aprendiz:", conteo_programas)
#Bonus: Identifica e imprime quién está matriculado en los tres programas a la vez. 
aprendices_tres_programas = python_curso.intersection(java_curso).intersection(bd_curso)
print("Aprendices matriculados en los tres programas a la vez:", aprendices_tres_programas)