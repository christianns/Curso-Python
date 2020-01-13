'''
Pilas
Son colecciones de elementos ordenados que únicamente permiten dos acciones:
    - Añadir un elemento a la pila.
    - Sacar un elemento de la pila.

La peculiaridad es que el último elemento en entrar es el primero en salir.
En inglés se conocen como estructuras LIFO (Last In First Out).

Las podemos crear como listas normales y añadir elementos al final con el append():

# En python no existen las pilas pero se pueden simular con listas
'''
# Las podemos crear como listas normales y añadir elementos al final con el append():
pila = ['auto', 3, 4, 5]
pila.append(6) # Agrega al final de la lista el 6
pila.append(7) # Agrega después del 6 el 7
print (pila)

# Para sacar los elementos utilizaremos el método pop().
print(pila.pop()) # Quita el ultimo datos
print (pila)      # ya no existe en la lista

# Si queremos trabajar con él deberíamos asignarlo a una variable
numero = pila.pop() # Guarda el ultimo dato en una variable
print (numero)

# Quita todos los datos y finalmente que una lista vacia [].
pila.pop()
pila.pop()
pila.pop()
pila.pop()
print (pila)
