# Ejercicios con bucles

"""Ejercicio 1 -  Crea un programa que muestre por pantalla la palabra Empezamos! y a continuacion muestre por pantalla
6 veces la palabra  Seguimos, deje una linea en blanco y por ultimo muestre por pantalla Final, ¡por fin!, haciendo uso de un
bucle for. """

print("Empezamos!")
for i in [0, 1, 2, 3, 4, 5]:
    print("Seguimos")
print(" ")
print("Final, ¡por fin!")

# Ejercicio 2 - ¿Que pasaria si la lista del ejercicio 1 esta vacia? ¿que imprimira por pantalla?

print("Empezamos!")
for i in []:
    print("Seguimos")
print(" ")
print("Final, ¡por fin!")

"""Ejercicio 3 - En este ejercicio la i tomara los valores del elemento recorrible. 
Crea un programa, que muestre por pantalla el valor de la iteracion "i" y en cada una de ellas, 
muestre su cuadrado, para la lista = 7,8,9,10"""

for i in [7, 8, 9, 10]:
    print(f"iteracion i: {i} valor de su cuadrado {i ** 2}")

# Ejercico 3 - recorriendo una lista de nombres
"""Crea un bucle for que muestre por pantalla todo el contenido de la lista [Coche, Bombilla, Vaso, 1278]"""

for i in ["Coche", "Bombilla", "Vaso", 1278]:
    print({i})

#Ejercico 4 - Crea un programa que muestre la tabla de multiplicar del numero 4

i = 4
print(f"Tabla de multplicar del numero {i}")

for i in [0, 1, 2, 3, 4,5,6,7,8,9]:
    print(f"{4} * {i} = {i ** 2}")
print("El bucle ha terminado")


"""Ejercicio 5 - Recorrer dos bucles for con la misma variable, para imprimir su contenido a la vez. Introducir una separacion entre 
los contenidos de las listas.

La lista1 sera = ["Humildad",12,"Galleta","AaAB"]
La lista2 sera = ["32x12", "bicicleta","electron","casa"] """

for i in ["Humildad",12,"Galleta","AaAB"]:
    print(f"{i}")

print("-----------")

for i in ["32x12", "bicicleta","electron","casa"]:
    print(f"{i}")

#Ejercicio 6 - Usar un bucle for para recorrer una cadena de caracteres como por ejemplo 'INFORMATICO', y al final imprima la palabra entera.

for i in "INFORMATICO":
    print(f"{i}")
print("INFORMATICO")

"""Ejercicio 7 - Haciendo uso de la funcion range(), escribe un proograma que indicandole el numero de saludos que quieres recibir, te los escriba por pantalla. 
Al final debe de imprimir una despedida"""

veces = int(input("Escribe el numero de saludos que quieres recibir: "))
for i in range(veces):
    print("¡Hola, Buenos dias!")
print(" ")
print("Adios, buenos dias")

"""Ejercicio 8 - Escribe un programa que te cuente los multiplos de 2, en un rango desde 1,6. Debemos hacer uso de un contador el cual le llamaremos cuenta. 
Ademas, hacer uso de la funcion range (). Al final el programa debe de sacar el numero de multiplos de 2 por pantalla """

cuenta = 0
for i in range(1, 6):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"En el rango (1,6): Hay {cuenta} múltiplos de 2")

"""Ejercicio 9 - Crea un bucle que nos cuente la suma total de un rango. Ese rango por ejemplo sera (1,6). El programa imprimira el resultado final. 
Hacer uso de una variable que vaya acumulando y sumando en cada iteracion """

Misuma = 0
for i in range(1,6):
    Misuma = Misuma + i
print(f"La suma total es: {Misuma}")

