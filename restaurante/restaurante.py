"""
Vamos a gestionar restaurantes

cada uno tiene:
-- nombre
-- especialidad
-- turnos
    -- puede haber como máximo 3 clientes
    -- si se realiza la reserva diremos "Reserva realizada a [nombre_cliente]"
    -- y sino "No se ha podido realizar la reserva. prueba en otro turno"
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
        self.turnos = turnos # Es una tupla
        self.lista_clientes = []          
        self.reserva = {}  

    # Metodos       
    def hacer_reserva(self, cliente, hora):
        if self.lista_clientes:
            contador = 0
            for res_cliente in self.lista_clientes:
                if hora == res_cliente["hora"]:
                    contador += 1
            if contador < 3:
                if hora in self.turnos:
                    reserva = {"cliente": cliente, "hora": hora}
                    self.lista_clientes.append(reserva)
                    print(f"Reserva realizada a {cliente.nombre} a las {hora} horas")
                else:
                    print(f"El turno elegido (Hora: {hora}) no existe en el restaurante '{self.nombre}', elige otro turno")
            else:
                print(f"No se ha podido realizar la reserva a las {hora} horas. prueba en otro turno") 

        else:
            if hora in self.turnos:
                reserva = {"cliente": cliente, "hora": hora}
                self.lista_clientes.append(reserva)
                print(f"Reserva realizada a {cliente.nombre}  a las {hora} horas")
            else:
                print(f"El turno elegido (Hora: {hora}) no existe en el restaurante '{self.nombre}', elige otro turno")


class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre

# Creo los objetos
restaurante_1 = Restaurante("Can Pizza", "Italiana", (13, 14, 15, 20, 21, 22))
restaurante_2 = Restaurante("Casa Carmen", "De mercado", (14, 16, 20))

cliente_1 = Cliente("Antonio")
cliente_2 = Cliente("Ana")
cliente_3 = Cliente("Paco")
cliente_4 = Cliente("Maria")
cliente_5 = Cliente("Pepe")
cliente_6 = Cliente("Rosa")

restaurante_1.hacer_reserva(cliente_1, 13)
restaurante_1.hacer_reserva(cliente_2, 13)
restaurante_1.hacer_reserva(cliente_3, 23)
restaurante_1.hacer_reserva(cliente_3, 20)
restaurante_1.hacer_reserva(cliente_4, 13)
restaurante_1.hacer_reserva(cliente_5, 15)
restaurante_1.hacer_reserva(cliente_6, 13)

restaurante_2.hacer_reserva(cliente_1, 15)
restaurante_2.hacer_reserva(cliente_3, 20)
restaurante_2.hacer_reserva(cliente_6, 16)




