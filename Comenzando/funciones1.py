#formato clasico para definir una funcion
""""
def NOMBRE_MI_FUNCION(variables/parametros de entrada si los hay) :
    #Cuerpo de mi funcion

NOMBRE_MI_FUNCION(valores de inicio para que se ejecute)"""

#Ejercicio-1
#crea una funcion que imprima por pantalla la suma de dos numeros
def Suma (x, y):
    return x+y

print(Suma(6,8))

#Ejercicio-2
#Crea una funcion que resuelva el perimetro de un rectangulo de lado mayor 5 y lado menor 3
def perimetroRectangulo(ladoMayor, ladoMenor):
    return 2*ladoMayor+2*ladoMenor

perimetroRectangulo(5,3)

#Ejercicio-3
#Crea una funcion que resuelva el area de un triangulo. Area = base x altura / 2

def AreaTriangulo(base, altura):
    area = (base*altura)/2
    return area

print(AreaTriangulo(2,5))


#Ejercici-4
#Crear una funcion que pasandole por parametro 3 numeros (3,5,8), nos indique cual de los 3 es el numero mayor. Hacer uso de if, elif y else.

def maxTresNumeros (num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print (num1)
    elif (num2 > num1 and num2 > num3):
        print (num2)
    elif (num3 > num1 and num3 > num2):
        print (num3)
    else:
        print ("Son iguales")
#inicializo la funcion con mis 3 numeros
maxTresNumeros(3,5,8)


#Ejercicio-5
"""Programar una funcion que dibuje un rectangulo a base de "*". Debe de tener dos parametros, ancho y alto y se deben de pedir por consola 
a traves de la funcion input de Phyton """
#Debe de pedir por parametro la anchura y la altura del rectangulo que se desee dibujar. Utilizar un bucle anidado for.


def rectangulo(ancho, alto):
    for i in range(alto): #Para cada alto
        for j in range(ancho): #Dibujar un ancho
            print("* ", end="")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
rectangulo(anchura, altura)

#Ejercicio-6
"""Desarrollar una funcion, que recorra una lista de numeros enteros, y que imprima tantas 'x' como indique cada numero de la lista"""
#Para recorrer la lista usaremos un for, desde i hasta lista (longitud total) y para cada elemento del for imprimiremos el caracter "x"
def ImprimirXlista (lista):
    for i in lista:
        print (i * "x")
 #Inicializar la funcion pasandole una lista.
ImprimirXlista([2, 3, 5, 7, 11, 13])







