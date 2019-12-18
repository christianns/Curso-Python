# Ejercicio 2 - Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica
# en un mensaje al usuario la causa y/o solución:

lista = [1, 2, 3, 4, 5]
try:
    print (lista[10])
    print ('Se ha detectado un error, indice fuera de rango')
except IndexError:
    print ('Ingrese un indice dentro del rango de la lista.') 
