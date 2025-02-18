"""
Formas de importar un modulo
"""
# importo el fichero edad.py
# import edad as ed # Importa el fichero edad.py, se pueden poner alias poniendo as nombre_alias

# y asi podemos utilizar las funciones contenidad en edad.py

# print(ed.calcula_edad("08/10/1969", "18/02/2025"))

from edad import calcula_edad # Solo importa la funcion calcula_edad

if __name__ == "__main__": # si se ejecuta desde el fichero main.py
    print(calcula_edad("08/10/1969", "18/02/2025")) # en este caso no hace falta poner ed.calcula_edad

