DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"
from datetime import date

#Funcion que valida si en una variable que va a ser string pero va a almacenar numeros quemados, hay caracteres
def ValidarNumber(number): 
    if not number.isdigit():
       print(WARNING + "ERROR: Ingreso un caracter" + RESET)
       return True #Retorna True para que el flag sea True y el ciclo se puede repetir y asi pida otra vez el input
    elif number == "":
       print(WARNING + "ERROR: Ingreso datos vacios" + RESET)
       return True
    else:
        return False #Retorna False para que se termine el ciclo

#Para validar que el texto que ingrese el usuario no este vacio  
def ValidarTexto(texto): 
    if texto == "":
       print(WARNING + "ERROR: No puede ingresar datos vacios" + RESET)
       return True
    else:
        return False

#Ingresar validaciones en las fechas
def ValidarFecha(fecha):

    if not "-" in fecha: #Verificar que se hayan separado por con "-"
        print(WARNING + "ERROR: Utilice '-' para separar los años, meses y dias" + RESET)
        return True
  
    else:
        lista = fecha.split("-")

        if len(lista) != 3:
            print(WARNING + "ERROR: Hace falta un dato" + RESET )
            return True

        elif not all(len(x) == 4 or len(x) == 2  for x in lista): #Verificar que haya ingresado bien año, mes, dia
            print(WARNING + "ERROR: Ingrese la fecha completa, utilice el ejemplo" + RESET )
            return True

        elif not all(lista[x].isdigit() for x in range(len(lista))): # Validacion para que no ingrese un caracter
            print(WARNING + "ERROR: Ingreso un caracter" + RESET)
            return True
        
        #Validacion para el caso de mes y dia no pase del limite 12 y 31 respectivamente
        elif int(lista[1]) > 12 :
            print(WARNING + "ERROR: Ingrese un mes valido" + RESET)
            return True
        
        elif int(lista[2]) > 31:
            print(WARNING + "ERROR: Ingrese un dia valido" + RESET)
            return True
        
        else:
            return False



    
            
