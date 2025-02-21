
"""
Crea un programa que utilice un inventario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades

"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo un inventario con 5 productos
inventario = {"manzanas": 10, "peras": 15, "kiwis": 5, "limones": 4, "naranjas": 7}

# añado dos elementos más al inventario
inventario["piñas"] = 3
inventario["tomates"] = 5

print(inventario)

# Modificar la cantidad
inventario["naranjas"] = 4

# incrementar una cantidad
inventario["kiwis"] +=2

print(inventario)

# Quitar un elemento
fruta = inventario.pop("peras") # guarda el valor de peras en fruta, quita el elemento del diccionario

print(fruta)
print(inventario)

inventario.popitem() # Quita el ultimo elemento
print(inventario)

# Ordenar alfabeticamente el diccionario
for producto in sorted(inventario): # el inventario no se modifica, solo lo ordena alfabeticamente momentaneamente
    print(f"producto: {producto}")
    
