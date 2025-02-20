'''
Crea una clase llamada Vehiculo.

En su constructor incluye marca, modelo y año de construcción.

Dos métodos también:
-- arrancar, con el mensaje "El vehículo XX modelo YY ha arrancado"
-- detener, con el mensaje "El vehículo XX modelo YY se ha detenido"

Luego, dos clases hijas: Coche y Moto

La clase Coche tiene dos atributos propio: numero de puertas y AC (verdadero o falso).
y también un método propio: abrir_maletero, que
devuelve este mensaje: "El maletero del [marca] [modelo] está abierto"

La clase Moto tiene un método propio: revisar_seguridad, devuelve este mensaje:
"Si circulas en motocicleta debes llevar casco"
'''
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo la clase Vehiculo
class Vehiculo():
    def __init__(self, marca, modelo, any_const):
        self.marca = marca
        self.modelo = modelo
        self.any_const = any_const
    # Metodos
    def arrancar(self):
        print(f"El vehículo {self.marca} modelo {self.modelo} ha arrancado")
    def detener(self):
        print(f"El vehículo {self.marca} modelo {self.modelo} se ha detenido")

# Creo las clases hijas Coche y Moto
class Coche(Vehiculo):
    def __init__(self, marca, modelo, any_const, num_puertas, AC):
        super().__init__(marca, modelo, any_const)
        self.num_puertas = num_puertas
        self.AC = AC
    
    # Metodos
    def abrir_maletero(self):
        print(f"El maletero del {self.marca} {self.modelo} está abierto")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, any_const):
        super().__init__(marca, modelo, any_const)
    def revisar_seguridad(self):
        print("Si circulas en motocicleta debes llevar casco")

# Programa principal, creo objetos de ñlas clases

coche_1 = Coche("SEAT", "Leon", 2000, 5, True)
moto_1 = Moto("Honda", "SH", 2010)

coche_1.arrancar()
coche_1.detener()

moto_1.revisar_seguridad()
moto_1.arrancar()
moto_1.detener()

