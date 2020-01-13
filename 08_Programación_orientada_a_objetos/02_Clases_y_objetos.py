'''
Clases y objetos

La base de la POO son los objetos.
Podéis imaginaros los objetos como un nuevo tipo de dato cuya definición viene
dada en una estructura llamada clase.
Suelo hacer una metáfora y comparar las clases con moldes de galletas y
los objetos con las galletas en sí mismas. Si bien todas las galletas que se
hacen con el mismo molde tienen la misma forma, cada una adquiere atributos individuales después del horneado.
Cosas como el color, la textura, el sabor... pueden llegar a ser muy distintas.
En otras palabras, las galletas comparten un proceso de fabricación y unos atributos,
pero son independientes entre ellas y del propio molde y eso hace que cada una sea única.
Extrapolando el ejemplo, una clase es sólo un guión sobre como deben ser los objetos que se crearán con ella.
'''

# La función type()
# Ya he comentado varias veces que en Python todo son clases y objetos,
# eso se puede comprobar fácilmente pasando a la función type() cualquier variable o literal:

numero = 10
type(numero) # int
print(type(numero)) # <class 'int'>

# En el código anterior numero es una variable entera, pero si vamos más allá,
# en realidad es una instancia del tipo int, una clase muy básica de dato para almacenar números enteros.

# Como curiosidad, incluso las funciones en Python son instancias del tipo function:
def hola():
    pass

type(hola)
print (type(hola)) # <class 'function'>

# Definición de clase
# La sintaxis es muy sencilla:
class Galleta:
    pass

# Esta es una definición muy simple de lo que es una galleta, ya que con el pass la dejo vacía.
# Luego añadiremos más información, por ahora veamos como crear galletas con este molde.

# Instancias de clase
# Para entender bien los objetos debemos tener claras dos cuestiones fundamentales:
# ¿Cuándo y dónde existen los objetos?
# Puede parecer trivial, pero es importante tener claro que los objetos "existen" sólo durante la
# ejecución del programa y se almacenan en la memoria del sistema operativo.
# Es decir, mientras las clases están ahí en el código haciendo su papel de instrucciones,
# los objetos no existen hasta que el programa se ejecuta y se crean en la memoria.
# Este proceso de "crear" los objetos en la memoria se denomina instanciación y para
# realizarlo es tan fácil como llamar a la clase como si fuera una función:

una_galleta = Galleta()
otra_galleta = Galleta()

# Demostrar que las galletas existen como "entes independientes" dentro de la memoria,
# es tan sencillo como imprimirlas por pantalla:

print(una_galleta)  # <__main__.Galleta object at 0x00000053697EE3C8>
print(otra_galleta) # <__main__.Galleta object at 0x00000053697EE248>

# Cada instancia tiene su propia referencia, demostrando que están en lugares distintos de la memoria.
# En cambio la clase no tiene una referencia porque es sólo un guión de instrucciones:

print(Galleta) # <class '__main__.Galleta'>

# Es posible consultar la clase de un objeto con la función type(),
# pero también se puede consultar a través de su atributo especial class:

print(Galleta)                # <class '__main__.Galleta'>
print(type(una_galleta))      # <class '__main__.Galleta'>
print(una_galleta.__class__)  # <class '__main__.Galleta'>

# A su vez las clases tienen un atributo especial name que nos devuelve su nombre en forma de cadena sin adornos:

print(Galleta.__name__)               # Galleta
print(type(una_galleta).__name__)     # Galleta
print(una_galleta.__class__.__name__) # Galleta
