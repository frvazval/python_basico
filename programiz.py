import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Pide un número hasta que introduzca uno entre 0 y 100
continuar = True # Para salir del bucle
try:    
    while continuar:
        num = int(input("Introduce un número entero emtre 0 y 100: -> "))

        if num >= 0 and num <= 100: # El número introducido es correcto            

            for num in range(num):
                texto = str(num)                

                if num % 3:
                    texto += " - FIZZ"
                if num % 5:
                    texto += " - BUZZ"
                
                print(texto) # Imprimo el mensaje final

            continuar = False # Para que no continue pidiendo números
        else:
            print("El número es incorrecto")

except ValueError:
    print("Has de introducir un número , no se pueden introducir letras")