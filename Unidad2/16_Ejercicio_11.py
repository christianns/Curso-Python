# Problema 11: Hacer un menú de opciones de un 1 a 4 y la opción salir para salir del programa, como se muestra la tabla y al
# ingresar un número entre 1 y 4 devolver la estación del año y con la opción salir se termine la ejecución.
# Análisis: Para la solución de este problema, se requiere que usuario ingrese un numero entero y es sistema realice el proceso
# para devolver la estación o salir del sistema.

while True:
    print ("ESTACIONES DEL AÑO")
    print ("Ingrese un digito del 1 al 4")
    print ("Ingrese 5 para salir del sistema")
    n1 = int(input())
    if n1 == 1:
        print ("Varano")
    elif n1 == 2:
        print ("Otoño")
    elif n1 == 3:
        print ("Invierno")
    elif n1 == 4:
        print ("Primavera")
    elif n1 == 5:
        print ("Saliendo del sistema")
        break
    else:
        print ("Codigo incorrecto")
