# Vamos a pedir un número entero al usuario
# Con el imprimiremos la tabla de multiplicar del 1 al 10

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Pido un número entero al usuario y lo guardo en num
num = input("Escribe un número: ")

# Paso de string a número
num = int(num)

# Calculo la tabla de multipluicar del 1 al 10
for n in range(1, 11, 1): # Desde la posicion 1 hasta 10 (11 - 1)
    print(f"{num} * {n} = {num * n}")
