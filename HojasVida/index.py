BDHojasdVida = {"123": {"DatosPersonales": ["nombre", ("fechaNacimiento"), ["Contactos"], ["DireccionesConSet"], ["CorreosConSet"]],
                              "FormacionAcademica": [["inst", "titulos", "años"], ["ints2", "titulo2", "años"]],
                              "ExperienciaProfesional": [["","","", ""], ["","","", ""]],
                              "ReferenciaPersonales": ["", "", ""],
                              "Habilidades/Certificaciones": ["Descripcion", "Fecha"]}}
def IngresarValidarPersonales():
    flag = True
    #Ingresar Nombre
    while flag:
        nombre = input("Nombre: ")
        if nombre == "":
            print("ERROR: Ingrese un nombre")
            continue
        flag = False

    
    #Ingresar Fecha Nacimiento
    flag = True
    while flag:
        FechaNacimiento = input("Ingrese fecha de nacimiento(yyyy/mm/dd): ")
        F = FechaNacimiento.split("/")
        if len(F[0]) != 4 or len(F[1]) != 2 or len(F[2]) != 2:
            print("ERROR: Ingrese una fecha correcta")
            continue
        elif int(F[0]) > 2025 or int(F[1]) > 12 or int(F[2]) > 31:
            print("Ingrese datos validos")
            continue
        # elif int(F[0]) < 0 or int(F[1]) < 0 or int(F[2]) < 0:
        #     print("ERROR:Numero negativo")
        #     continue

        flag = False

    #Ingresar Contactos
    flag = True
    while flag:
        Contacto = input()





flag = True
while flag:
    Documento = input("Documento: ")
    if Documento in BDHojasdVida:
        print("El documento ya esta")
        continue
    break
        
IngresarValidarPersonales()


