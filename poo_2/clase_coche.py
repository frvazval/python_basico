"""
Crear una clase llamada Coche

Tendrá los siguientes atributos:
-- marca
-- color
-- combustible
-- cilindrada

Crear la función __init__ con los parámetros anteriores.

Crear otra función llamada "mostrar_caracteristicas" que muestre todos los detalles anteriores en un único mensaje.

Crear la función __str__ que tendrá como salida la marca y el color.

Con eso crearemos un objeto Coche, con estos valores:
-- Opel
-- rojo
-- electrico
-- 1.6

Ejecutar las funciones que acabas de crear.
"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo la clase coche
class Coche():
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    def __str__(self):
        return f"Es de la marca {self.marca} y su color es {self.color}\n"
    def mostrar_caracteristicas(self):
        return f"marca: {self.marca}, color: {self.color}, combustible: {self.combustible} y cilindrada {self.cilindrada}\n"
    


# Creo un objeto de la clase Coche
coche = Coche("Opel", "rojo", "electrico", 1.6)
