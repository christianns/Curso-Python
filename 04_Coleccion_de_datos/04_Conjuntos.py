# CONJUNTOS
# Los conjuntos es un almacenador de datos "desodenado".
# Son colecciones desordenadas de elementos únicos utilizados para hacer
# pruebas de pertenencia a grupos y eliminación de elementos duplicados.


# Conjunto vacio
conjunto = set ()
print (conjunto)

# Definición de un conjunto
conj = {1, 2, 3}
print (conj)

# funcion .add sierve para agregar un dato
conj.add(4)
conj.add(0)
conj.add('H')
conj.add('a')
conj.add('Z')
conj.add('A')
conj.add('H') # Los datos repetidos no se muestran en un congunto
print (conj)

# La funcion .discard quita elementos de un conjunto (solo si existe)

conj.discard(4)
conj.discard('H')
conj.discard('i') # Omite esta sentencia, ya que no existe dicho elemento.
print (conj)

# La funcion .remove quita datos de un conjunto (Si el elemento no exista provocará un error)
conj.remove('A')
conj.remove(1)
conj.remove(0)
# conj.remove(i) # Causa un error dado que el elemento no existe
print (conj)

# la función .clear limpia completamente el conjunto
conj.clear()
print (conj)

# Datos print (pertenecia en un conjunto)
nombres = {'Vicente', 'Vicente', 'Vicente'}
print ('Vicente' in nombres) # True
print ('Andrés' in nombres)  # False
print ('Vicente' not in nombres ) # False
print ('Andres' not in nombres) # True
print (nombres) # No imprime datos repetido

# Conversión con listas en conjuntos
lista = [1,'e',3,4,5,5,1]
print (lista)

conjunto = {1,'A', 'Hola', 0.5} # Define un conjunto
print (conjunto)

conjunto = set(lista) # La lista se convierte en conjunto
print (conjunto)

lista = list(conjunto) # Convierte el conjunto en lista
print (lista)

# Otra forma de manipular listas
lista1 = [1, 'ñ', 'A', 0.5, 1, 100, 'ñ', 'ñ']
print (lista1)

lista1 = list(set(lista1)) # Convierte la lista en conjunto (set) y luego a lista.
print (lista1)

# Conversion de cadena de caracteres

cadena = 'Hola mundo de cadenas'
print (set(cadena)) # Convierte la cadena de caracteres en conjunto

print (list(cadena)) # Convierte la cadena de caracteres en listas

cj = (list(set(cadena))) # Convierte la cadena de caracteres en conjuto y luego en lista.
print (cj)
