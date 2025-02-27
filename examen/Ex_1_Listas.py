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
        
    """)
    opcion = input("\tTu elección es .... ")
    print("\n")    
    
    match opcion:
        case "1": # Crear la lista, indicando el número de palabras
            print("CREAR LISTA")
            print("-" * 11)

            try: # Para controlar el error si no es un numero
                cantidad = int(input("Cuantas palabras tendra la lista: "))

                # Si es mayor que 0
                if cantidad > 0:
                    # Pregunta la palabra a introducir en la lista tantas veces como se indique en cantidad
                    for num in range(cantidad):
                        # Pregunta la palabra, le quita los espacios y la pone en minusculas
                        palabra = input(f"Introduce la palabra {num + 1}: ").lower().strip()
                        lista_palabras.append(palabra) # La añade a la lista 

                    print(f"Las {num + 1} palabras se han añadido correctamente a la lista\n")
                else:
                    print("El número de palabras ha de ser mayor que 0\n")               
                
            except ValueError:
                print("Hay que introducir un número entero valido, no se pueden introducir letras\n")

            

        case "2":
            pass

        case "3": # Añadir palabra a la lista
            print("AÑADIR PALABRA A LA LISTA")
            print("-" * 25)
            # Comprueba que la lista no esta vacia
            if lista_palabras:
                

                # Pregunta la palabra, le quita los espacios y la pone en minusculas
                palabra = input("Introduce la palabra que quieres añadir a la lista: ").lower().strip()

                # La añade a la lista
                lista_palabras.append(palabra)

                print("La nueva palabra se ha añadido correctamente a la lista\n")
            else:
                print("La lista de palabras esta vacia\n")
        
        case "4": # Borrar una palabra de la lista
            print("BORRAR UNA PALABRA DE LA LISTA")
            print("-" * 30)

            # Comprueba que la lista no esta vacia
            if lista_palabras:
                pass
                
            else:
                print("La lista de palabras esta vacia\n")
        case "5": # Mostrar la lista de palabras
            print("LISTA DE PALABRAS")
            print("-" * 17)
            # Comprueba que la lista no esta vacia
            if lista_palabras:                                       
                # Recorre la lista y muestra las palabras
                for palabra in lista_palabras:
                    print(palabra)
            else:
                print("La lista de palabras esta vacia\n")

        case _: # Cualquier otra opción para salir
            continuar = False # Para que salga del bucle
