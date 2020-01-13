# Condiciones - Sentencia elif (sino si)
# Se encadena a un if u otro elif para comprobar múltiples condiciones,
# siempre que las anteriores no se ejecuten:
n = 2
if n == 1:
    print ("N es igual a 1")
    if n < 5:
        print ("N es menor que 5")
elif n == 2:
    print ("N es igual a 2")
elif n == 3:
    print ("N es igual a 3")
else:
    print ("No se cumple la condición")

# Instrucción pass
# Sirve para finalizar un bloque, se puede utilizar en un bloque vacío:

if True:
    pass
