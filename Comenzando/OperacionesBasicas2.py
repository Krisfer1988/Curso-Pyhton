#Funcion divmod en Python
#La función divmod(a, b) devuelve una tupla formada por el cociente y el resto de la divión de a entre b.
#Usa la funcion divmod para hallar el cociente y resto de una division cualquiera, e imprimelo por pantalla.
print(divmod(13,4))


#Calculo de potencias

#uso de operador **
#Calcula la potencia 2^3 e imprimela por pantalla
print(2**3)

#Calcula la potencia (4^3)^2 = 4096
print((4**3)**2)

#Calculo de potencias o raices a traves de la funcion pow
#Si se da un tercer argumento, pow(a, b, c), la función calcula primero a elevado b y después calcula el resto de la división por c.

#Calcula 4^3 usando la funcion pow, imprimela por pantalla
print(pow(4,3))

#Calcula usando la funcion pow, el resto de la division entre 2^3 y 5, imprimelo por pantalla
print(pow(2,3,5))


#Uso de funcion Max - halla el maximo valor de un conjunto de valores

#La función integrada max() calcula el valor máximo de un conjunto de valores (numéricos o alfabéticos).
#En el caso de cadenas, el valor máximo corresponde al último valor en orden alfabético, sin importar la longitud de la cadena.

#halla el valor maximo de este conjunto: 3,5,10,45,2,-4,9 e imprimelo por pantalla
print(max(3,5,10,45,2,-4,9))

#Uso de funcion Min - halla el valor minimo de un conjunto de valores
#Actua de la misma forma que la funcion max.
#halla el valor minimode este conjunto: -1,-7,1,6,14,-35,15 e imprimelo por pantalla
print(min(-1,-7,1,6,14,-35,15))


#Uso de funcion Valor absoluto - abs()
#halla el valor sin signo

#Calcula el valor absoluto del numero -3588, e imprimera por pantalla
print(abs(-3588))
