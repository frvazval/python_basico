import os # importa libreria os
os.system("cls") # Limpia la pantalla

class Animal():
    pass

class Perro(Animal): # Perro hereda de Animal
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

milu = Perro()
milu.sonido()
silvestre = Gato()
silvestre.sonido()

print(Perro.__bases__) # de donde hereda
print(Animal.__subclasses__()) # que subclases tiene

