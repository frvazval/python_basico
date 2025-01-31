"""
IF / ELIF / ELSE
Control de condiciones

"""

llueve = True

if llueve:
    print("Cogeré el paraguas")
else:
    print("iré a pasear")

print("Resto del código")

lunes = False # Los lunes como pizza
jueves = True # Los jueves paella

# El resto de días un bocadillo

if lunes:
    print("Toca pizza")
elif jueves:
    print("Toca paella")
else:
    print("Toca bocadillo")

# Ejercicio:
# preguntar la edad al usuario
# si tiene menos de 12 años -> eres un niño/a
# si tiene menos de 18 años -> eres un/a adolescente
# si tiene menos de 30 años -> eres muy joven
# si tiene menos de 40 -> eres joven, pero menos
# si tiene más -> tu puedes con todo

# edad = input("Cual es tu edad -> ")
# edad = int(edad) # Convierto a entero, porque el input recoge un string
# if edad > 0:
#     if edad < 12:
#         print("Eres un niño/a")
#     elif edad < 18:
#         print("Eres un/a adolescente")
#     elif edad < 30:
#         print("Eres muy joven")
#     elif edad <= 40:
#         print("Eres joven, pero menos")
#     elif edad < 120:
#         print("Tu puedes con todo")
#     else:
#         print("No me lo creo")
# else:
#     print("Edad incorrecta")

# si aun no se sabe lo que va en el bloque de la condición se puede poner dentro la palabra pass, para que no de error por estar vacio

# Preguntar al usuario la edad
# Si tiene menos de 0 o más de 129 diremos : no me lo creo
# si tiene menos de 18 diremos : aun no puedes votar, te faltan x años
# si tiene 18 o más, diremos : puedes votar desde hace x años

# edad = int(input("Cual es tu edad ->"))

# if edad < 0:
#     print("No me lo creo")
# else:
#     if edad > 129:
#         print("No me lo creo")
#     elif edad < 18:
#         print("Aun no puedes votar, te faltan " + str(18 - edad) + " años")
#     else:
#         print("Puedes votar desde hace " + str(edad - 18) + " años")


# Ejercicio
# Pedir al usuario un número
# pedir otro número
# si no son numeros le diremos que no se puede hacer y finalizara el programa
# pedir que operadión matematica quiere hacer (7 posibilidades)
# pero si no es ninguna de estas mostraremos un mensaje de error
#   suma
#   resta
#   multi
#   division
#   exp
#   div_ent
#   modulo
# pero si no es ninguna de estas mostraremos un mensaje de error

# Al final debe aparecer algo así :
# Escribe el primer úmero -> 1
# Escribe el primer úmero -> 3
# ¿Qué operación quieres realizar -> suma
# 1 + 3 = 4

import os # importa libreria os
os.system("cls") # Limpia la pantalla

try:
    num1 = float(input("Escribe el primer número -> "))
    num2 = float(input("Escribe el segundo número -> "))
       
    operacion = input("¿Que operación quieres realizar? -> ")
    if operacion == "suma":       
        print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    elif operacion == "resta":
        print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    elif operacion == "multi":
        print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
    elif operacion == "division":             
        print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))    
    elif operacion == "exp":
        print(str(num1) + " ** " + str(num2) + " = " + str(num1 ** num2))
    elif operacion == "div_ent":        
        print(str(num1) + " // " + str(num2) + " = " + str(num1 // num2))       
    elif operacion == "modulo":        
        print(str(num1) + " % " + str(num2) + " = " + str(num1 % num2))      
    else:
        print("La operación introducida no es valida")    
except ZeroDivisionError:
    print("Error, no se puede dividir por cero")
except ValueError:
    print("El valor introducido no es un número valido")
except:
    print("Se ha producido un error indeterminado")



