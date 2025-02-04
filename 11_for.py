"""
for 
"""

import os
os.system("cls")

# nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
# edades = [25, 30, 35, 40, 45]


# Para cada nombre en nombres ....
# Mostrar los nombres que empiezan por "p"

# for nombre in nombres:
#     if nombre[0] == "P" or nombre[0] == "p": # muestra solo los que empiezan por "p"
#         print(nombre)

# print("===================")

# También se podria hacer asi
# check = "p"
# for nombre in nombres:
#     # Comprobar si empieza por "p"
#     if nombre.lower().startswith(check.lower()):
#         print(nombre)


# print("===================")

# Ejercicio 1
# Mostrar los numeros de esta lista que empiecen por 2

# edades = [25, 30, 35, 40, 45, 28, 24, 76, 89, 234]
# check = 2
# suma = 0
# cantidad = 0

# for edad in edades:
#     if str(edad).startswith(str(check)): # Lo convierto en string y despues miro si el primer caracter es "2"
#         print(edad, end=" ") # end=" " -> significa que ponga un espacio y no haga el salto de linea
#         suma += edad # Suma las edades que cumplen la condicion
#         cantidad += 1

# print(end = "\n") # Salto de linea (Recupero el original porque lo habia modificado)

# print("La suma de estos numeros es : " + str(suma))
# print("Hay " + str(cantidad) + " elementos")
# print("El promedio de la lista es : " + str(suma / cantidad))

# Ejercicio
# Mostrar el resultado así : 

# la suma de los elementos es X
# hay X elementos
# el promedio de la lista es X

# edades = [25, 30, 35, 40, 45, 28, 24, 76, 89, 234]
# suma = 0
# cantidad = len(edades)

# for edad in edades:  
#         suma += edad # Suma las edades que cumplen la condicion   

# print(end = "\n") # Salto de linea (Recupero el original porque lo habia modificado)

# print("La suma de estos numeros es : " + str(suma))
# print("Hay " + str(cantidad) + " elementos")
# print("El promedio de la lista es : " + str(suma / cantidad))

# quiero saber si un nombre esta en la lista

nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
nombre_a_buscar = "Luis"

# "Luis" esta en la lista
# "Alba" no esta en la lista

# for nombre in nombres:
#     if nombre.lower() == nombre_a_buscar.lower():
#         print(f"{nombre} esta en la lista")
#         break # Finaliza el bucle
# else:
#     print(f"{nombre_a_buscar} no esta en la lista") # Se ejecuta en el caso de que no se ejecute el break
    
# Quiero saber que nombres de la lista contienen la letra "o" y guardarlo en otra lista

nombres_con_o = []

for nombre in nombres:
    indice = nombres.index(nombre) # Guarda el indice de nombre
    if "o" in nombre.lower():
        print(f"{indice + 1}. {nombre}") # el + 1 es para que marque la posición desde el 1
        nombres_con_o.append(nombre)

print(nombres_con_o)

print(range(10))       # Muestra el rango
print(list(range(10))) # Muestra la lista

for num in range(10): # lo hace 10 veces
    print(num)

# recorre la lista por los indices

for indice in range(len(nombres)):
    print(f"{indice} {nombres[indice]}")