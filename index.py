import os
os.system("cls")
import validaciones as valentina
from datetime import date
punctuation = ["#", "-", "/"]

BDHojasdVida = {"123": {"DatosPersonales": ["nombre", ("fechaNacimiento"), ["Contactos"], ["DireccionesConSet"], ["CorreosConSet"]],
                              "FormacionAcademica": [["inst", "titulo", "año"], ["ints2", "titulo2", "año2"]],
                              "ExperienciaProfesional": [["empres","cargo","funciones", "duracion"], ["empresa2","cargo","funciones2", "duracion"]],
                              "ReferenciaPersonales": [["nombre", "relacion", "telefono"], ["nombre2", "relacion2", "funcion2"]],
                              "Habilidades/Certificaciones": [["Descripcion", "Fecha"], ["Descripcion2", "Fecha2"]]}}

#Lista que va almacenar los datos: nombre, fecha de nacimiento, ListasdeContactos, ListaDirecciones, ListaCorreos
DatosPersonales = []


#Ingresar documento
flag = True
while flag:
    documento = input("\nIngrese un documento\n>> ")
    flag = valentina.ValidarNumber(documento)

#Ingresar nombre
flag = True
while flag:
    nombre = input("\nIngrese su nombre\n>> ")
    flag = valentina.ValidarTexto(nombre)

    if flag:
        continue
    else:
        DatosPersonales.append(nombre)
        

#Ingresar Fecha de Nacimiento
flag = True
while flag:
    FechaNacimiento = input(f"\nIngrese su fecha de nacimiento en formato yyyy-mm-dd\nEjemplo-> {date.today()}\n>> ")
    flag = valentina.ValidarFecha(FechaNacimiento)
    
    if flag:
        continue
    else:
        DatosPersonales.append((FechaNacimiento))

#Ingresar contactos y debe ingresar almenos 1 contacto
flag = True
while flag:
    Contacto = input("\nIngrese un numero de contacto\n>> ")

    flag =valentina.ValidarNumber(Contacto)

    if flag:
        continue
    elif not flag:
        DatosPersonales.append([Contacto])
        flag = input("\nSi desea agregar un nuevo contacto oprima Enter, sino desea agregar mas contactos ingrese 1\n>> ")
        if flag:
            flag = False
        else:
            flag = True
            continue


#Ingresar direcciones 
flag = True
while flag:
    Direccion = input("\nDireccion\n>> ")

    flag = valentina.ValidarTexto(Direccion)
    
    if flag:
        continue
    elif not flag:
        DatosPersonales.append([Direccion])
        flag = input("\nSi desea agregar un nuevo contacto oprima Enter, sino desea agregar mas contactos ingrese 1\n>> ")
        if flag:
            flag = False
        else:
            flag = True
            continue


print(DatosPersonales)