#Ejercicio 1 - Imprime por pantalla con un bucle while 10 veces la palabra 'Ordenador'
i=1
while i <= 10:
    print("Ordenador")
    i = i+1

#Ejercicio 2 - Crea un programa usando un bucle while, que sume todos los numeros impares del 1 al 100 y que muestre todas las sumas hasta llegar al resultado final.
total = 0
i=1
while i<100:
    if (i % 2) != 0:
        total += i
        print(total)
    i+=1


#Ejercicio 3 - Definir una función inversa() que calcule la inversión de una cadena. Debemos de tener un contador que cuente la longitud de la cadena.
"""Hacer uso de un bucle while. 
Para la cadena Hola que tal, debe de dar lat euq aloH """

def inversa (cadena): # parametro de entrada cadena de caracteres
    invertida = ""
    cont = len(cadena) #guardamos la longitud de la cadena introducida
    indice = -1 #marcamos un indice como tope del while
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return print(invertida) #devolvemos e imprimimos la cadena invertida

#Inicializar la funcion con Hola que tal.
inversa("Hola que tal")


#Ejercicio 4
"""Escriba un programa que pida dos números enteros.
 El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números"""

primero = int(input("Escriba un número: "))
segundo = int(input(f"Por favor, escriba un número mayor que {primero}: "))

while segundo <= primero:
    segundo = int(input(f"{segundo} no es mayor que {primero}. Inténtelo de nuevo: "))
print()
print(f"Los números que ha escrito son {primero} y {segundo}.")

"""Ejercicio 2 - Escriba un programa que pida la cantidad de números positivos que se tienen que escribir 
 y a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada"""

objetivo = int(input("Escriba la cantidad de números positivos a escribir: "))
while objetivo < 1:
    objetivo = int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

print()
numero = int(input("Escriba un número: "))
total = 1
if numero > 0:
    cantidad = 1
else:
    cantidad = 0

while cantidad < objetivo:
    numero = int(input("Escriba otro número: "))
    if numero > 0:
        cantidad += 1
    total += 1

print()
if total == 1:
    print("Ha escrito 1 número positivo.")
elif objetivo == 1:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivo.")
else:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivos.")
print("Programa terminado")

#Ejercicio-5 - Escriba un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números introducidos supere el límite inicial
#Hacer uso de un bucle While y usar unna variable que nos indique el limite. El programa ira sumando los valores


limite = float(input("Introduce limite : "))
while limite <= 0:
    limite = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

numero = float(input("Escriba un número: "))
suma = 0
suma += numero

while suma < limite:
    numero = float(input("Escriba otro número: "))
    suma += numero

print(" ")
print(f"Limite superado. La suma de los números positivos introducidos es {suma}.")

