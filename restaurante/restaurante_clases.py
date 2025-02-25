"""
Vamos a gestionar resturantes

Cada uno tiene:
-- nombre
-- especialidad
-- turnos:
    -- Puede haber como máximo 3 clientes
    -- si se realiza la reserva diremos "Reserva realizada a [nombre_cliente]"
    -- y si no "No se ha podido realizar la reserva. pruebe en otro turno"
-- clientes

Del cliente vamos a necesitar (de momento)
sólo el nombre

Ejemplo de uso:
cliente_1 = Cliente("Anna")
restaurante_1 = Restaurante("Can Pizza", "Italiana", [13, 14, 15, 20, 21, 22])

"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre

ana = Cliente("Ana")
saludo = "hola"

class Restaurante():
    '''Restaurante: nombre, especialidad, turnos'''
    def __init__(self, nombre: str, especialidad: str, turnos: tuple):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        # Atributo añadido para controlar los turnos
        self.reservas = {}
        for turno in turnos:
            self.reservas[turno] = 0 # pone todos los turnos a cero

    # Metodo para reservar
    def reservar(self, cliente, hora_reserva):
        # Comprobar si la hora solicitada esta en los turnos disponibles
        if hora_reserva not in self.turnos:
            tupla_turnos = [ str(turno) for turno in self.turnos] # Guarda los turnos en una tupla en formato string para mostrarlo en el mensaje
            mensaje = f"Lo sentimos, no es posible la reserva a las {hora_reserva}\n"
            mensaje +=  f"Horarios disponibles: " + ", ".join(tupla_turnos) + " horas." # muestra los turnos de la tupla
            return mensaje
        # Comprobar las reservas anteriores
        if self.reservas[hora_reserva] < 3:
            self.reservas[hora_reserva] += 1
            return  f"Reserva confirmada a las {hora_reserva} para el cliente {cliente.nombre}"
        else:
            return f"Lo sentimos, no es posible reservar a las {hora_reserva}"  

napoli = Restaurante("Napoli", "Italiana", (12, 13, 14, 15, 20, 21, 22))

print(napoli.__doc__) # Muestra el comentario
print(napoli.__dict__) # Muestra el contenido

print(napoli.reservar(ana, 14))
print(napoli.reservar(ana, 14))
print(napoli.reservar(ana, 14))
print(napoli.reservar(ana, 14))
