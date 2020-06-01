#OperacionesBasicas - uso de python como una calculadora

#Imprime un numero
print(1)

#Python distingue entre números enteros y decimales. Al escribir un número decimal, el separador entre la parte entera y la parte decimal es un punto.
#Imprime un numero con parte decimal.
print(1.5)

#Si se escribe una coma como separador entre la parte entera y la decimal, Python no lo entiende como separador, sino como una pareja de números (tupla)
#imprime una tupla de dos numeros enteros
print(4,5)

#Si se escribe un número con parte decimal 0, Python considera el número como número decimal.
print(3.0)

#Operaciones basicas - multiplicacion de dos numeros: uno entero y otro decimal.

#Al hacer operaciones en las que intervienen números enteros y decimales, el resultado es siempre decimal.
#En el caso de que el resultado no tenga parte decimal, Python escribe 0 como parte decimal para indicar que el resultado es un número decimal
print(4.5*3)

#Operaciones basicas - suma y resta dos numeros
print (5+6)
print (9-4)

#Operaciones basicas - division de dos numeros

#Al dividir números enteros, el resultado es siempre decimal, aunque sea un número entero.
#Cuando Python escribe un número decimal, lo escribe siempre con parte decimal, aunque sea nula.
print(9/2)
print(9/3)

#Cuando en una fórmula aparecen varias operaciones, Python las efectúa aplicando las reglas usuales de prioridad de las operaciones
# (primero multiplicaciones y divisiones, después sumas y restas).
print(6+7*2)

#Para realizarlas en otro orden, usar parentesis
print((6+3) / (7-1))

#Operaciones basicas - cociente de una division

#El cociente de una división se calcula en Python con el operador // y tiene la misma prioridad que la division.
#El resultado es siempre un número entero, pero será de tipo entero o decimal dependiendo del tipo de los números que se empleen
#Haz el cociente de varios numeros.
print(10//3)
print(12.0 // 2.0)
print(25 // (3/2))

#Operaciones basicas - resto de una division
#el resto de una división se calcula en Python con el operador %.
#Calcula el resto de dos numeros, enteros o decimales.

print(8%4)
print(11.5 % 4)