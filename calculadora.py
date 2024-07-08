print("Hola , bienvenido a la calculadora ")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División ")
bucle = True
while bucle == True:
    
    opcion =input("Selecciona una opción del menú ")
    if opcion == "1" or opcion == "suma":
        numero = int(input("introduce el primer número "))
        numero_2 = int(input("Introduce el segundo número "))
        resultado = numero + numero_2
        print(resultado)
    elif opcion == "2" or opcion == "resta":
        numero = int(input("Introduce el primer número "))
        numero_2 = int(input("Introduce el segundo número "))
        resultado = numero - numero_2
        print(resultado)
    elif opcion == "3" or opcion == "multiplicacion":
        numero = int(input("Introduce el primero número "))
        numero_2 = int(input("Introduce el segundo número "))
        resultado = numero * numero_2
        print(resultado)
    elif opcion == "4" or opcion == "division":
        numero = int(input("Introduce el primer número "))
        numero_2 = int(input("Introduce el segundo número "))
        resultado = numero / numero_2
        print(resultado)
    else: 
        print("No se encontró la operación especificada")

    salir =input("Desea continuar ejecutando la calculadora? \n 1. si 2.no: ")
    if salir == "2":
        bucle = False
        