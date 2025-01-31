"""
MATCH = switch de JS o JAVA
"""

mes = "Febrero"

match mes:
    case"Enero":
        print("Ire a NY")
    case "Febrero":
        print("Ire a Paris")
    case "Marzo" | "Abril" | "Mayo":
        print("Ire a Londres")
    case _: # Cuando no se cumple ninguna de las opciones
        print("No se a donde ire")
