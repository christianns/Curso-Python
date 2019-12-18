# Problema 04: Determine si un número es múltiplo de 3 y 5.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese un número entero n, y luego el sistema analiza y
# determine si es el número de múltiplo de 3 y de 5.

print ("Ingrese un numero entero:")
n1 = int(input())
if n1 % 3 == 0 and n1 % 5 == 0:
    print ("El numero ingresado es multiplo de 3 y 5")
elif n1 % 3 == 0:
    print ("El numero ingresado es multiplo de 3")
elif n1 % 5 == 0:
    print ("El numero ingresado es multiplo de 5")
else:
    print("El numero ingresado no es multiplo de 3 ni de 5")
