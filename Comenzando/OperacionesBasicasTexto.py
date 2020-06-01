#Operaciones Basicas textos

#Hallar la lontitud de un texto

#Hacemos uso de len()
#Hallar la longitud de una palabra cualquiera e imprimirla por pantalla.
print(len("coche"))
print(len("humildad"))


#SubString
#Puedes acceder a distintos caracteres e imprimir por pantalla hacia la izquierda o derecha desde un determinado caractrer.

#Guarda en una variable la frase Hello Python, e imprime los siguientes SubString's:
x="Hello Python"

#Imprima llo Python
print(x[2:])
#Imprima He
print(x[:2])
#Imprima lo Python
print(x[3:])
#Imprima llo Pyth
print(x[2:-2])
#Imprima Python
print(x[6:])
#Imprima Hello
print(x[:6])

#Concatenacion

#Las cadenas de texto pueden ser concatenadas (pegadas juntas) con el operador + y repetidas con *:
#Concatena las palabras coche y cama, para formar cochecama, haciendo uso del operador + e imprimelo por pantalla

palabra = 'coche' + 'cama'
print (palabra)

#Concatena las siguientes palabras: juego, DE, TroNo, S para formar la palabra juegoDETroNoS, haciendo uso del operador + y * e imprimelo por pantalla
palabras = 'juego' + 'DE' + 'TroNo' + 'S'
print(palabras)

#Repite 3 veces la palabra juegoDETroNoS añadiendole delante el caracter << y al final >>, haciendo uso del operador + e imprimelo por pantalla
print('<<' + palabras*3 + '>>')


#Otras funciones para trabajar con cadenas de caracteres

#La función find() regresa el índice correspondiente al primer carácter de la cadena original que coincide con lo que estamos buscando, si existe retorna -1.
#Crea un programa que recoja la palabra jefatura y devuelva el indice correspondiente al primer caracter 't'
cadena = "jefatura"
print(cadena.find("t"))

#Podemos reemplazar uan serie de caracteres por otros, usamos la funcion replace()
#Crear un programa que reemplaze la primera palabra de la frase Hola Jesus, por Adios, y la imprima por pantalla.
cadena1 = "Hola Jesus"
print(cadena1.replace("Hola","Adios"))

#Uso del metodo upper y lower, los cuales cambian todos los caracteres de la palabra por MAYUSCULAS O MINUSCULAS
#Crear un programa que cambie todos los caracteres de la palabra 'teclado' a mayusculas, haciendo uso del metodo upper. Imprimiendolos por pantalla.
cadena2 = "teclado"
print(cadena2.upper())
#Crear un programa que cambie todos los caracteres de la palabra 'RaToN' a minusculas, haciendo uso del metodo lower. Imprimiendolos por pantalla
cadena3 = "RaToN"
print(cadena3.lower())


#Uso de metodo capitalize() - sirve para cambiar el primer caracter del String a mayusculas.
#Crea un programa que cambie el primer caracter del String 'ventiladoR' e imprimelo por pantalla
cadena4 = "ventiladoR"
print(cadena4.capitalize())

#Uso de funcion split(). Se usa para dividir una cadena
#Crea un programa, que de la cadena de marcas de coche Audi|Ford|BMW|porsche, las divida sin el caracter '|', imprimelo por pantalla.
marcasCoche = "Audi|Ford|BMW|porsche"
print(marcasCoche.split("|"))

#Sentencia join(). Caso contrario a la sentencia split().
#Crea un programa, que de la cadena de marcas de electrodomesticos LG -Zanussi-Samsung-Teka, las una con el caracter '|', imprimelo por pantalla.
marcasElectrodometicos = ["LG","Zanussi","Samsung","Teka"]
caracter = "|"
print(caracter.join(marcasElectrodometicos))
