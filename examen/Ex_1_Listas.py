"""
LISTAS

Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.

Mediante este menú:

        LISTA DE PALABRAS

        Elige una opción:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras

        Cualquier otra opción para salir

        Tu elección es ....

Requerimientos:

    -- Las opciones 2-3-4-5 deben verificar que existan elementos en la lista.
        Si no hay, mostrar el correspondiente mensaje.

    -- La opción 1 siempre crea una lista nueva. Por tanto elimina la
        lista anterior si existe.

    -- Cuando se pregunte cuantas palabras incluirá la lista, no hay que
        verificar que sea un número. Se asume que el usuario escribe un número.
        Lo que sí que se debe comprobar es que sea mayor a 0.

Posibles mejoras:

    -- Añadir una opción para editar una palabra en la lista.
    
    -- Añadir una opción para borrar todas las palabras de la lista.

    -- Comprobar que al pedir la cantidad de palbras de la lista, el usuario
        escribe un número entero.

    -- Y lo que se te ocurra...

  
"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Declaración de variables
continuar = True # Para salir del bucle
lista_palabras = [] # Contendra la lista de palabras
cantidad = 0 # Cantidad de palabras que contendra la lista

# Bucle para que se repita el menu, hasta que elija la opción salir
while continuar:
   
    # Muestra el menú en patalla
    print("""
    LISTA DE PALABRAS

        Elige una opción:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras

        Cualquier otra opción para salir

        Tu elección es ....
    """)
    opcion = input("Elige una opción: -> ")
    os.system("cls") # Limpia la pantalla
    match opcion:
        case "1": # Crear la lista, indicando el número de palabras
            print("CREAR LISTA")
            print("-" * 11)
            try:

            except ValueError:
                print("Hay que introducir un número entero valido, no se pueden introducir letras\n")

        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case _: # Cualquier otra opción para salir
            continuar = False # Para que salga del bucle
