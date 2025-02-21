"""
Vamos a gestionar restaurantes

cada uno tiene:
-- nombre
-- especialidad
-- turnos
    -- puede haber como máximo 3 clientes
    -- si se realiza la reserva diremos "Reserva realizada a [nombre_cliente]"
    -- y sino "No se ha podido realizar la reserva. pruebe en otro turno"
-- clientes

Del cliente vamos a necesitar (de momento)
sólo el nombre

Ejemplo de uso:
cliente_1 = Cliente("Ana)
restarurante_1 = Restaurante("Can Pizza", "Italiana", [13, 14, 15, 20, 21, 22], )
"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Creo las clases
class Restaurante():
    def __init__(self, nombre, especialidad, turnos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.lista_clientes = []
        self.hora = None  
        self.reserva = {}  
    # Metodos
    def reservado(self):
        print(f"Reserva realizada a ")
    def no_reservado(self):
        print(f"No se ha podido realizar la reserva. pruebe en otro turno")
    def hacer_reserva(self, cliente, hora):
        if self.clientes:
            reserva = {"cliente": cliente, "hora": hora}
            self.lista_clientes.append(reserva)
        else:
            pass

class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre

# Creo los objetos

restaurante_1 = Restaurante("Can Pizza", "Italiana", (13, 14, 15, 20, 21, 22))

cliente_1 = Cliente("Antonio")

restaurante_1.hacer_reserva(cliente_1,13)

