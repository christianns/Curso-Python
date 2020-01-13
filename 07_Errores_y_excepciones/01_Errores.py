'''
Errores

Los errores detienen la ejecución del programa y tienen varias causas.
Para poder estudiarlos mejor vamos a provocar algunos intencionadamente.
'''

# Errores de sintaxis - SyntazError
print("Hola"

# Errores por nombre - NameError
pint("Hola")

# Errores semánticos
# Estos errores son muy difíciles de identificar porque van ligados al
# sentido del funcionamiento y dependen de la situación. Algunas veces
# pueden ocurrir y otras no.

# La mejor forma de prevenirlos es programando mucho y
# aprendiendo de tus propios fallos, la experiencia es la clave. Veamos un par de ejemplos:

# Ejemplo .pop() con lista vacía
# Si intentamos sacar un elemento de una lista vacía,
# algo que no tiene mucho sentido, el programa dará fallo de tipo IndexError.
# Esta situación ocurre sólo durante la ejecución del programa, por lo que
# los editores no lo detectarán:

l = []
l.pop()

# Para prevenir el error deberíamos comprobar que una lista tenga como
# mínimo un elemento antes de intentar sacarlo, algo factible utilizando la función len():

l = []
if len(l) > 0:
    l.pop()

# Ejemplo lectura de cadena y operación sin conversión a número
# Cuando leemos un valor con la función input(),
# éste siempre se obtendrá como una cadena de caracteres.
# Si intentamos operarlo directamente con otros números tendremos un
# fallo TypeError que tampoco detectan los editores de código:
n = input("Introduce un número: ")
print("{}/{} = {}".format(n,m,n/m))

 # Sin embargo no siempre se puede prevenir, como cuando se introduce una cadena que no es un número:
n = float(input("Introduce un número: "))
m = 4
print("{}/{} = {}".format(n,m,n/m))

# Como podéis suponer, es difícil prevenir fallos que ni siquiera nos habíamos
# planteado que podían existir. Por suerte para esas situaciones existen las excepciones.
