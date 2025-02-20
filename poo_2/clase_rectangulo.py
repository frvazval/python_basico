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
    # Metodos de la instancia
    def area(self): 
        return self.base * self.altura
    def perimetro(self):
        return (self.base + self.altura) * 2
    def diagonal(self):
        return (self.base ** 2 + self.altura ** 2) ** 0.5

# Creo un objeto del tipo Rectangulo

rectangulo = Rectangulo(3,4) 
print(f"Area = {rectangulo.area()}")
print(f"Perimetro = {rectangulo.perimetro()}")
print(f"Diagonal = {rectangulo.diagonal()}")
