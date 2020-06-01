#funciones2 -  recursividad

#Ejemplo-1
#Crear un programa recursivo que calcule el factorial de un numero y lo imprima por pantalla.
#si el factorial es 1 lo devuelve automaticamente
#En otro caso, hacemos la llamada recursiva para hallar el factorial correspondiente.

def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(7))

#Ejemplo-2
#Crear una funcion recursiva que represente la funcion de fibonacci, pasandole por parametro el numero que queramos que nos calcule la sucesion.

#La sucesión comienza con los números 0 y 1, y a partir de estos, «cada término es la suma de los dos anteriores
def fib(num):
    a, b = 0,1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b
    print()
#Inicializacion de la funcion para el numero que queramos
fib(1000)


#Ejemplo-3
"""Crear un programa que te pida ¿de que color es una naranja? y tu debes escribir un color .
Si tu respondes otro color que no sea naranja, se vuelve a llamar la funcion a si misma y te lo vuelva a preguntar.
Usar como condicion de parada la palabra naranja"""

def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print ("Fallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print ("Perdiste!")
    else:
        print ("Ganaste!")
#inicializar funcion
jugar()





