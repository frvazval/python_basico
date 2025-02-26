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

    Opcional:

    Hacer reservas y devoluciones de libros


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
        self.libro_y_cantidad = {} # Contiene las cantidades que hay de cada libro y los que hay disponibles
        self.libro_y_disponibles = {} # Contiene los que hay disponibles del total
        self.lector_reserva = {} # Contiene el libro que ha reservado un lector
        self.lista_reservas = [] # Contiene la lista de reservas de libros

    # Metodos de la clase Biblioteca
    def buscar_libro(self, libro_buscado: object):
        valor = False
        if self.lista_libros:
            for libro in self.lista_libros:
                if libro_buscado == libro:
                    valor = True        
        return valor 

    def mostrar_libros(self):
        if self.lista_libros: # Si la lista de libros no esta vacia
            print("Lista de libros")
            print("==========================================================================================\n")
            for libro in self.lista_libros:
                mensaje = f"Titulo: {libro.titulo}, Autor: {libro.nombre_autor} {libro.apellido_autor} Cantidad: {self.libro_y_cantidad[libro]}, "
                mensaje += f"Disponibles: {self.libro_y_disponibles[libro]}\n"               

                print(mensaje)
            print("==========================================================================================\n")
        else: # Si la lista de libros esta vacia
            print("Actualmente no hay libros disponibles en esta biblioteca\n")
        
    def mostrar_lectores(self):
        if self.lista_lectores: # Si la lista de lectores no esta vacia
            print("Lista de lectores")
            print("==========================================================================================\n")
            for lector in self.lista_lectores:
                print(f"Nombre: {lector.nombre} Apellido: {lector.apellido}\n")
            print("==========================================================================================\n")
        else: # Si la lista de lectores esta vacia
            print("Actualmente no hay lectores registrados en esta biblioteca\n")

    def mostrar_reservas(self):
        print("Lista de reservas")
        print("==========================================================================================\n")
        for reserva in self.lista_reservas:
            print(f"Libro: {reserva['libro']}, reservado por {reserva['lector']}\n")
        print("==========================================================================================\n")

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
            if self.buscar_libro(libro_nuevo):
                self.libro_y_cantidad[libro_nuevo] += cantidad
                self.libro_y_disponibles[libro_nuevo] += cantidad
                            
                return f"Libro '{libro_nuevo.titulo}' actualizado correctamente\n"
            else:
                self.libro_y_cantidad[libro_nuevo] = cantidad
                self.libro_y_disponibles[libro_nuevo] = cantidad
                self.lista_libros.append(libro_nuevo)
                return f"Libro '{libro_nuevo.titulo}' añadido correctamente\n"
            
        else: # Si la lista de libros esta vacia
            self.libro_y_cantidad[libro_nuevo] = cantidad
            self.libro_y_disponibles[libro_nuevo] = cantidad
            self.lista_libros.append(libro_nuevo)
            return f"Libro '{libro_nuevo.titulo}' añadido correctamente\n"         

    def reservar_libro(self, libro_reservado: object, lector: object):
        # Si el lector no esta registrado en la biblioteca
        if lector not in self.lista_lectores:
            return f"{lector.nombre} {lector.apellido} no puede reservar, porque no esta registrado en esta biblioteca\n"

        if self.lista_libros: # Si hay libros en la lista de libros
            if self.buscar_libro(libro_reservado): # Si el libro esta en la biblioteca
                if self.libro_y_disponibles[libro_reservado] > 0: # Si hay algun ejemplar disponible
                    self.libro_y_disponibles[libro_reservado] -= 1 # Le resta 1 a la cantidad

                    # Crea la reserva y la añade a la lista de reservas
                    self.lector_reserva = {"lector": f"{lector.nombre} {lector.apellido}", "libro": libro_reservado.titulo}
                    self.lista_reservas.append(self.lector_reserva)
                    mensaje = f"El libro '{libro_reservado.titulo}' ha sido reservado correctamente "
                    mensaje += f"por {lector.nombre} {lector.apellido}, ahora quedan {self.libro_y_disponibles[libro_reservado]} disponibles\n"
                    return mensaje
                else: # Si no hay ningún ejemplar disponible
                    return f"El libro '{libro_reservado.titulo}' no se puede reservar, porque quedan {self.libro_y_cantidad[libro_reservado]} disponibles\n"
            else: # Si el libro no esta en la biblioteca
                return f"El libro '{libro_reservado.titulo}' no se puede reservar, porque no existe en la biblioteca\n"
        else: # Si no hay libros en la lista de libros
            return f"No hay libros en la biblioteca, no se puede reservar\n"

    def devolucion_libro(self, libro_devuelto: object, lector: object):
        # Si el lector no esta registrado en la biblioteca
        if lector not in self.lista_lectores:
            return f"{lector.nombre} {lector.apellido} no puede reservar, porque no esta registrado en esta biblioteca\n"

        if self.lista_libros: # Si hay libros en la lista de libros            
            if self.buscar_libro(libro_devuelto): # Si el libro esta en la biblioteca
                self.lector_reserva = {"lector": f"{lector.nombre} {lector.apellido}", "libro": libro_devuelto.titulo}
                if self.lector_reserva in self.lista_reservas: # Si existe la reserva
                    self.libro_y_disponibles[libro_devuelto] += 1 # Añado 1 a la cantidad
                
                    # Busca la reserva en la lista para eliminarla
                    for reserva in self.lista_reservas:
                        if reserva == self.lector_reserva:
                            self.lista_reservas.remove(reserva)
                            mensaje = f"{lector.nombre} {lector.apellido} ha devuelto el libro '{libro_devuelto.titulo}' correctamente, "
                            mensaje += f"ahora quedan {self.libro_y_disponibles[libro_devuelto]} disponibles\n"
                            return mensaje 
                          
                else: # Si no existe la reserva
                    return f"{lector.nombre} {lector.apellido} no tiene el libro '{libro_devuelto.titulo}' reservado\n"                 
            else: # Si el libro no esta en la biblioteca
                return f"El libro '{libro_devuelto.titulo}' no se puede devolver, porque no pertenece a esta biblioteca\n"   
        else: # Si no hay libros en la lista de libros
            return f"No hay libros en la biblioteca, no se pueden hacer devoluciones\n"

# Creo los ojetos -> lector, libro y biblioteca
lector_1 = Lector("Antonio", "Lopez")
lector_2 = Lector("Maria", "Perez")
lector_3 = Lector("Pedro", "Martinez") # No existira en la biblioteca

libro_1 = Libro("Carlos", "Ruiz Zafón", "La sombra del viento")
libro_2 = Libro("Dolores", "Redondo", "Ofrenda a la tormenta")
libro_3 = Libro("Michael", "Ende", "La historia interminable") # No existira en la biblioteca

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

# Reserva de un libro
print(biblioteca_1.reservar_libro(libro_2, lector_1)) # Libro existente en la biblioteca
print(biblioteca_1.reservar_libro(libro_2, lector_3)) # Libro existente en la biblioteca, pero el lector no existe
print(biblioteca_1.reservar_libro(libro_3, lector_1)) # Libro que no existe en la biblioteca

# Muestro los libros para ver cuantos hay disponibles despues de las reservas
biblioteca_1.mostrar_libros()

# Muestro la lista de reservas
biblioteca_1.mostrar_reservas()

# Devolución de un libro
print(biblioteca_1.devolucion_libro(libro_2, lector_3)) # Libro existente en la biblioteca, pero el lector no esiste
print(biblioteca_1.devolucion_libro(libro_3, lector_1)) # Libro que no existe en la biblioteca
print(biblioteca_1.devolucion_libro(libro_2, lector_1)) # Libro y lector existente en la lista de reservados
print(biblioteca_1.devolucion_libro(libro_2, lector_1)) # Como ya lo ha devuelto altes, ya no existe esta reserva







