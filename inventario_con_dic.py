"""
Crea un programa que utilice un diccionario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades

"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

producto =  {}
lista_productos = []

try:
    for i in range(5):
       num_producto = int(input("Numero de producto: "))
       nombre = input("Nombre: ")
       cantidad = input("Cantidad: ")
       producto["numero"] = num_producto
       producto["nombre"] = nombre
       producto["cantidad"] = cantidad
       lista_productos.append(producto)
    print(lista_productos)

    # for i in range(2):
    #    num_producto = int(input("Numero de producto: "))
    #    nombre = input("Nombre: ")
    #    cantidad = input("Cantidad: ")
    #    producto["numero"] = num_producto
    #    producto["nombre"] = nombre
    #    producto["cantidad"] = cantidad
    #    lista_productos.append(producto)

    # print(lista_productos)

    # for prod in lista_productos:
    #     if prod["numero"] == 4:
    #         prod["cantidad"] = 40
    #     if prod["numero"] == 6:
    #         prod["cantidad"] = 60        

    # for prod in lista_productos:
    #     print(f"Num: {prod['numero']}, nombre producto: {prod['nombre']} y cantidad: {prod['cantidad']}")

    
except ValueError:
    print("Has introducido una cantidad incorrecta")