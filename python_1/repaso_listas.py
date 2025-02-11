"""
REPASO LISTAS
"""
# Lista vacia
lista = []

lista.append("Anna")

print(lista) # devuelve : ["Anna"]

# Las listas son colecciones de datos indexados
# el indice empieza por 0

lista[0]

# hacemos un casting de range a list

lista_enteros = list(range(1,21,2))
print(lista_enteros)

lista_nombres = ["Pol", "Noa", "Sara", "Pepe"]

for nombre in lista_nombres:
    indice = lista_nombres.index(nombre) 
    print(f"{indice}. {nombre}")

for indice, valor in enumerate(lista_nombres):
    print(f"{indice}. {valor}")

# Copia de una lista

nueva_lista_1 = lista_nombres.copy()
nueva_lista_2 = lista_nombres[:]

# Mini ejercicio: obtener los números elevados al cuadrado de la serie

lista_numeros = list(range(0, 11)) # Hay que obtener --> 0, 1, 4, 9, ...
print(lista_numeros) # muestra los números de la lista

# necesitamos otra lista sólo con los números elevados al cuadrado de lista_numeros

lista_num_cuadrado = [] # Contendra la lista de números al cuadrado

for numero in lista_numeros:
    lista_num_cuadrado.append(numero * numero)

print(lista_num_cuadrado) # Muestra los números al cuadrado