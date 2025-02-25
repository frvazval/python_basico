"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplare disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca


"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo las clases
class Lector():
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

class Libro():
    def __init__(self, nombre_autor: str, apellido_autor: str, titulo: str):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.titulo = titulo

class Biblioteca():
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_lectores = []
        self.lista_libros = [] 
        self.libro = {}
        self.lector = {}      

    # Metodos de la clase Biblioteca
    def mostrar_libros():
        if self.lista_libros:
            for libro in self.lista_libros:
                print(f"Titulo: {libro['titulo']}, Autor: {libro['nombre']} {libro['apellido']}")
        
    def mostrar_lectores():
        if self.lista_lectores:
            for lector in self.lista_lectores:
                print(f"Nombre: {lector['nombre']} Apellido: {lector['apellido']} ")

    def agregar_lector(self, lector):
        self.lector = {"nombre": lector.nombre, "apellido": lector.apellido}
        self.lista_lectores.append(self.lector)

    def agregar_libro(self, libro):
        self.libro = {"nombre": libro.nombre_autor, "apellido": libro.apellido_autor, "titulo": libro.titulo}
        self.lista_libros.append(self.libro)

    def buscar_libro(self, libro):
        pass


# Creo los ojetos -> lector, libro y biblioteca
lector_1 = Lector("Antonio", "Lopez")
lector_2 = Lector("Maria", "Perez")

libro_1 = Libro("Carlos", "Zafón", "La sombra del viento")
libro_2 = Libro("Dolores", "Redondo", "Ofrenda a la tormenta")

biblioteca_1 = Biblioteca("Biblioteca municipal", "Av. Masnou")

# Agrego los libros a la biblioteca
biblioteca_1.agregar_libro(libro_1)
biblioteca_1.agregar_libro(libro_2)

# Agrego los lectores a la biblioteca
biblioteca_1.agregar_lector(lector_1)
biblioteca_1.agregar_lector(lector_2)

# Utilizo los metodos del objeto biblioteca

biblioteca_1.mostrar_lectores()

biblioteca_1.mostrar_libros()

