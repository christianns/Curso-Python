# Ejercicio 3 - Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica
# en un mensaje al usuario la causa y/o solución:

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }

try:
    print (colores['blanco'])
    print ('Se ha detectado un error, indice fuera de rango')
except KeyError:
    print ('La clave no existe.')
