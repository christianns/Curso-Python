# Iteraciones - Sentencia while (mientras)
# Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

# Se basa en repetir un bloque a partir de evaluar una condición lógica,
# siempre que ésta sea True. Queda en las manos del programador decidir el
# momento en que la condición cambie a False para hacer que el While finalice.

c = 0
while c <= 5:
    c+=1
    print("c vale", c)

# Uso de else en while
# Se encadena al While para ejecutar un bloque de código una vez la condición ya no devuelve True (normalmente al final):

opcion = 0
while opcion < 5:
    print (opcion)
    opcion += 1
else:
    print ("Termina el ciclo while")
