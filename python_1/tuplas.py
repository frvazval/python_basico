"""
TUPLAS
Es una colección INMUTABLE de datos
"""

tupla = ("Anna", "Pou", 20, "anna@email.com")
print(tupla)

mi_tupla = 3, 4, 5, # Al ponerle la coma final sabe que es una tupla
print(type(mi_tupla))

# tupla[0] = "Marta" # Da un error porque no se puede modificar

# Para poder modificar el contenido de una tupla hay que crearse una lista temporal

lista_temporal = list(tupla) # Copia los valores en una lista temporal
lista_temporal[0] = "Marta"  # Modifica el valor en la lista temporal
print(lista_temporal)
tupla = tuple(lista_temporal) # Convierte la lista temporal en tupla
print(tupla)
print(tupla[1:3]) # Muestra a partir de la posición 1 hasta kla 3, pero no muestra la 3

for item in tupla:
    print(item)