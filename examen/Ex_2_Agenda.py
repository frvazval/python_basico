"""
AGENDA

Escribir un programa que implemente una agenda.
Supondremos que siempre se indicarán nombres diferentes.

En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

* Añadir/modificar: Nos pide un nombre. 
    -- Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
    opcionalmente, permitir modificarlo si no es correcto, preguntando
    al usuario si quiere hacerlo. 
    -- Si el nombre no se encuentra debe añadirlo y también el teléfono correspondiente.

* Buscar: Nos pide una cadena de caracteres, 
    y nos muestras todos los contactos 
    cuyos nombres comiencen por dicha cadena.
    Por ejemplo, podemos tener contactos llamados "Mario", María", "Maria", "Mar",
    "Marta". Si buscamos "Mar" nos mostrará todos ellos. 
    Si no hay ningún contacto que comience por dicha cadena, 
    muestra el correspondiente mensaje de aviso:
    "No hay contactos que comiencen por la cadena introducida."

* Borrar: Nos pide un nombre completo y si existe nos preguntará si queremos borrarlo de la agenda. 
    Si no existe muestra el correspondiente mensaje de aviso.

* Listar: Nos muestra todos los contactos de la agenda.
    Si no hay ningún contacto, muestra el correspondiente mensaje de aviso.

* Salir, con un saludo final

Implementar el programa con un diccionario.
Como elemento de selección en el menú puedes usar letras, números o palabras completas
    (por ejemplo, "Añadir", "1", "A"), o incluso emojis.



Posibles mejoras:

* Implementar una opción en el menú que permita buscar un contacto por número de teléfono.

* Implementar el código como una función.

* Y lo que se te ocurra...

"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Definición de variables
nombre_telefono = {} # Diccionario que contendra nombre y telefono
continuar = True # Para salir del menu

# Definición de funciones
def agregar_modificar(nombre: str):
    # Compruebo que la agenda no este vacia
    if nombre_telefono:       
        if nombre in nombre_telefono:
            # Muestro el dato
            print(f"Nombre: {nombre}, Telefono: {nombre_telefono[nombre]}\n")

            # Pregunto si lo quiere modificar
            opcion = "a" # Para que entre la primera vez en el bucle
            while opcion != "s" and opcion != "n":
                opcion = input("¿Quieres modificar el telefono (s / n): ").lower()
            
            if opcion == "s":
                telefono = input("Introduce el nuevo telefono: ")
                nombre_telefono[nombre] = telefono
                return f"El telefono de '{nombre}' se ha modificado correctamente\n"
            else:
                return f"No se ha modificado nada en '{nombre}'"

    else: # Si esta vacia añado el nuevo nombre y su telefono        
        telefono = input("Introduce el número de telefono: ")
        nombre_telefono[nombre] = telefono        

        return f"El nombre '{nombre}' con el telefono '{telefono}' se ha añadido correctamente a la agenda\n"        

def buscar(nombre: str):
    pass

def borrar(nombre: str):
    pass

def listar():
    # Compruebo que el diccionario no este vacio
    if nombre_telefono:
        pass
    else:
        return "No se pueden mostrar los contactos porque la agenda esta vacia\n"

# Programa principal
# Muestro el menu mientras no se elija la opcion salir
while continuar:
    print("\tAGENDA")
    print("\t" + "-" * 6)
    print("""
    A - Añadir / Modificar
    B - Buscar
    C - Borrar
    D - Listar
          
    Para salir cualquier otra opción
          
""")
    # Pido la opción, le quito los espacios y la pongo en minusculas
    opcion = input("Elige una opción: ").lower().strip()

    match opcion:
        case "a":
            print("AÑADIR / MODIFICAR")
            print("-" * 18)

            # Pregunto el nombre que quiero añadir/modificar, (Quito los espacios y le pongo la primera letra en mayusculas)
            nombre = input("Introduce el nombre: ").strip().capitalize()

            # LLamo a la función agregar_modificar(nombre: str)
            print(agregar_modificar(nombre))

        case "b":
            pass
        case "c":
            pass
        case "d": # Listar contenido de la agenda
            print(listar())
        case _: # Salir del programa
            continuar = False

