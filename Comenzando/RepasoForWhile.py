#Mas ejercicios con for y while

#Ejercicio 1 - Crear una funcion pedir_confirmacion que nos pregunte si queremos salir o no.
#si la respuesta es si, debera de acpetar los siguientes tipos de introduccion por pantalla: ('s', 'S', 'si', 'Si', 'SI')
#si la respuesta es no, debera de acpetar los siguientes tipos de introduccion por pantalla: ('n', 'no', 'No', 'NO')
#Cuando muestre alguna de esas cadenas, debera de salir del programa.

def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise IOError('usuario duro')
        print(queja)

pedir_confirmacion("quieres salir?")

#Ejercicio 2
"""Escribir un programa con dos for anidados. El primer bucle debe de recorrer el rango de 2 a 10, y el segundo rango de 2 a la variable de iteracion del primer for. 
Con el objetivo de ver:
    si n/x es par: 
        Imprimira: n = x imprimirá por pantalla n/x  
    si no seguimos buscando un factor primo. 
        imprimira por pantalla n es un numero primo. """
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
        else:
            # sigue el bucle sin encontrar un factor
            print(n, 'es un numero primo')

#Repaso de for

#Ejercicio 3
"""Crear con un bucle for un programa que recorra una lista de nombres, y nos imprima el numero de iteracion y su contenido. 
Para la lista ['Mary', 'tenia', 'un', 'corderito'] """
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print(i, a[i])

#Ejercicio 4
"""Recorrer con un bucle for la lista de palabras: ['gato', 'ventana', 'defenestrado'] y que nos imprima por pantalla la palabra y su longitud. """
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
    print(p, len(p))

#Ejercicio 5
"""Usar un bucle for para recorrer la siguiente tupla con el metodo items(). Debe de imprimir por pantalla el valor de las tuplas"""
#{'gallahad': 'el puro', 'robin': 'el valiente'}

caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.items():
    print(k, v)

#Ejercicio 6
"""hacer uso de la funcion enumerate para enumerar automaticamente a traves de un bucle for, la lista 'ta','te'ti' """
"""for i, v in enumerate(['ta', 'te', 'ti']):
    print(i, v)"""

#Ejercicio 7
"""Crear con un for y la funcion zip(), un iterador que agrege los elementos de cada uno de los iterables, de estas dos listas
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul'] """

"""El programa recorrera las dos listas, y preguntara ¿Cual es tu? e imprimira por pantalla el valor de la variable de recorrido de esa lista y 
añadira el valor de la variable de recorrido de la segunda lista, haciendo un preguntas y repuestas. """


preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print('Cual es tu {0}? {1}.'.format(p, r))