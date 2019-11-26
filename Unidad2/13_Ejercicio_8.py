# Problema 08: Dado tres números, devolver el número en orden ascendente.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese tres números enteros n1, n2, n3 y luego el
# sistema verifique y devuelva los números ordenados en forma
# ascendente. Primero se debe encontrar el número mayor, luego el
# número menor y al final en número intermedio, que es el
# resultado de sumar los tres números – (Mayor + Menor).

print ("Ingrese primer dígito:")
n1 = int(input())
print ("ingrese segundo dígito:")
n2 = int(input())
print ("Ingrese tercer dígito:")
n3 = int(input())

# Encuentra el numero mayor
if n1 > n2 and n1 > n3:
    print ("El numero mayor es:", str(int(n1)))
elif n2 > n1 and n2 > n3:
    print ("El numero mayor es:", str(int(n2)))
elif n3 > n1 and n3 > n2:
    print ("El numero mayor es:", str(int(n3)))

# Encuentra el numero intermedio
if n1 > n2 and n1 < n3:
    print ("El numero intermedio es:", str(int(n1)))
elif n2 > n1 and n2 < n3:
    print ("El numero intermedio es:", str(int(n2)))
elif n3 > n1 and n3 < n2:
    print ("El numero intermedio es:", str(int(n3)))

# Encuentr el numero Menor
if n1 < n2 and n1 < n3:
    print ("El numero menor es:", str(int(n1)))
elif n2 < n1 and n2 < n3:
    print ("El numero menor es:", str(int(n2)))
elif n3 < n1 and n3 < n2:
    print ("El numero menor es:", str(int(n3)))
