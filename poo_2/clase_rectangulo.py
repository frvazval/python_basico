"""
Hay que crear una clase llamada Rectangulo.

Necesitamos los métodos para obtener el área, el perímetro y la diagonal de la figura.

Cada uno en un método diferente.

Lo probaremos con un rectangulo de lados 3 y 4

"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo la clase Rectangulo
class Rectangulo():
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    # Metodos de la clase
    def area(self):
        return base * altura
    def perimetro(self):
        pass
    def diagonal(self):
        pass

        