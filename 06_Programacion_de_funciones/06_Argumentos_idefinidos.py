'''
Argumentos indeterminados o indefinidos

Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a
enviar a una función. En estos casos podemos utilizar los parámetros
indeterminados por posición y por nombre.
'''

# Argumentos indeterminados
# Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar
# a una función. En estos casos podemos utilizar los parámetros indeterminados
# por posición y por nombre.

# Este ejemplo recive una cantidad indeterminada de valores por pocision
def ejemplo (*args):
    for i in args:
        print (i)

ejemplo('hola')
ejemplo('hola', [1,'cadena', 3.05], 5.23)

# Por nombre
# Para recibir un número indeterminado de parámetros por nombre
# (clave-valor o en inglés keyword args), debemos crear un diccionario dinámico
# de argumentos definiendo el parámetro con dos asteriscos:

# Este ejemplo recive una cantidad indeterminada de valores por nombre.
def argumentos_por_nombre (**kwargs):
    print (kwargs)

argumentos_por_nombre(a = 'Christian', e = 37) # Almecena como un diccionario

# Por posición y nombre
# Si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos
# crear ambas colecciones dinámicas. Primero los argumentos indeterminados por
# valor y luego los que son por clave y valor:

# Este ejemplo recive una cantidad indeterminada de valores por valores y nombre.
def argumentos_por_nombre_posicion (*args, **kwargs):
    print (args, kwargs)

argumentos_por_nombre_posicion(2, 4, 'auto', n = 'hola', e = 34,)

'''
Los nombres args y kwargs no son obligatorios, pero se suelen utilizar por convención.
Muchos frameworks y librerías los utilizan por lo que es una buena practica llamarlos así.
'''
