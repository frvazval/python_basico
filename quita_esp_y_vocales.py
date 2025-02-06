# Vamos a recibir un texto por parte del usuario.
# Con ese texto vamos a generar otro sin las vocales ni los espacios

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Guardo el texto en una variable
texto = input("Escribe un texto: ")

# En texto_2 guardare el texto sin vocales ni espacios
texto_2 = ""
vocales = ["a", "e", "i", "o", "u"]

for caracter in texto:
    if caracter != " " and caracter.lower() not in vocales:
        texto_2 += caracter

print("El texto introducido, sin vocales y espacios es:")
print("================================================")
print()
print(texto_2)
