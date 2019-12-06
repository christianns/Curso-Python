'''
Este envia valor mediente scripts con argumentos, para ello se
utiliza la libreria sys y con listas argv que almacena argumentos a un scrips
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
