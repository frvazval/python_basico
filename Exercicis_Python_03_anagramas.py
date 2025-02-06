"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

print("Anagramas")
print("=========")
print()

# Guardo las palabras en las variables "palabra_1" y "palabra_2", las guardo en minúsculas
palabra_1 = input("Introduce la primera palabra -> ").lower()
palabra_2 = input("Introduce la segunda palabra -> ").lower()


# Comprueba si la palabra 2 es un anagrama de la palabra 1

if len(palabra_1) != len(palabra_2): # Si no tienen la misma longitud no puede ser un anagrama
    es_anagrama = False
else:  # Si no tienen la misma longitud, no puede ser un anagrama
    # Creo dos listas, cada una con las letras de cada palabra ordenada alfabeticamente
    es_anagrama = True
    letras_1 = []
    letras_2 = []

    for letra in palabra_1:
        letras_1.append(letra)

    for letra in palabra_2:
        letras_2.append(letra)

    letras_1.sort()
    letras_2.sort()

    # Compruebo las dos listas letra a letra

    for posicion in range(len(letras_1)):
        if letras_1[posicion] != letras_2[posicion]:
            es_anagrama = False
            break

if es_anagrama:
    print("Son anagramas --> Sí")
else:
    print("Son anagramas --> No")

