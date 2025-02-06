# El usuario introduce un número entero, como máximo 100
# ese número es el límite
# Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números
# Pero...
# -- Si el número es multiplo de 3, escribiremos 3 - FIZZ
# -- Si el número es multiplo de 5, escribiremos 5 - BUZZ
# -- Si el número es multiplo de 3 y de 5, escribiremos 3 - FIZZ-BUZZ
# -- En los demás casos sólo el número
# -- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Pide un número hasta que introduzca uno entre 0 y 100
continuar = True # Para salir del bucle
try:    
    while continuar:
        num = int(input("Introduce un número entero emtre 0 y 100: -> "))

        if num >= 0 and num <= 100: # El número introducido es correcto            

            for num in range(num + 1):
                texto = str(num)                

                if num % 3 == 0 and num % 5 == 0 and num != 0:
                    texto += " - FIZZ-BUZZ"
                elif num % 3 == 0 and num != 0:
                    texto += " - FIZZ"
                elif num % 5 == 0 and num != 0:
                    texto += " - BUZZ"
                
                print(texto) # Imprimo el mensaje final

            continuar = False # Para que no continue pidiendo números
        else:
            print("El número es incorrecto")

except ValueError:
    print("Has de introducir un número , no se pueden introducir letras")
