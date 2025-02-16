"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20
- Día del espectador : 5.00€ (quizá)

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar 
el proceso sin que se produzca la compra

"""
import os

# Informción de partida
tipo_entrada = {"estandar": 9.0, "senior": 6.9, "infantil": 7.2}
# tipo_entrada = {"estandar": 9.0, "senior": 6.9, "infantil": 7.2, "dia del espectador": 5.0}

# Lo que el cliente va a comprar
lista_entradas_compradas = []

lista_iniciales = []
for clave in tipo_entrada:
    lista_iniciales.append(clave[0])


compra_activa = True

while compra_activa:

    menu = "Precios de la entradas:"
    # Leer el diccionario con los datos de las entradas
    for clave, valor in tipo_entrada.items():
        menu += f"\n{clave[0].upper()}. {clave.capitalize()} : {valor:.2f}€"

    menu += "\n\nF. Finalizar la compra"
    menu += "\nX. Salir sin compra"
    menu += "\n\nElija el tipo de entrada."
    menu += "\nA continuación podrá indicar la cantidad.\n>>> "

    eleccion_entrada = input(menu).lower().strip()

    if eleccion_entrada == "x":
        print("\nAplicación finalizada. ¡Hasta pronto!")
        compra_activa = False
    elif eleccion_entrada == "f":
        if lista_entradas_compradas:
            pass
            # compra_activa = False
        else:
            print("Aún no ha realizado la compra\n")
    elif eleccion_entrada in lista_iniciales:
        # buscar la entrada que corresponde a la elección del cliente
        for clave, valor in tipo_entrada.items():
            if eleccion_entrada == clave[0]:
                try: 
                    cantidad = int(input("Indique cuántas entradas desea --> "))
                except:
                    print("Debe indicar un número entero")
                    break
                ### Nos quedamos aquí
                tipo = clave
                precio = valor
                subtotal = precio * cantidad

    else:
        os.system("cls")
        print("Opción incorrecta.\n")