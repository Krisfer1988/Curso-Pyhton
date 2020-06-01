#Ejercicio-1
#Mete los valores del 1 al 50 en una lista.

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i = i + 1
print(lista)

#¿Se podria hacer mucho mas compacto y eficiente?

lista = list(range(1, 101))
print(lista)

#Ejercicio -2
#Crear un diccionario con los jugadores de la Seleccion Española que gano el mundial.
#Casillas-ramos-pique-puyol-Capdevila-XabiAlonso-Busquets-xavi-Pedro-iniesta-Villa
#recorrer el diccionario e imprimir sus pares clave

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa" }
# Recorrer un diccionario, imprimiendo su clave-valor
for k,v in futbolistas.items():
    print ("%s -> %s" %(k,v))


#¿Cuantos elementos tiene el diccionario?
numElem = len(futbolistas)
print ("\nNumero de elementos del diccionario len(futbolistas) = %i" %numElem)


#Ejercicio - 3
#Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
numero = int(input("Dame un numero: "))
lista = []
for i in range(1, 11):
    lista.append(i * numero)
print(lista)

#Ejercicio -4
#Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
#la tupla sera por ejemplo: (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)

numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)
numero = int(input("Dame un numero: "))
contador = 0
for i in numeros:
    if numero == i:
        contador = contador + 1
print("Hay ", contador, " repeticion/es")

#¿Se podria hacer de forma mas compacta? Realizalo para la siguiente tupla: (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)
numeros = (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)
numero = int(input("Dame un numero: "))
print("Numero de repeticiones: ", numeros.count(numero))

#Ejercicio -5
#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga. Realizalo para la tupla: (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)
numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)
maximo = numeros[0]
minimo = numeros[0]
for i in numeros:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i
print("El maximo es ", maximo)
print("El minimo es ", minimo)


#¿Se podria hacer mas eficiente? Realizalo para la tupla:(7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)
numeros = (7, 6, 5, 4, 3, 2, 3, 4, 5, 1, 4, 3)
print("Maximo: ", max(numeros))
print("Minimo: ", min(numeros))

#Ejercicio - 6
"""Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y 
la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero"""

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre")

salir = False
while (not salir):
    numero = int(input("Dame un numero: "))
    if (numero == 0):
        salir = True
    else:
        if (numero >= 1 and numero <= len(meses)):
            print(meses[numero - 1])
        else:
            print("Inserta un numero entre 1 y ", len(meses))

#Ejercicio-7

#Escriba un programa que permita crear una lista de palabras.
#Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
#Por último, el programa tiene que escribir la lista.

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

#Ejercicio - 8
#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    eliminar = input("Palabra a eliminar: ")
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == eliminar:
            del(lista[i])
    print("La lista es ahora:", lista)

#Ejercicio-9
"""Escriba un programa que permita crear una lista de palabras y que,
a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta)"""

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    inversa = []
    for i in lista:
        inversa = [i] + inversa
    print("La lista inversa es:", inversa)
