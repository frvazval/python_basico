"""
WHILE = mientras
"""
import os
os.system("cls")

# Se ejecuta mientras se cumpla una condición

# num = 5

# while num > 0:
#     print(num)
#     num -= 1
# else:
#     print("Has entrado en el else")


# num = 5

# while True:  # bucle infinito
#     print(num)
#     num -= 1

#     if num == 0:
#         break  # Sale del bucle cuando num sea 0
# else:
#     print("Has entrado en el else") # Este print no se ejecuta porque no entra en el else (por el break)


monedas = 10
while True:
    print(f"actualmente tienes {monedas} monedas\n")
    prestamo = input("¿Cuantas monedas necesitas?: ")
    

    if int(prestamo) > monedas:
        print("No hay suficientes monedas")        
    else:
        monedas -= int(prestamo)
        print(f"ahora te quedan {monedas} monedas")

    if monedas == 0: # ya no quedan más monedas
        break
     

