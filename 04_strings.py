
# SON LAS CADENAS DE TEXTO

# string_1 = 'Hola'
# string_3 = "Hola"
# string_3 = """Hola"""


# Mini ejercicio
# nombre =
# apellido =
# edad =
# frase =

# Para obtener datos de usuario
"""
nombre = input("Escribe tu nombre -> ")
apellido= input("Escribe tu apellido -> ")
edad = input("Escribe tu edad -> ")

"""
frase = "Esto es una frase larga"


print("frase[0] -> ", frase[0]) # Primer caracter
print("frase[-1] -> ", frase[-1]) # ultimo caracter
print("frase[0:6] -> ", frase[0:6]) # 6 primeros caracteres, tambien se puede poner frase[:6]
print("frase[-6:] -> ", frase[-6:]) # 6 ultimos caracteres

# caracteres en posición par , frase[:] = todo

print("frase[::2] -> ", frase[::2])

# Invertir frase

print("frase[::-1] -> ", frase[::-1])

# Cuantos caracteres hay en un string

print("frase tiene " + str(len(frase)) + " caracteres")

# Convertir texto a mayusculas

print(frase.upper())

# Convertir el texto a minusculas

print(frase.lower())

# empezar el string con mayusculas

print(frase.capitalize())

# Contar caracteres

# Cuantas a hay en mi texto

print(frase.count("a")) # Sensible a mayusculas y minusculas

# Encontrar la posicion de un caracter o grupo de caracteres, si no existe devuelve -1

print(frase.find("a"))

# verificar si un string cumple una condicion
# verificar si el texto empieza por un caracter o grupo de caracteres concreto

print(frase.startswith("Esto"))

print(frase.endswith("larga")) # mira si termina con un conjunto de caracteres

# Verificar si el texto es convertible a numero

numero = "10"
print(int(numero))

print(numero.isnumeric()) # si es numerico

print(numero.isalpha()) # si es solo texto

print(numero.isalnum()) # si es alfanumerico, numeros y letras

# Cambiar caracteres en un string

print(frase.replace("a", "i"))

# Cuantas palabras tiene un estring

palabras_en_frase = frase.split(" ")
print(len(palabras_en_frase))

# Mini ejercicio

texto = "bUeNos dÍAs" # Buenos días
texto = texto.lower()

print(texto.capitalize())

# Compara palabras, para orden alfabetico

print("abeja" > "flor") # es False porque la a va antes

