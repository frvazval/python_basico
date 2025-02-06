# Tenemos esta lista de animales:
# ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]

# Vamos a pedir una letra al usuario y mostraremos los animales que contienen esa letra.
# Si no hay ninguno diremos "Ningún animal contiene esa letra"

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

animales = ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]
existe = False

print("La lista de animales es: ['gato', 'perro', 'caballo', 'paloma', 'murcielago', 'leon', 'mono']")

letra = input("Introduce una letra: ")

# muestra los animales de la lista que contienen la letra introducida

print("Los animales de la lista que contienen la letra '" + letra + "' son:")

for animal in animales:
    if letra in animal:
        print(animal)
        existe = True # Si lo ha encontrado

if existe == False: # Si no lo ha encontrado
    print("Ningún animal contiene esa letra")
