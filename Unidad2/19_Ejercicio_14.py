# Problema 14: Dado un número entero, obtén la tabla de multiplicación de número ingresado.
# Análisis: Para la solución de este problema, se requiere que tenga un menú para
# sacar la multiplicación o salir del programa luego de la opción el usuario
# ingrese un número y el sistema realice una tabla de multiplicar.

while True:
    print ("\nTABLA DE MULTIPLICAR")
    print ("1 - Imprime la tabla de multiplicar")
    print ("2 - salir")

    opcion = int(input("Ingrese opcion: \n"))

    if opcion == 1:
        n = int(input("Ingrese el numero para realizar tabla: \n"))
        c = 0
        while c <= 10:
            r = n * c
            print ("|",n,"x",c,"=",r,"|")
            c+=1
    elif opcion == 2:
        print ("Terminando programa \n")

        break
    else:
        print ("Opcion incorrecta \n")
