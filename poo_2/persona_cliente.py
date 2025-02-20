"""
Vamos a crear una clase llamada Persona.

tendrá estos atributos:
-- nombre
-- apellido
-- ciudad

Crear el constructor y el método que muestra la información de la clase (print(objeto))

También Habrá una clase hija llamada Cliente.

Tendrá además los atributos:
-- dni
-- compras

Cuando se muestre el objeto deben aparecer todos los atributos.

Hay que crear un método llamado compras_realizadas que tenga esta salida:
El cliente Fulanito ha comprado xx.xx €
"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo la clase principal Persona
class Persona():
    def __init__(self, nombre: str, apellido: str, ciudad: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido} y ciudad: {self.ciudad}\n"
    
# Creo una clase heredada de Persona, llamada Cliente
class Cliente(Persona):
    def __init__(self, nombre, apellido, ciudad, dni, compras):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.ciudad = ciudad
        super().__init__(nombre, apellido, ciudad) # Rellena las propiedades del padre
        self.dni = dni
        self.compras = compras
    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, ciudad: {self.ciudad}, DNI: {self.dni} y compras {self.compras} €\n"
    def compras_realizadas():
        print(f"El cliente {self.nombre} {self.apellidos} ha comprado {self.compras} €")

# Creo un objeto de la clase Persona
persona = Persona("Maria", "Pau", "BCN")

# Creo un objeto de la clase Cliente
cliente_1 = Cliente("Pepito", "García", "Vic", "1234", 30_000)
print(cliente_1)
    