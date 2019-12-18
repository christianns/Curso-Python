# Argumentos indeterminados

# Este ejemplo recive una cantidad indeterminada de valores por pocision
def ejemplo (*args):
    for i in args:
        print (i)

ejemplo('hola')
ejemplo('hola', [1,'cadena', 3.05], 5.23)

# Este ejemplo recive una cantidad indeterminada de valores por nombre.
def argumentos_por_nombre (**kwargs):
    print (kwargs)

argumentos_por_nombre(a = 'Christian', e = 37) # Almecena como un diccionario

# Este ejemplo recive una cantidad indeterminada de valores por valores y nombre.
def argumentos_por_nombre_posicion (*args, **kwargs):
    print (args, kwargs)

argumentos_por_nombre_posicion(2, 4, 'auto', n = 'hola', e = 34,)
