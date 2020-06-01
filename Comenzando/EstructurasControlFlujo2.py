"""Programar una funcion que nos indique si es vocal o no una cierta cadena de texto, pasandole como parametros principales un texto y una
posicion de caracter"""

#debe devolver un valor booleano, y debe de distinguir entre vocales Mayusculas o Minusculas. Hacer uso de if, elif o else.
def esVocal(texto,posicionCaracter):
    caracter = texto[posicionCaracter]
    if(caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U"):
        return True
    elif(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        return True
    else:
        return False

#Inicializar 3 textos; indicar para cada uno de ellos si es vocal o no las siguientes posiciones de caracteres
#texto1 = aevde ; posicion 1 ¿es vocal?
#texto2 = AEIOU ; posicion 3 ¿es vocal?
#texto3 = ABCDE ; posicion 4 ¿es vocal? ; imprimir tambien la letra B pasandole una posicion.

#texto 1
texto1 = "aevde"
print(esVocal(texto1,1))

#texto 2
texto2 = "AEIOU"
print(esVocal(texto2,3))

#texto 3
texto3 = "ABCDE"
print(esVocal(texto3,4))

#imprimir letra B pasandole una posicion al texto
posicion = 1
print(texto3[1])

"""Programar una funcion que cuente el numero de vocales desde una posicion dada por parametro, en un texto"""

#Esta funcion debe hacer uso de la funcion esVocal.

def contarVocalesDesdePosicion(texto, posicion):
# Mirar si en la posicion actual hay una vocal o no
    esteEsVocal = esVocal(texto, posicion)
    if( esteEsVocal == True ) :
        aSumar = 1
    else:
        aSumar = 0;
# Si no soy el ultimo caracter, continuo
    longitudDelTexto = len (texto) -1
    if ( posicion == longitudDelTexto):
        return aSumar
    else:
        return aSumar + contarVocalesDesdePosicion(texto, posicion+1)

print(contarVocalesDesdePosicion("ABCDE",0))


"""Crear una funcion que nos cuente las vocales que hay en un texto, para ello debemos de recorrer el texto haciendo uso de un while/bucle
 hasta la longitud de texto"""

def contarVocales(texto):
    posicion=0
    numeroDeVocalesQueLlevo=0
    #Contar las vocales
    while posicion<len(texto):
        #Mirar si en esta posicion es vocal o no y totalizarlo
        estaEsVocal = esVocal(texto,posicion)
        if(estaEsVocal == True):
            numeroDeVocalesQueLlevo = numeroDeVocalesQueLlevo + 1
        #Pasar a la siguiente posicion
        posicion = posicion+1 #posicion+=1
    return numeroDeVocalesQueLlevo

print(contarVocales("AEIOU"))
print(contarVocalesDesdePosicion("AEIOU",0))