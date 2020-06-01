ESTADO_NOMBRE = 0
ESTADO_DOMINIO = 1
ESTADO_EXTENSION = 2

modoPruebas = False

def mostrarError(caracterErroneo, posicionDelError, error):
    if modoPruebas:
        print("Error encontrado al validar el email.")
        print("  Error en el carácter número: " + str(posicionDelError))
        print("  Caracter erróneo: " + caracterErroneo)
        print("  Problema encontrado: " + error)
    return False

#Maravillosa funcion para validar emails
# Devuelve true o false dependiendo de si es bueno o no
def validarEmail(emailAValidar):
    caracterActual = ""
    posicionActual = 0
    posicionArroba = 0
    estadoActual = 0
    caracteresTotales =len(emailAValidar)
    while posicionActual<caracteresTotales:
        #Saber cual es el caracter actual
        caracterActual = emailAValidar[posicionActual]
        #Validar el caracter actual
        # Mirar en que estado estoy
        if estadoActual == ESTADO_NOMBRE:
            #Estoy en el nombre
            if caracterActual == "@":
                if posicionActual==0:
                    return mostrarError(caracterActual, posicionActual, "Debe poner el nombre antes de la @")
                else:
                    posicionArroba = posicionActual
                    estadoActual = ESTADO_DOMINIO
            elif (not caracterActual.isalnum()):
                if caracterActual != ".":
                    if caracterActual != "-":
                        if caracterActual != "_":
                            return mostrarError(caracterActual, posicionActual, "")
        elif estadoActual == ESTADO_DOMINIO:
            #Estoy en el dominio
            if caracterActual == ".":
                #Mirar si han metido mas caracteres en el domonio. Si no error
                if posicionActual == posicionArroba + 1:
                    return mostrarError(caracterActual, posicionActual, "No ha introducido un dominio válido")
                else:
                    estadoActual = ESTADO_EXTENSION
            elif not caracterActual.isalnum():
                return mostrarError(caracterActual, posicionActual, "")
        else: #elif estadoActual==2
            #Estoy en la extension
            if caracterActual ==".":
                #OJO Mirar que el de antes no fuera tambien puntoi
                if(emailAValidar[posicionActual-1]=="."):
                    return mostrarError(caracterActual, posicionActual, "Un dominio / subdominio no puede estar vacio ")
            elif caracterActual.isdigit():
                estadoActual = ESTADO_DOMINIO
            elif not caracterActual.isalpha():
                return mostrarError(caracterActual, posicionActual, "")
        #Actualizar el estado actual si es necesario
        #Pasar al siguiente
        posicionActual+=1

    if estadoActual != ESTADO_EXTENSION or emailAValidar[-1] == ".":
        return mostrarError(caracterActual, posicionActual, "Dirección sin terminar")
    return True

#resultadoValidacion = validarEmail("ivan@kiwitec.com.es")
#print(resultadoValidacion)