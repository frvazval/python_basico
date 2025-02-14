"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar
el proceso sin que se produzca la compra

"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# definición de variables, listas, etc...
entradas_compradas = [] # para guardar todas las entradas compradas
PR_ESTANDAR = 9.00
PR_SENIOR = 6.00
PR_INFANTIL = 7.20
PR_DIA_ESPECTADOR = 5.00

salir = False
acomp_adulto = False

# Definicion de funciones
def mostrar_precios():
    print("Hay tres precios:")
    print("=================")
    print("1 - Entrada estandar: 9.00")
    print("2 - Mayores de 65 años (seniors) : 6.00")
    print("3 - Infantiles : 7.20") 
    print("4 - Día del espectador : 5.00") 
    print("5 - Terminar compra")
    print("6 - Salir sin comprar\n")
                

def comprar_entradas(tipo, cant):  # añade entradas compradas a la lista   
    dic_entradas_compradas = {"tipo" : tipo, "cantidad" : cant} # para ir añadiendo nuevas entradas a la lista
    entradas_compradas.append(dic_entradas_compradas) # añade el diccionario a la lista         

def mostrar_total():
    total = 0
    ent_estandar = 0
    ent_senior = 0
    ent_infantil = 0
    ent_dia_esp = 0

    # Lee los valores de la lista
    for entrada in entradas_compradas:
        match entrada["tipo"]:
            case 1:
                ent_estandar += entrada["cantidad"]
                total += (PR_ESTANDAR * entrada["cantidad"])
            case 2:
                ent_senior += entrada["cantidad"]
                total += (PR_SENIOR * entrada["cantidad"])
            case 3:
                ent_infantil += entrada["cantidad"]
                total += (PR_INFANTIL * entrada["cantidad"])
            case 4:
                ent_dia_esp += entrada["cantidad"]
                total += (PR_DIA_ESPECTADOR * entrada["cantidad"])
            case _:
                print("\nNo es un tipo de entrada valido\n")

    print("\nPRECIO TOTAL")
    print("=============\n")
    print(f"Entradas estandar: \t\t{ent_estandar} \tPrecio: {PR_ESTANDAR} € \tTotal: {ent_estandar * PR_ESTANDAR} €")
    print(f"Entradas senior: \t\t{ent_senior} \tPrecio: {PR_SENIOR} € \tTotal: {ent_senior * PR_SENIOR} €")
    print(f"Entradas infantil: \t\t{ent_infantil} \tPrecio: {PR_INFANTIL} € \tTotal: {ent_infantil * PR_INFANTIL} €")
    print(f"Entradas día del espectador: \t{ent_dia_esp} \tPrecio: {PR_DIA_ESPECTADOR} € \tTotal: {ent_dia_esp * PR_DIA_ESPECTADOR} €")
    print(f"\n\t\t\t\t\t\t\tTotal: {total} €\n")


# Programa principal

try:    
    while not salir:        
        mostrar_precios()
        opcion = int(input("Introduce el tipo de entrada que quieres comprar: -> "))

        match opcion:
            case 1:
               tipo = 1
               acomp_adulto = True
               cantidad = int(input("Cuantas entradas estandar quieres comprar (0 - para salir ): -> "))
               if cantidad > 0:
                   comprar_entradas(tipo, cantidad)
               else:
                   continue              

            case 2:
                tipo = 2
                acomp_adulto = True
                cantidad = int(input("Cuantas entradas senior quieres comprar (0 - para salir ): -> "))
                if cantidad > 0:                    
                    comprar_entradas(tipo, cantidad)
                else:
                   continue
            case 3:
                tipo = 3                
                if acomp_adulto:                    
                    cantidad = int(input("Cuantas entradas infantiles quieres comprar (0 - para salir ): -> "))
                    if cantidad > 0:
                        comprar_entradas(tipo, cantidad)
                    else:
                        continue
                else:
                    print("\nLas entradas infantiles solo se pueden vender si van acompañados de adultos\n")
                               
            case 4:
                tipo = 4
                acomp_adulto = True
                cantidad = int(input("Cuantas entradas infantiles quieres comprar (0 - para salir ): -> "))
                if cantidad > 0:                    
                    comprar_entradas(tipo, cantidad)
                else:
                   continue            
            case 5:
                if entradas_compradas:
                    mostrar_total()
                    salir = True
                    print("\nEl programa ha finalizado\n")                    
                else:
                    print("\nAun no has realizado ninguna compra\n")              
            case 6:
                salir = True
                print("\nEl programa ha finalizado\n")
            case _:
                print("\nLa opción introducida no es correcta\n")

except ValueError:
    print("\nHas de introducir un número del 1 al 4\n")

except:
    print("\nHa ocurrido un error en el programa\n")


