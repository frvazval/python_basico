

def calcula_edad(fecha_nacimiento: str, fecha_actual: str) -> int:
   '''
   Devolver la edad a partir de dos fechas

   Params
   fecha_nacimiento: str -> "dd/mm/aaaa"
   fecha_actual: str -> "dd/mm/aaaa"

   Return
   edad: int

   Códigos de error:
   -1 : día o mes incorrecto
   -2 : la fecha de nacimiento debe ser igual o menor que la actual
   '''
   dia1, mes1, any1 = fecha_nacimiento.split("/")
   dia2, mes2, any2 = fecha_actual.split("/")

   # Día o mes incorrecto
   if int(dia1) <= 0 or int(dia1) > 31:
      return -1
   if int(mes1) <= 0 or int(mes1) > 12:
      return -1    
   
   if int(dia2) <= 0 or int(dia2) > 31:
      return -1
   if int(mes2) <= 0 or int(mes2) > 12:
      return -1
    
   # No se puede calcular la edad si la fecha de nacimiento
   # es posterior a la actual
   dif_any = int(any2) - int(any1)
   dif_meses = int(mes2) - int(mes1)
   dif_dias = int(dia2) - int(dia1)
   if (dif_any < 0) or (dif_any == 0 and dif_meses < 0) \
         or (dif_any == 0 and dif_meses == 0 and dif_dias < 0):
      return -2
  
   # Calculo de la edad
   edad = int(any2) - int(any1) # Primero resto los años

   # Compruebo los meses y los dias para saber si ha cumplido los años o aun no los ha cumplido
   if (int(mes2) < int(mes1)) or (int(mes2) == int(mes1) and int(dia2) < int(dia1)): 
      edad -= 1 # Le resta 1 a la diferencia de años
   
   return edad # Retorna la edad
      

    
    


    
# Pedimos las dos fechas al usuario

# fecha_nacimiento = input("Introduce la fecha de nacimiento, formato (dd/mm/aaaa): ")
# fecha_actual = input("Introduce la fecha actual, formato (dd/mm/aaaa): ")

# edad = calcula_edad(fecha_nacimiento, fecha_actual)
# edad = calcula_edad("08/10/1969", "18/02/2025")
# print(edad)
