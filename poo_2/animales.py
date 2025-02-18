import os # importa libreria os
os.system("cls") # Limpia la pantalla

class Animal():
    def __init__(self, especie):
        self.especie = especie

    def __str__(self):
        return f"La especie es {self.especie}"

class Perro(Animal): # Perro hereda de Animal
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

class Tortuga(Animal):
    pass

milu = Perro("perro")
milu.sonido()
print(milu)


silvestre = Gato("perro")
silvestre.sonido()

tortuga = Tortuga("tortuga")

print(Perro.__bases__) # de donde hereda
print(Animal.__subclasses__()) # que subclases tiene

