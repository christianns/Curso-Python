'''
Definición y llamada
Se definen con la palabra reservada def, el nombre de la función y unos paréntesis,
que también se utilizan para hacer la llamada:
'''

# Ejemplo 1
def nombre_funcion(): # Define una funcion
    print ('Esta es una funcion.')
nombre_funcion() # llama a la funcion

# Ejemplo 2 - Dentro de una función podemos utilizar variables y sentencias de control:
def hola():
    c = 0 # Variable dentro de una funcion y es parte solo de esta funcion.
    global i # Con global se puede definir una variable para ser utilizada de manera global en el programa
    while c < 5:
        print ('Esta en una funcion con while')
        c += 1
    for i in range(1, 10):
        print ('este es un bucle for', i)
hola()
print (i)

# Ejemplo 3 - Dentro de una función podemos utilizar variables y sentencias de control:
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))

dibujar_tabla_del_5()


# Ámbito de las variables
# Una variable declarada en una función no existe en la función principal:
def test():
    n = 10
test()
print(n)

# Sin embargo, una variable declarada fuera de la función (al mismo nivel),
# sí que es accesible desde la función:
m = 10
def test():
    print(m)
test()

# Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:
def test():
    print(l)
l = 10
test()

# En el caso que declaremos de nuevo una variable en la función, se creará un
# copia de la misma que sólo funcionará dentro de la función.
# Por tanto no podemos modificar una variable externa dentro de una función:

def test():
    o = 5  # variable que sólo existe dentro de la función
    print(o)

o = 10  # variable externa, no modificable
test()
print(o)

# La instrucción global
# Para poder modificar una variable externa en la función,
# debemos indicar que es global de la siguiente forma:

def test():
    global o  # variable que hace referencia a la o externa
    o = 5
    print(o)

o = 10
test()
print(o)
