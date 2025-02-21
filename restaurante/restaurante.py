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

