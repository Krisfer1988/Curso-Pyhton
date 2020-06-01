# Este es el primer programa
print("hola mundo")



mivariable = 2
mivariabletexto = "hola mundo"
mivariablelogica = True

print(mivariabletexto)

if mivariable == 3 :
    print (mivariabletexto)
print(mivariablelogica)

A = 10
B = 27

if( A > B):
    print (A)
elif (A==B):
    print("Son iguales")
else:
    print(B)



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
mimaximo = maximoDe3(1,2,3)
print(mimaximo*3)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(2))
print(factorial(3))

texto1="En un lugar de la Mancha"
print(len(texto1))
print(texto1[-1])
print(texto1[ len(texto1)-1 ])

def esVocal(texto,posicionCaracter):
    caracter = texto[posicionCaracter]
    if(caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U"):
        return True
    elif(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        return True
    else:
        return False

print(esVocal(texto1, 1))
texto2="abvde"
print(esVocal(texto2, 3))
print(esVocal("AEIOU", 1))

texto4="ABCDE"
posicion=1
print("ABCDE"[1])
print(texto4[1])
print("ABCDE"[posicion])



# Voy a hacer una fucnion que cuente las vocales desde una posicion
def contarVocalesDesdePosicion(texto, posicion):
# Mirar si en la posicion actual hay una vocal o no
    esteEsVocal = esVocal(texto, posicion)
    if( esteEsVocal == True ) :
        aSumar = 1
    else:
        aSumar = 0;
# Si no soy el ultimo caracter, que siga la fiesta
    longitudDelTexto = len (texto) -1
    if ( posicion == longitudDelTexto):
        return aSumar
    else:
        return aSumar + contarVocalesDesdePosicion(texto, posicion+1)
contarVocalesDesdePosicion("ABCDE",0)


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