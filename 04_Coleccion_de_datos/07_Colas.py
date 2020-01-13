'''
Colas
Son colecciones de elementos ordenados que únicamente permiten dos acciones:
 - Añadir un elemento a la cola.
 - Sacar un elemento de la cola.
La peculiaridad es que el primer elemento en entrar es el primero en salir.
En inglés se conocen como estructuras FIFO (First In First Out).
'''

# Debemos importar la colección deque manualmente para crear una cola:
from collections import deque # importar función

cola = deque() # Una cola vacia

# Podemos añadir elementos al crear la cola pasándolos en una lista:
cola = deque(["Christian", 'Paola', 'Vicente'])
print (cola)

# Luego podemos seguir añadiéndolos utilizando el método append():
cola.append('León') # Agrega dato al final
cola.append('Andrés') # Agrega dato al final
print (cola)

# La parte interesante es a la hora de sacar los elementos,
# pues en esta ocasión utilizaremos el método popleft().
# Hace lo mismo que pop() pero los extrae por la parte izquierda, que sería el principio de la cola:

cola.popleft() # Quita el dato de la izquerda
print (cola)

# Además al igual que antes debemos asegurarnos de almacenar los elementos al sacarlos o los perderemos:
nombre = cola.popleft()
print (nombre)
