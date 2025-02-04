"""
LISTAS
"""

# Las listas equivalen a los "arrays" de otros lenguajes
# Las listas y los string son "iterables" (Se pueden recorrer)
# La lista es una colección (de datos) indexada
# el indice empieza a contar desde 0

lista = [1, 2, 3, 4, 5] # lista de números enteros
lista_nombres = ["Maria", "Pau", "Pol"] # lista de strings
lista_de_listas = [[1, 2], [3, 4], [5, 6]] # lista de listas
lista_mixta = [1, "Hola", True] # lista mixta

# Acceder al primer valor:

print(lista[0]) # el valor es 1

# acceder al ultimo valor

print(lista[-1]) # el valor es 5

# SLICING (atención, el último valor no esta incluido)

print(lista[1:3]) # [2, 3]
print(lista[-3:-1]) # [3, 4]