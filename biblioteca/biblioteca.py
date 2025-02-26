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
        indicando los ejemplares disponibles
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
        self.lista_lectores = [] # Contiene los lectores añadidos a la biblioteca
        self.lista_libros = [] # Contiene los libros añadidos a la biblioteca
        self.libro_y_cantidad = {} # Contiene las cantidades que hay de cada libro

    # Metodos de la clase Biblioteca
    def mostrar_libros(self):
        if self.lista_libros: # Si la lista de libros no esta vacia
            for libro in self.lista_libros:
                print(f"Titulo: {libro.titulo}, Autor: {libro.nombre_autor} {libro.apellido_autor} Cantidad: {self.libro_y_cantidad[libro]}\n")
        else: # Si la lista de libros esta vacia
            print("Actualmente no hay libros disponibles en esta biblioteca\n")
        
    def mostrar_lectores(self):
        if self.lista_lectores: # Si la lista de lectores no esta vacia
            for lector in self.lista_lectores:
                print(f"Nombre: {lector.nombre} Apellido: {lector.apellido}\n")
        else: # Si la lista de lectores esta vacia
            print("Actualmente no hay lectores registrados en esta biblioteca\n")


    def agregar_lector(self, lector_nuevo: str):
        if self.lista_lectores: # Si la lista de lectores no esta vacia
           
            if lector_nuevo in self.lista_lectores:
                return f"El lector {lector_nuevo.nombre} {lector_nuevo.apellido} no se puede añadir porque ya existe\n"
            else:
                self.lista_lectores.append(lector_nuevo) # Lo añade a la lista                
                return f"El lector {lector_nuevo.nombre} {lector_nuevo.apellido} se ha añadido correctamente\n"

        else: # Si la lista de lectores esta vacia, lo añade a la lista
            self.lista_lectores.append(lector_nuevo)       
            return f"El lector {lector_nuevo.nombre} {lector_nuevo.apellido} se ha añadido correctamente\n"

    def agregar_libro(self, libro_nuevo: object, cantidad: int):
        if self.lista_libros: # Si la lista de libros no esta vacia
            if libro_nuevo in self.lista_libros:
                self.libro_y_cantidad[libro_nuevo] += cantidad                
                return f"libro '{libro_nuevo.titulo}' actualizado correctamente\n"
            else:
                self.libro_y_cantidad[libro_nuevo] = cantidad
                self.lista_libros.append(libro_nuevo)
                return f"libro '{libro_nuevo.titulo}' añadido correctamente\n"
            
        else: # Si la lista de libros esta vacia
            self.libro_y_cantidad[libro_nuevo] = cantidad
            self.lista_libros.append(libro_nuevo)
            return f"libro '{libro_nuevo.titulo}' añadido correctamente\n"        

    def buscar_libro(self, libro_buscado: object):
        valor = f"El libro '{libro_buscado.titulo}' no existe en esta biblioteca\n"
        if self.lista_libros:
            for libro in self.lista_libros:
                if libro_buscado == libro:
                    valor = f"El libro '{libro_buscado.titulo}' si que existe en la biblioteca, \n"        
        return valor 

    def reservar_libro(self, libro_reservado: object):
        if self.lista_libros: # Si hay libros en la lista de libros
            if libro_reservado in self.lista_libros: # Si el libro esta en la biblioteca
                if self.libro_y_cantidad[libro_reservado] > 0: # Si hay algun ejemplar disponible
                    self.libro_y_cantidad[libro_reservado] -= 1 # Le resta 1 a la cantidad
                    return f"El libro '{libro_reservado.titulo}' ha sido reservado correctamente, ahora quedan {self.libro_y_cantidad[libro_reservado]} disponibles\n"
                else: # Si no hay ningún ejemplar disponible
                    return f"El libro '{libro_reservado.titulo}' no se puede reservar, porque quedan {self.libro_y_cantidad[libro_reservado]} disponibles\n"
            else: # Si el libro no esta en la biblioteca
                return f"El libro '{libro_reservado.titulo}' no se puede reservar, porque no existe en la biblioteca\n"
        else: # Si no hay libros en la lista de libros
            return f"No hay libros en la biblioteca, no se puede reservar\n"

    def devolucion_libro(self, libro_devuelto: object):
        pass  


# Creo los ojetos -> lector, libro y biblioteca
lector_1 = Lector("Antonio", "Lopez")
lector_2 = Lector("Maria", "Perez")

libro_1 = Libro("Carlos", "Ruiz Zafón", "La sombra del viento")
libro_2 = Libro("Dolores", "Redondo", "Ofrenda a la tormenta")
libro_3 = Libro("Michael", "Ende", "La historia interminable")

biblioteca_1 = Biblioteca("Biblioteca municipal", "Av. Masnou")

# Agrego los libros a la biblioteca
print(biblioteca_1.agregar_libro(libro_1, 1))
print(biblioteca_1.agregar_libro(libro_2, 1))
print(biblioteca_1.agregar_libro(libro_2, 3))

# Agrego los lectores a la biblioteca
print(biblioteca_1.agregar_lector(lector_1))
print(biblioteca_1.agregar_lector(lector_2))
print(biblioteca_1.agregar_lector(lector_1))

# Utilizo los metodos del objeto biblioteca

# Muestra todos los lectores añadidos a la biblioteca
biblioteca_1.mostrar_lectores()

# Muestra todos los libros añadidos a la biblioteca
biblioteca_1.mostrar_libros()

# Busqueda de libros, muestran si existe en la biblioteca o no existe
print(biblioteca_1.buscar_libro(libro_1))
print(biblioteca_1.buscar_libro(libro_2))
print(biblioteca_1.buscar_libro(libro_3))

# Reserva de un libro
print(biblioteca_1.reservar_libro(libro_2)) # Libro existente en la biblioteca
print(biblioteca_1.reservar_libro(libro_3)) # Libro que no existe en la biblioteca

# Devolución de un libro
print(biblioteca_1.devolucion_libro(libro_2))





