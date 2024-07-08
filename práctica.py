#1. Escribe un programa que imprima : Hola mundo
#2. Escribe una función que determine si un número es par o impar
#3. Escribe un programa que sume todos los numeros de una lista 
#4. Escribe una función que cuente cuantas vocales hay en una cadena de texto
#5. Crear una calculadora que realice operaciones básicas , según la elección del usuario .

#1
print("hola mundo")

#2
numero = int(input("Introduce un número: "))
if numero % 2 == 0: 
    print("El número es par")
else:
    print("El número es impar")


#3
mi_lista = [1 , 2 , 3 , 4 , 5]
suma = 0
for numero in mi_lista :
    suma += numero
print(suma)

#4
def contador_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena :
        if letra in vocales:
            contador += 1
    return contador
texto = input("Introduce una cadena de texto ")
print(f"La cantidad de vocales en la cadena es: {contador_vocales(texto)}")
5#
def calculadora():
    suma = 1 + 3 + 4
    resta = 5 - 5 -2
    multiplicacion = 3 * 3
    print(suma)
    print(resta)
    print(multiplicacion)

#6
nombre = "Mario"
altura = 1.69
print ("Hola "+nombre)
if altura > 1.69:
    print("es mayor a 1.69")
else:
    print("No es mayor a 1.69")


