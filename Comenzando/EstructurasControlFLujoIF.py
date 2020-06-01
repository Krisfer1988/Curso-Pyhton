#Estructuras de control de flujo, if, else if, else.

#Ejemplo-1
""""Crear un programa que recoja dos numeros A y B, y nos saque por pantalla los siguientes casos:
si A>B debe imprimir A
si B>A debe de imprimir B
y si son iguales, debe imprimir 'son iguales' """

A = 10
B = 27

if( A > B):
    print (A)
elif (A==B):
    print("Son iguales")
else:
    print(B)

#Ejemplo-2
#Crear un programa que nos muestre por pantalla:
#si el color del semaforo esta en verde, se pueda cruzar y si es otro color nos diga que esperemos.

semaforo = "verde"

if (semaforo == "verde") :
    print ("Cruzar la calle")
else:
    print ("Esperar")


#Ejemplo-3
"""Queremos hacer el mismo programa que el ejercicio 1 pero implementandolo con una funcion. Para ello debemos de definirlo con:

**************Estructura basica*****************
def NOMBRE_MI_FUNCION(variables/parametros de entrada si los hay) :
    #Cuerpo de mi funcion
    
NOMBRE_MI_FUNCION(valores de inicio para que se ejecute)"""

#En base a esta estructura basica, resuelve el mismo ejercicio: decir de dos nuemeros A y B si uno es mayor que el otro o si son iguales.
#Implementar al final de codigo, una modificacion de la misma funcion para que te resuelva el mayor de 3 numeros.

def maximo(a,b):
    if (a > b):
        return a
    else:
        return b

def maximoDe3(a,b,c):
    return maximo(a,maximo(b,c))

print(maximo(10,11))
print(maximo(20,30))
print(maximoDe3(1,2,3))

#Implementar al final de codigo, una modificacion de la misma funcion para que te resuelva el mayor de 3 numeros, y el resultado lo x3.
mimaximo = maximoDe3(1,2,3)
print(mimaximo*3)

#Ejemplo-4
#Escribir un programa sencillo con if else que nos diga si un numero es par o impar.

numero = int(input("Escriba un número: "))
if (numero % 2):
    print("es impar")
else:
    print("es par")









