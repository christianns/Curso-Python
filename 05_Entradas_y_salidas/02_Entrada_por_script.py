'''
Entrada por script
Hasta ahora todo lo que hemos hecho ha sido escribir código en el intérprete,
pero los programas informáticos no funcionan así. Se basan en escribir todas
las instrucciones en ficheros llamados scripts (o guiones de instrucciones).
Luego se envía este fichero al intérprete desde la terminal (si es un lenguaje
interpretado como Python) y éste ejecutará todas las instrucciones en bloque.

A parte de ser la base de los programas, la gracia de los Scripts es que pueden 
recibir datos desde la propia terminal en el momento de la ejecución,
algo muy útil para añadirles dinamismo.

Para poder crear y ejecutar scripts hace falta un editor y una terminal,
por suerte Anaconda trae el editor Spyder y el intérprete es accesible a través
de la terminal Anaconda Prompt, ambos programas accesibles desde Inicio
(o con Anaconda Navigator si utilizáis Linux/MAC).
'''

import sys
# print (sys.argv)
# print ('Hola')

# python3 02_Entrada_por_script.py 'Christian' 5 -0.1
# ['02_Entrada_por_script.py', 'Christian', '5', '-0.1']
# Hola

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print (texto)
else:
    print ('Error - Introduzca los argumentos correctamente')
    print ('Por ejemplo: archivo.py <arg1> <arg2>')
