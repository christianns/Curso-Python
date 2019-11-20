# Problema 02: Determinar si un número es positivo, negativo o neutro.
# Análisis: Para la solución de este problema, se requiere que
# ingrese un número entero por teclado y el sistema verifique si
# es positivo, neutro o negativo.


n1 = float(input("Ingrese un número \n"))
if n1 > 0:
    print ("El numero es mayor a 0")
elif n1 == 0:
    print ("El numero es igual a 0")
elif n1 < 0:
    print ("El numero es menor a 0")
