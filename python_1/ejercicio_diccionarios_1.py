"""
EJERCICIO DICCIONARIOS

Tenemos un sitio que registra los accesos de los usuarios.

Necesitamos un menú con estas opciones
1. Añadiremos un usuario (Si no existe ya)
2. Añadiremos una visita al usuario indicado (si el usuario no existe mostrar error)
3. Mostraremos las visitas del usuario que se decida (si el usuario no existe mostrar error)
4. Mostraremos las visitas de todos los usuarios (si no hay usuarios todavia indicarlo)
X. Salir

Hazlo como quieras
"""
import os # importa libreria os 
os.system("cls") # Limpia la pantalla

salir = False
dic_usuario = {} # Diccionario de usuarios vacio
lista_usuarios = [] # Guardara los diccionarios de usuarios

while not salir:           
    print("1. Añadir un usuario")
    print("2. Añadir visita a un usuario")
    print("3. Mostrar visitas de un usuario")
    print("4. Mostrar visitas de todos los usuarios")
    print("X. Salir")
    print()
    
    opcion = input("Elige una opción: ").strip().title() # Le quito los espacios y pongo la primera letra en mayusculas

    match opcion:
        case "x" | "x": # Salir
            salir = True
            print("Salimos del programa")
        case "1": # añadir usuario            
            nombre = input("Nombre del nuevo usuario: ")

            if lista_usuarios: 
                for usuario in lista_usuarios:
                    if usuario["nombre"] == nombre:
                        print("El usuario ya existe")
                    else:
                        dic_usuario = {"nombre" : nombre, "visitas": 0} 
                        lista_usuarios.append(dic_usuario)                
            else:             
                 dic_usuario = {"nombre" : nombre, "visitas": 0} 
                 lista_usuarios.append(dic_usuario)                
        case "2": # añadir visita
            pass
        case "3": # mostrar visita
            pass
        case "4": # mostrar todas las visitas
            if lista_usuarios:
                print(lista_usuarios)
            else:
                print()
                print("Aun no existen usuarios")
                print()
        case _: # opción incorrecta
            print()
            print(f"La opción {opcion} elegida es incorrecta")
            print()
   
    