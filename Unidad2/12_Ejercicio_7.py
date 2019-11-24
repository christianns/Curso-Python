# Problema 07: Dado un número entero, devolver el doble si el
# número es par, caso contrario el triple.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese un número entero n y luego el sistema verifique
# y devuelva el doble o el tiple del número.

print ("Ingrese un digito")
n1 = int(input())
if n1 % 2 == 0:
    n1 *= 2
    print ("El doble es", str(int(n1)) + " y es par.")
else:
    n1 *= 3
    print ("El digito", str(int(n1)) + " es impar.")
