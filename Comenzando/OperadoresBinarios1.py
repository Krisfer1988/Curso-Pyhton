"""Haciendo uso de expresiones compuestas, utiliza los operadores binarios para resolver estas operaciones"""

#¿Que resultado obtenemos?

#El operador not se evalúa antes que el operador and

#not True and False
print(not True and False)
#(not True) and False
print((not True) and False)
#not (True and False)
print(not (True and False))


#El operador not se evalúa antes que el operador or:
#not False or True
print(not False or True)
#(not False) or True
print((not False) or True)
#not (False or True)
print(not (False or True))

#El operador and se evalúa antes que el operador or:
#False and True or True
print(False and True or True)
#(False and True) or True
print((False and True) or True)
#False and (True or True)
print(False and (True or True))

#Otros ejemplos:
#Si en las expresiones lógicas se usan valores distintos de T o F, Python utiliza esos valores en vez de True o False
print(2 or 3)
print (3 and 3)
print (3 and 7)
#Si queremos convertir ese resultado aun valor booleano introducimos delante la palabra bool(expresion a comprobar)
print(bool(2 or 3))
print(bool (3 and 3))
print(bool(3 and 7))

"""Evalua la siguiente operacion haciendo uso de operadores binarios. El resultado sera true,
si y solo si todas sus comparaciones son verdaderas """
print(4 == 3 + 1  and 3 + 1 > 2)

