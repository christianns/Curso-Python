# En la colas, se puede encolar (poner un dato al final de una lista) y
# desencolar (sacar un dato del principio de una lista) - fifo (first in first out)

from collections import deque # importar función

cola = deque() # Una cola vacia

cola = deque(["Christian", 'Paola', 'Vicente'])
print (cola)

cola.append('León') # Agrega dato al final
cola.append('Andrés') # Agrega dato al final
print (cola)

cola.popleft() # Quita el dato de ka izquerda
print (cola)

nombre = cola.popleft()
print (nombre)
