'''
Ejercicio 2: Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
 * Si el primer número es mayor que el segundo, debe devolver 1.
 * Si el primer número es menor que el segundo, debe devolver -1.
 * Si ambos números son iguales, debe devolver un 0.
Los numero a y b tienes que ser ingresados por teclado
'''
a = int(input('Ingrese 1er digito:\n'))
b = int(input('Ingrese 2do digito:\n'))

def relacion (a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
    return ()
print (relacion(a,b))
