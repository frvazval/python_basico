"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
. 
"""

# Ejercicio 2a
# ============

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

print("Contar letras en un texto")
print("=========================")
print()

texto = input("Por favor, introduzca un texto (Puede contener números y caracteres con tilde) -> ").lower() # Pide un texto al usuario, ya lo guarda en minúsculas

caracteres_ign = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "¡", "!", "¿", "?", ".", ",", ":", ";", ] # lista de caracteres a ignorar
letras_diferentes = [] # Lista que contendra las diferentes letras
num_letras = len(texto) # numero de caracteres que tiene la cadena

print()
print("El texto contiene las letras:")
print("=============================")
print("Ignoraremos los números, los espacios y los signos de puntuación")
print("(punto, coma, punto y coma, exclamación, etc.)")
print("Consideremos mayúsculas y minúsculas como la misma letra.")
print("=========================================================")
print()

for posicion in range(num_letras): # Recorro toda el texto

    # Si no es un caracter que hay que ignorar
    if texto[posicion] not in caracteres_ign:
        if texto[posicion] not in letras_diferentes: # Si no esta en la lista de letras diferentes la añado
            letras_diferentes.append(texto[posicion])
        
# Ordenos las letras diferentes por orden alfabetico
letras_diferentes.sort()

for letra in range(len(letras_diferentes)):
    caracter = letras_diferentes[letra] # Guarda cada caracter le la lista para mostrarlo
    cantidad = texto.count(letras_diferentes[letra]) # Cuenta cuantas hay de cada letra en el texto
    
    # Si la cantidas es 1 pongo "vez" y si no pongo "veces"
    if cantidad == 1:
        print(f"{caracter}, {cantidad} vez")
    else:
        print(f"{caracter}, {cantidad} veces")

# Ejercicio 2b
# ============

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

print("Contar palabras en un texto")
print("===========================")
print()

# Pide un texto al usuario, ya lo guarda en minúsculas y sin espacios al principio ni al final
texto = input("Por favor, introduzca un texto (Puede contener números y caracteres con tilde) -> ").strip().lower()
texto2 = "" # uardara la frase correcta, sin los caracteres ignorados

palabras = [] # Guardara las palabras del texto2
palabras_diferentes =  []

# lista de caracteres a ignorar, en este caso no pòngo el " " para poder separar las palabras después
caracteres_ign = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "¡", "!", "¿", "?", ".", ",", ":", ";", ]  

# Elimino del texto todos los caracteres no validos, menos el espacio
for letra in texto:
    if letra not in caracteres_ign:
        texto2 += letra # va añadiendo las letras a la cadena texto2


print()
print("El texto contiene las palabras:")
print("===============================")
print("Ignoraremos los números, los espacios y los signos de puntuación")
print("(punto, coma, punto y coma, exclamación, etc.)")
print("Consideremos mayúsculas y minúsculas como la misma letra.")
print("=========================================================")
print()

palabras = texto2.split(" ") # lo separa por los espacios, asi obtenemos las diferentes palabras

for palabra in palabras:
    if palabra not in palabras_diferentes:
        palabras_diferentes.append(palabra) # Guarda las palabras diferentes

# Ordenos afabeticamente las palabras diferentes
palabras_diferentes.sort()

# Cuenta cuantas palabras hay de cada una
for valor in palabras_diferentes:
    cantidad = texto2.count(valor) # Guarda cuantas veces se repite la palabra en el texto

    # Si la cantidas es 1 pongo "vez" y si no pongo "veces"
    if cantidad == 1:
        print(f"{valor}, {cantidad} vez")
    else:
         print(f"{valor}, {cantidad} veces")

