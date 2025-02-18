"""
EJERCICIO 1 : SUMA DE VALORES
Haz un programa que pida al usuario dos números para sumarlos.
La respuesta del programa será:
"La suma de los dos números es XX" (el valor que sea)
"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    print(f"La sumade  {num1} y {num2} es {num1 + num2}")

except ValueError:
    print("No has introducido un número entero valido")