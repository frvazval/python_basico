import os # importa libreria os
os.system("cls") # Limpia la pantalla

# nombre = "Francisco"
# apellido = "Vázquez"
# edad = 55

# # Se puede hacer de varias formas

# print("Me llamo " + nombre + " " + apellido + " y tengo " + str(edad) + " años")

# print(f"Me llamo {nombre} {apellido} y tengo {edad} años")

# print("Me llamo {} {} y tengo {} años".format(nombre, apellido, edad))

# Ejercicio:
# Comprobar si un texto es un palindromo, (es igual leida al derecho y al reves)

frase = input("Introduce una frase -> ").strip().lower() # Le quita los espacios del principio y del final y lo pasa a minúsculas
frase = frase.split(" ") # lo separa por los espacios
frase = "".join(frase)   # junta todas las palabras sin espacios
if frase == frase[::-1]:
    print("Esta frase es un palindromo")
else:
    print("Esta frase no es un palindromo")
