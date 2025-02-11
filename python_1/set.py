"""
SET -> conjunto lógico
Los sets no pueden tener valores repetidos
"""

lista_numeros = [1, 2, 2, 5, 7, 5, 4, 1]
lista_sin_repeticiones = list(set(lista_numeros)) # lista[]
lista_sin_repeticiones = set(lista_numeros) # set{}

print(lista_sin_repeticiones)
