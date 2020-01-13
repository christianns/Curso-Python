'''
Envío de valores

Para comunicarse con el exterior las funciones no sólo pueden
devolver valores, también pueden recibir información:
'''

# Ejemplo de envio y retorno de valores.
def suma(a, b):
    r = a + b # tambien se puede definir de la siguiente manera return a + b
    return r

resultado = suma(34, 8)
print(resultado)
