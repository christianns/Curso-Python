# TEXTO

print ('Este texto incluye unas " "') # Es posible poner comillas dobles en una cadena de comillas simples

print ("Esta 'palabra' se encuentra escrita entre comillas simples") # Comillas simples en una cadena de comillas dobles

print ("Esta \"palabra\" se encuentra escrita entre comillas dobles") # carácter de escape \ para poner comillas del mismo tipo

# tabulaciones \t o los saltos de línea \n
print("Un texto\tuna tabulación")
print("Un texto\nuna nueva línea")

# Para evitar los caracteres especiales, debemos indicar que una cadena es cruda (raw):

print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)

# utilizar """ (triple comillas) para cadenas multilínea
print("""Una línea
otra línea
otra línea\tuna tabulación""")

# Operaciones
# suma de cadenas
c = "Esto es una cadena\ncon dos líneas"
print(c+c)

s = "Una cadena" " compuesta de dos cadenas"
print(s)

c1 = "Una cadena"
c2 = "otra cadena"
print("Una cadena " + c2)

diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")

# Índices en las cadenas

palabra = "Python"
print (palabra[0]) # carácter en la posición 0
print (palabra[-1])
print(palabra[-0])
print(palabra[-2])
print(palabra[-6])

# Slicing en las cadenas
# El slicing es una capacidad de las cadenas que devuelve un subconjunto o
# subcadena utilizando dos índices [inicio:fin]:
# * El primer índice indica donde empieza la subcadena (se incluye el carácter).
# * El segundo índice indica donde acaba la subcadena (se excluye el carácter).

palabra = "Python"
print(palabra[0:2])
print(palabra[2:])
print (palabra[-2:])
# Si en el slicing no se indica un índice se toma por defecto el principio y el final:
print (palabra[:2])
print (palabra[2:])
print (palabra[:])
print (palabra[:2] + palabra[2:])

# Si un índice se encuentra fuera del rango de la cadena, dará error¡
''' print (palabra[99])
'''

# Pero con slicing esto no pasa y simplemente se ignora el espacio hueco
print (palabra[:99])

# INMUTABILIDAD
# Una propiedad de las cadenas es que no se puede modificar su contenido. Si intentamos reasignar un carácter, no nos dejará:
''' palabra[0] = "N"
    print(palabra[0])
'''
# Sin embargo, utilizando slicing y concatenación podemos generar nuevas cadenas fácilmente.
palabra = "N" + palabra[1:]
print (palabra)

# FUNCIONES
# Un ejemplo de función útil que soportan las cadenas es len(),
# que nos permite saber su longitud (el número de caracteres que contienen).

palabra = "Python"
len(palabra)
print (len(palabra))

# Función .type()
print (type("Hola Mundo")) # <class 'str'>
print (type([1, 10, 100])) # <class 'list'>
print (type(-25))          # <class 'int'>
print (type(1.167))        # <class 'float'>
print (type(["Hola", "Mundo"])) # <class 'list'>
