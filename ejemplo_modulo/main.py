"""
Formas de importar un modulo
"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# importo el fichero edad.py
# import edad as ed # Importa el fichero edad.py, se pueden poner alias poniendo as nombre_alias

# y asi podemos utilizar las funciones contenidad en edad.py

# print(ed.calcula_edad("08/10/1969", "18/02/2025"))

from edad import calcula_edad # Solo importa la funcion calcula_edad

if __name__ == "__main__": # si se ejecuta desde el fichero main.py, si se importa main desde otro fichero no se podra ejecutar
    print(calcula_edad("08/10/1969", "18/02/2025")) # en este caso no hace falta poner ed.calcula_edad
    print(calcula_edad.__doc__) # Muestra los comentarios de la función
