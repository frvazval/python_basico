

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
   if int(dia1) <= 0 or int(dia1) > 31:
      return -1
   if int(mes1) <= 0 or int(mes1) > 12:
      return -1
    
   dia2, mes2, any2 = fecha_actual.split("/")
   if int(dia2) <= 0 or int(dia2) > 31:
      return -1
   if int(mes2) <= 0 or int(mes2) > 12:
      return -1
    
   if int(any2) < int(any1):
      return -2
    
   edad = int(any2) - int(any1)
   if int(mes2) < int(mes1):
      edad -= 1
    
    


    
# Pedimos las dos fechas al usuario

# fecha_nacimiento = input("Introduce la fecha de nacimiento, formato (dd/mm/aaaa): ")
# fecha_actual = input("Introduce la fecha actual, formato (dd/mm/aaaa): ")

# edad = calcula_edad(fecha_nacimiento, fecha_actual)
edad = calcula_edad("08/10/1969", "18/02/2025")
 
if edad == -1 or edad == -2:
   pass
else:
   pass
