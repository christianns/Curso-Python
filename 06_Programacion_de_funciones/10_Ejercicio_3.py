'''
Ejercicio 3: Realiza una función llamada intermedio(a, b) que a partir de dos números,
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio
entre dos valores que tenga que ingresar por teclado:
Recordatorio
El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
'''
a = int(input('Ingrese 1er digito:\n'))
b = int(input('Ingrese 2do digito:\n'))

def intermedio (a,b):
    return (a + b)/2
print (intermedio(a,b))

'''
OPCION 2

def intermedio (a,b):
    i = (a + b)/2
    return i
print (intermedio(a,b))

'''
