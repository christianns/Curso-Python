# Problema 15: Realiza un sistema para controlar el ingreso a un cine, donde ofrezca
# películas de terror, acción y aventuras. En cada opción tenga restricción por edad.
# Categorías $      Edad (%)
# Terror            18 - 55
# Acción            10 a mas
# Aventura          4 a mas

# Análisis: Para la solución de este problema, se requiere que tenga un menú de opciones para
# elegir si desea terror, acción o aventura y se permita el ingreso de acuerdo a la edad.

while True:
    print ("=========================")
    print ("Bienvenido a Nuestro Cine")
    print ("=========================")
    print ("Elija la categoria: ")
    print ("1 - Terror")
    print ("2 - Acción")
    print ("3 - Infantil")
    print ("4 - Salir")
    opcion = int(input("Ingrese la opcion:"))
    if opcion == 1:
        edad = int(input("Ingrese su edad:"))
        if  edad >= 18 and edad <= 55:
            print ("====================")
            print ("Disfrute su pelicula")
            print ("====================\n\n")
        else:
            print ("============================================")
            print ("No tiene permitido acceder a ver la pelicula")
            print ("============================================\n\n")

    elif opcion == 2:
        edad = int(input("Ingrese su edad:"))
        if edad >= 10:
            print ("====================")
            print ("Disfrute su pelicula")
            print ("====================\n\n")
        else:
            print ("============================================")
            print ("No tiene permitido acceder a ver la pelicula")
            print ("============================================\n\n")
    elif opcion == 3:
        edad = int(input("Ingrese su edad:"))
        if edad >= 4:
            print ("====================")
            print ("Disfrute su pelicula")
            print ("====================\n\n")
        else:
            print ("============================================")
            print ("No tiene permitido acceder a ver la pelicula")
            print ("============================================\n\n")
    elif opcion == 4:
        print ("Grcias por visitarnos\n")
        break
    else:
        print ("Opcion no valida")
        print ("Intentelo nuevamente")
