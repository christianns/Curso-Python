# Problema 06: Dado tres números enteros, devolver el número mayor.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese tres números enteros n1, n2, n3 y luego el
# sistema verifique y devuelva el número mayor.

print ("Ingrese un numero:")
n1 = int(input())
print ("Ingrese un numero:")
n2 = int(input())
print ("Ingrese un numero:")
n3 = int(input())

# Compara los numeros ingresados

if n1 > n2 and n1 > n3:
    print ("El numero mayor es", str(int(n1)))
elif n2 > n1 and n2 > n3:
    print ("El numero mayor es", str(int(n2)))
else:
    print ("El numero mayor es", str(int(n3)))
