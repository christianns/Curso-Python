# Condiciones - Estructura selectiva doble.
# evalua una expresion logica o condicion, si es verdad
# ejecuta una determinada instruccion y si es faslo ejecuta otro conjunto de acciones.

# Sentencia else (sino)
# Se encadena a un If para comprobar el caso contrario (en el que no se cumple la condición):

# Ejemplo 1
n = 5
if n == 5:
    print ("N es igual a 5")
else:
    print ("No se cumple la condición")

# Ejemplo 2
x = 11
if x % 2 == 0:
    print(x,"es un número par")
else:
    print(x,"es un número impar")
