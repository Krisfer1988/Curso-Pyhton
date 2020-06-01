# +0000-999-999-999-999

# +999 999 999 999
# 0999 999 999 999
# 999 999 999
def normalizarTelefono(telefonoAValidar):
    b1 = "34"
    b2 = ""
    b3 = ""
    b4 = ""
    separadorUtilizado=""
    cantidadDeNumeros = len(telefonoAValidar)
    posicionActual = 0
    estadoActual = 1
    while posicionActual < cantidadDeNumeros:
        caracterActual = telefonoAValidar[posicionActual]
        #Operaciones pertinentes
        if estadoActual == 1 :
            if caracterActual =="+":
                estadoActual = 3
            elif caracterActual =="0":
                estadoActual = 2
            elif caracterActual.isdigit() :
                estadoActual = 8
                b2=caracterActual
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 2 :
            if caracterActual == "0":
                estadoActual = 3
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 3:
            if caracterActual.isdigit():
                b1 = caracterActual
                estadoActual = 4
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 4:
            if caracterActual.isdigit():
                b1 += caracterActual
                estadoActual = 5
            elif caracterActual == '-' or caracterActual == ' ' or caracterActual == '/':
                estadoActual = 7
                separadorUtilizado = caracterActual
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 5:
            if caracterActual.isdigit():
                b1 += caracterActual
                estadoActual = 6
            elif caracterActual == '-' or caracterActual == ' ' or caracterActual == '/':
                estadoActual = 7
                separadorUtilizado = caracterActual
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 6:
            if caracterActual.isdigit():
                b2 += caracterActual
                estadoActual = 8
            elif caracterActual == '-' or caracterActual == ' ' or caracterActual == '/':
                estadoActual = 7
                separadorUtilizado = caracterActual
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 7 or estadoActual == 11 or estadoActual == 15 or estadoActual == 19:
            if caracterActual.isdigit():
                b2 += caracterActual
                estadoActual = estadoActual + 1
            else:
                raise NameError("Prefijo internacional Inválido")
        elif estadoActual == 8 or estadoActual == 12 or estadoActual == 16 or estadoActual == 20:
            if caracterActual.isdigit():
                b2 += caracterActual
                estadoActual = estadoActual +1
            else:
                raise NameError("Número de teléfono inválido")
        elif estadoActual == 9 or estadoActual == 13 or estadoActual == 17:
            if caracterActual.isdigit():
                b2 += caracterActual
                estadoActual = estadoActual +1
            elif caracterActual == '-' or caracterActual == ' ' or caracterActual == '/':
                if(separadorUtilizado == caracterActual):
                    estadoActual = estadoActual + 2
                else:
                    raise NameError("Caracter utilizado como separador no homogéneo")
            else:
                raise NameError("Número de teléfono inválido")
        elif estadoActual == 10  or estadoActual == 14 or estadoActual == 18 :
            if caracterActual.isdigit():
                b2 += caracterActual
                estadoActual = estadoActual+2
            elif caracterActual == '-' or caracterActual == ' ' or caracterActual == '/':
                if (separadorUtilizado == caracterActual):
                    estadoActual = estadoActual + 1
                else:
                    raise NameError("Caracter utilizado como separador no homogéneo")
            else:
                raise NameError("Número de teléfono inválido")
        posicionActual+=1 #posicionActual = posicionActual +1
    if len(b2) == 9:
        pass
    else:
        raise NameError("Número de teléfono inválido")

    b4 = b2[6:]
    b3 = b2[3:6]
    b2 = b2[0:3]
    return "(+" + b1+")-"+b2+"-"+b3+"-"+b4
"""
while True:
    telefono= input("Dime un teléfono: ")
    try:
        telefonoNormalizado = normalizarTelefono(telefono)
        print (telefonoNormalizado)
        break
    except NameError as error:
        print("Ha ocurrido un error al normalizar el telefono")
        print(error)
"""
