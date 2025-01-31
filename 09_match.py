"""
MATCH = switch de JS o JAVA
"""

import os # importa libreria os
os.system("cls") # Limpia la pantalla

# mes = "Febrero"

# match mes:
#     case"Enero":
#         print("Ire a NY")
#     case "Febrero":
#         print("Ire a Paris")
#     case "Marzo" | "Abril" | "Mayo":
#         print("Ire a Londres")
#     case _: # Cuando no se cumple ninguna de las opciones
#         print("No se a donde ire")

# Ejercicio
# Preguntar al usuario que dia de la semana es (lunes, martes ...)
# si dice lunes diremos: "Toca sistemas"
# si dice martes, miercoles, jueves o viernes,  diremos "Toca Python"
# si dice sabado o domingo diremos: "Es fin de semana"
# si dice otra cosa diremos: "Creo que estas confundido/a"

dia = input("Qué día de la semana es -> ")
dia = dia.lower()

match dia:
    case "lunes":
        print("Toca sistemas")
    case "martes" | "miercoles" | "jueves" | "viernes":
        print("Toca Python")
    case "sabado" | "domingo":
        print("Es fin de semana")
    case _:
        print("Creo que estás confundido/a")