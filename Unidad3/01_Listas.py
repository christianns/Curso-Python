# Definicion de una lista
numeros = [1, 2, 3, 4]
datos = [5, 'cadena', 5.5, 'texto', 3, 'lunes']

# Muesta la lista
print (numeros)
print (datos)

# imprime la posición [0] de la lsita datos
print (datos[0])

# imprime la posición [4], tambien se puede utilizaar la pocisión [-1]

print (datos[-1])

# Mostar datos por Slicing
print (datos[0:2])
print (datos[-4:-1])
print (datos[1:4])

# Suma de listas
listas = numeros + datos
print (listas)

# Mutabilidad
pares = [0, 2, 4, 5, 6, 8, 10]
print (pares)
pares[3] = 144
print ('Pares:', pares)

# funciones o metodos de listas
# la función .append() sirve para agregar un elemento al final de la lista
qty = len(pares)
pares.append(12)
print ('Cantidad de datos:', qty)
print ('Lista actulizada:', pares)

# La función .index() sirve para mostrar la posición del elemento en la lista.
print (pares.index(144))

# La función .count() indica cuantas veces se repite un elemento.
pares.append(0)
print (pares.count(0))
print (pares)

# La función .remove() quita un elemento de una lista.
pares.remove(0)
print (pares)

# La función .reverse() invierte los elementos de una lista.
pares.reverse()
print (pares)
