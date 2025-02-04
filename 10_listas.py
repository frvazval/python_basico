"""
lista
"""

# Las listas equivalen a los "arrays" de otros lenguajes
# Las listas y los string son "iterables" (Se pueden recorrer)
# La lista es una colección (de datos) indexada
# el indice empieza a contar desde 0

lista_numeros = [1, 2, 3, 4, 5] # lista de números enteros
lista_nombres = ["Maria", "Pau", "Pol"] # lista de strings
lista_de_listas = [[1, 2], [3, 4], [5, 6]] # lista de listas
lista_mixta = [1, "Hola", 3.5, True] # lista mixta

# Acceder al primer valor:

print(lista_numeros[0]) # el valor es 1

# acceder al ultimo valor

print(lista_numeros[-1]) # el valor es 5

# SLICING (atención, el último valor no esta incluido)
# [inicio : final : paso]

print(lista_numeros[1:3]) # [2, 3]
print(lista_numeros[-3:-1]) # [3, 4]
print(lista_numeros[-3:]) # [3, 4, 5]
print(lista_numeros[::-1]) # [5, 4, 3, 2, 1]

# añadir un elemento al final de la lista

lista_numeros.append(6) # nombre_lista.append(valor)
print(lista_numeros) # [1, 2, 3, 4, 5, 6]

# Quitar el ultimo elemento

ultimo_numero = lista_numeros.pop() # nombre_lista.pop() 
print(lista_numeros) # [1, 2, 3, 4, 5]
print(ultimo_numero)

# Poner un elemento en una posición concreta

lista_numeros.insert(2, 3) # nombre_lista.insert(valor)
print(lista_numeros)

# quitar un elemento de la lista

print(lista_nombres)
lista_nombres.remove("Pol")
print(lista_nombres)

# para eliminar por una posicion concreta

print(lista_mixta)
del lista_mixta[2]
print(lista_mixta)

# unir dos listas

lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]

lista_1.extend(lista_2)
print(lista_1)

# otra forma de hacerlo

lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]

lista_1 = lista_1 + lista_2 # tambien se puede hacer lista_1 += lista_2
print(lista_1)


