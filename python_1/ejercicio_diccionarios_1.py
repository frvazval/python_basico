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
    
    opcion = input("Elige una opción: ").strip() # Le quito los espacios

    match opcion:
        case "x" | "X": # Salir
            salir = True
            print("Salimos del programa")
        case "1": # añadir usuario            
            nombre = input("Nombre del nuevo usuario: ").strip().title() # Quita los espacios y pone la primera en mayusculas

            if lista_usuarios: # Si la lista de usuarios no esta vacia

                # Guardo los usuarios existentes en una lista auxiliar
                nombres_existentes = []
                for nombre_usuario in lista_usuarios:
                    nombres_existentes.append(nombre_usuario["nombre"])
                
                # Si el nombre introducido no existe
                if nombre not in nombres_existentes:
                    # Lo añado a un diccionario y este a la lista "lista_usuarios"
                    dic_usuario = {"nombre" : nombre, "visitas" : 0}
                    lista_usuarios.append(dic_usuario)  
                    print(f"Usuario {nombre} añadido correctamente")
                else:
                    print(f"El usuario {nombre} no se puede añadir porque ya existe")                                                      

            else:             
                 dic_usuario = {"nombre" : nombre, "visitas": 0} 
                 lista_usuarios.append(dic_usuario)
                 print(f"Usuario {nombre} añadido correctamente")                
        case "2": # añadir visita          

            # Si la lista esta vacia no se pueden añadir visitas
            if lista_usuarios:
                # Si existen usuarios pido el nombre le quito los espacios y le pongo la primera en mayusculas
                nombre = input("Nombre del nuevo usuario para añadir visita: ").strip().title()

                # Guardo los nombres existentes en la lista auxiliar
                nombres_existentes = []
                for nombre_usuario in lista_usuarios:
                    nombres_existentes.append(nombre_usuario["nombre"])

                # Compruebo si el usuario introducido existe en la lista
                if nombre in nombres_existentes:
                    for nom in lista_usuarios:
                        if nom["nombre"] == nombre:
                            nom["visitas"] += 1 # Añado una visita a las existentes
                            print(f"Se ha añadido correctamente la visita al usuario {nombre}")
                else:
                    print(f"No se pueden añadir visitas al usuario {nombre} porque no existe")
                
            else:
                print("No exite ningún usuario en la lista")
        case "3": # mostrar visita
            pass
        case "4": # mostrar todas las visitas
            if lista_usuarios:
                for u in lista_usuarios:
                    print(u)
            else:
                print()
                print("Aun no existen usuarios")
                print()
        case _: # opción incorrecta
            print()
            print(f"La opción {opcion} elegida es incorrecta")
            print()
   
    