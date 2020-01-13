# tuplas
# las tuplas no se pueden modificar (inmutabilidad) a diferencia de una lista

# Definisión de un tupla
tupla  = (100, 'hola', [1,2,3],-50, 100, 10.3, 'hola')

# Imprime las posiciones 0 y 1.
print (tupla[0]) # 100
print (tupla[1]) # 'hola'

# Imprime la tupla
for i in tupla:
    print (i)

# Funciones de tuplas
print (len(tupla))

# esta funcion len muestra la cantidad de caracteras de la posición 1.
# este es solo para cadenas de caracteres y listas
print (len(tupla[1]))

# Indexación y slicing
print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])

# Inmutabilidad

tupla[0] = 50 # Indica error

# la función .index muestra la posición del dato
print (tupla.index([1,2,3]))

# la funcion .count indica la cardinalidad del dato ingresado
print (tupla.count(100))

# append() ?
# Al ser inmutables, las tuplas no disponen de métodos para modificar su contenido

tupla.append(10)
