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

edades = [25, 30, 35, 40, 45, 28, 24, 76, 89, 234]
suma = 0
cantidad = len(edades)

for edad in edades:  
        suma += edad # Suma las edades que cumplen la condicion   

print(end = "\n") # Salto de linea (Recupero el original porque lo habia modificado)

print("La suma de estos numeros es : " + str(suma))
print("Hay " + str(cantidad) + " elementos")
print("El promedio de la lista es : " + str(suma / cantidad))
