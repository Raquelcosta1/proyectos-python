#CREA TU PERFIL.

print("Crear un perfil. ")
print("1.Nombre\n2.Apellido\n3.Edad\n4.Trabajo\n ")

bucle = True
while bucle == True:
    opcion=input("Seleccione una opción ")
    if opcion == "1" or opcion == "nombre":
        print("Nombre seleccionado")
        try:
            texto = input("Introduzca su nombre: ")
            print(f"Gracias por introducir su nombre . {texto}")
        except ValueError:
            print(f"Parece que ha habido un error..")
    if opcion == "2" or opcion == "apellido":
        print("Apellido seleccionado")
        try:
            texto = input("Introduzca su apellido : ")
            print(f"Gracias por introducir sus datos, Apellido:  {texto}")
        except ValueError:
            print(f"Parece que ha habido un error")
    if opcion == "3" or opcion == "edad":
        print("Edad seleccionada .")
        try:
            texto = int(input("Introduzca su edad : "))
            print(f"Gracias por introducir sus datos, edad: {texto} ")
        except ValueError:
            print(f"Error, es necesario introducir un número. ")
    if opcion == "4" or opcion == "apellido":
        print("Profesión seleccionada")
        try:
            texto = input("Introduzca su profesión: ")
            print(f"Gracias por introducir sus datos, profesión: {texto}")
        except ValueError:
            print(f"Parece que ha habido un error..")
    salir = input("Ha concluido introduciendo los datos, desea continuar?  \n 1.si 2.no: ")
    if salir == "no" or salir == "2":
         bucle = False

    
 