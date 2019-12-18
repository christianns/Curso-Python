# Una funcion tambien puede retornar valores.
# pora esto se utiliza la funion return

# Ejemplo de retorno de una cadena de caracteres
def ejemplo ():
    return 'Cadena retornada'

print (ejemplo())


# Ejemplo de retorno de un entero
def ejemplo1 ():
    return 2345

print (ejemplo1())

# Ejemplo de retorno de una tupla
def ejemplo2():
    return (100, 'hola', [1,2,3],-50, 100, 10.3, 'hola')

print (ejemplo2())
print (ejemplo2()[0:3]) # Retorna la posion 0 a la 3 de la tupla
print (ejemplo2()[0])
print (ejemplo2()[2])
