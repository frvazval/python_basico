"""
DICCIONARIOS
El acceso al dato se produce mediante un identificador
llamado "clave", así: "clave" : "valor"
La clave puede ser un string, un número, una tupla, .....
los diccionarios son mutables, se le puede cambiar el contenido

No importa el orden en el que esten puestos los datos, importa la clave
{} <-- llaves
"""

dic_1 = {} # dicionario vacio
list_1 = [] # lista vacia

if not list_1: # Se ejecutara si la lista esta vacia
    print("La lista esta vacia")

dic_1 = {"nombre": "Maria", "apellido": "Callas", "edad": 53}
print(dic_1["nombre"])

clave = "direccion"
print(dic_1.get(clave, f"la clave {clave} no existe en el diccionario")) # Para que no de error porque no existe la clave "direccion", devuelve "esta clave no existe en el diccionario"
# Si no se pone el mensaje devuelve none

# Se puede iterar por los elementos

for propiedad in dic_1: # Muestra las claves
    print(propiedad)

# Iteracion especifica de claves
# Hace lo mismo que el anterior

for propiedad in dic_1.keys():
    print(propiedad)

# iteraccion por valores

for valor in dic_1.values():
    print(valor)

# iteracion especifica de valores

for clave, valor in dic_1.items():
    print(f"{clave} : {valor}")

# Añadir un par clave-valor

dic_1["pais"] = "Grecia"
print(dic_1)

# actualizacion de datos
dic_actualizacion = {"ciudad" : "Paris", "edad" : 50}
dic_1.update(dic_actualizacion)

print(dic_1)
