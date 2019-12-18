# El bloque de codigo llamado funcion puede ser 'llamado' por un nombre.

# Ejemplo 1
def nombre_funcion(): # Define una funcion
    print ('Esta es una funcion.')
nombre_funcion() # llama a la funcion

# Ejemplo 2
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
