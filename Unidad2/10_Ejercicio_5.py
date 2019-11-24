# Problema 05: determine si un nuero entero es par o impar.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese un número entero n, y luego el sistema verifique si el número es par o impar.

print ("Ingrese un digito")
n1 = int(input())
if n1 % 2 == 0:
    print ("El digito", str(int(n1)) + " es par.")
else:
    print ("El digito", str(int(n1)) + " es impar.")
