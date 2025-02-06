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

if len(palabra_1) == len(palabra_2): # Si tienen la misma longitud puede ser un anagrama
    pass
else:  # Si no tienen la misma longitud, no puede ser un anagrama
    pass

