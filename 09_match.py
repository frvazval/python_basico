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
# si dice martes, miércoles, jueves o viernes,  diremos "Toca Python"
# si dice sábado o domingo diremos: "Es fin de semana"
# si dice otra cosa diremos: "Creo que estas confundido/a"

dia = input("Qué día de la semana es -> ").lower() # Lo convierte a minusculas antes de asignarlo a la variable dia

match dia:
    case "lunes":
        print("Toca sistemas")
    case "martes" | "miercoles" | "miércoles" | "jueves" | "viernes":
        print("Toca Python")
    case "sabado" | "sábado" |"domingo":
        print("Es fin de semana")
    case _:
        print("Creo que estás confundido/a")
        