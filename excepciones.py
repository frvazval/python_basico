"""
EXCEPCIONES
Son errores que se producen durante la ejecución del programa y lo interrumpen
"""
import os # importa libreria os
os.system("cls") # Limpia la pantalla

# try / except
# si hay try, hay que tener except

try:
    # Intentamos ejecutar el código
    num = float(input("Escribe un número .... "))
    print( 1/0 )
except ValueError:
    print("Has de introducir un número")
except ZeroDivisionError:
    # Si se produce una excepción, división por cero
    print("No se puede dividir por cero")
except:
    # cualquier otro error
    print("Ha ocurrido un error")

print("El programa no se interrumpe")

try:
    # intenta hacer algo
    pass
except:
    # si falla ejecuta esto
    pass
else:
    # si no falla ejecuta esto
    pass
finally:
    # se ejecuta siempre
    pass
