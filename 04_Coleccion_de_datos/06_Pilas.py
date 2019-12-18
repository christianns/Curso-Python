# En python no existen las pilas pero se pueden simular con listas
# Se puede agregar un solo datos al final de una lista y quita el del finalmente
 
pila = ['auto', 3, 4, 5]
pila.append(6) # Agrega al final de la lista el 6
pila.append(7) # Agrega después del 6 el 7
print (pila)

print(pila.pop()) # Quita el ultimo datos
print (pila)      # ya no existe en la lista

numero = pila.pop() # Guarda el ultimo dato en una variable
print (numero)

# Quita todos los datos y finalmente que una lista vacia [].
pila.pop()
pila.pop()
pila.pop()
pila.pop()
print (pila)
