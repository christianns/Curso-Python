# tuplas
# las tuplas no se pueden modificar a diferencia de una lista

# Definisión de un tupla
tupla  = (100, 'hola', [1,2,3],-50, 100, 10.3, 'hola')

# Imprime las posiciones 0 y 1.
print (tupla[0])
print (tupla[1])

# Imprime la tupla
for i in tupla:
    print (i)

# Funciones de tuplas
print (len(tupla))

# esta funcion len muestra la cantidad de caracteras de la posición 1.
# este es solo para cadenas de caracteres y listas
print (len(tupla[1]))

# la función .index muestra la posición del dato
print (tupla.index([1,2,3]))

# la funcion .count indica la cardinalidad del dato ingresado
print (tupla.count(100))
