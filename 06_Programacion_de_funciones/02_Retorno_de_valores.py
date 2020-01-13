# Retorno de valores
# Para comunicarse con el exterior, las funciones pueden devolver valores
# al proceso principal gracias a la instrucción return.

# En el momento de devolver un valor, la ejecución de la función finalizará:

# Ejemplo de retorno de una cadena de caracteres
def ejemplo ():
    return 'Cadena retornada'

print (ejemplo())


# Ejemplo de retorno de un entero
def ejemplo1 ():
    return 2345

print (ejemplo1())

'''
Por ejemplo no podemos sumar una cadena con un número:
c = test() + 10
'''

# También podemos devolver cualquier tipo de colección y manejarla directamente:
def test():
    return [1,2,3,4,5]

print(test())
print(test()[-1])
print(test()[1:4])

# Evidentemente es posible asignar el valor retornado a una variable:
lista = test()
print(lista[-1])

# Retorno múltiple
# Ejemplo de retorno de una tupla
def ejemplo2():
    return (100, 'hola', [1,2,3],-50, 100, 10.3, 'hola')

print (ejemplo2())
print (ejemplo2()[0:3]) # Retorna la posion 0 a la 3 de la tupla
print (ejemplo2()[0])
print (ejemplo2()[2])
