# Ejercicio 16
# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
# * Mostrar una suma de los dos números
# * Mostrar una resta de los dos números (el primero menos el segundo)
# * Mostrar una multiplicación de los dos números
# * En caso de introducir una opción inválida, el programa informará de que no es correcta.

n1 = float(input('Ingrese 1er numero:\n'))
n2 = float(input('Ingrese 2do numero:\n'))

print("""Ingrese la opcion:
       1 - Suma los numeros
       2 - Resta los numeros
       3 - Multiplicación de los numeros
       4 - Salir""")
opcion = int(input("Ingrese la opcion:\n"))


if opcion == 1:
    print ('La suma de ambos numeros es: ', n1 + n2)
elif opcion == 2:
    resta = n1 - n2
    print ('La resta de ambos numeros es: ', resta)
elif opcion == 3:
    multiplicacion = n1 * n2
    print ('La multiplicacion de ambos numeros es: ', multiplicacion)
elif opcion == 4:
    print ('Gracias por participar :)')
else:
    print ('Ingrese un opcion valida')


'''
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0

print("""
¿Qué quieres hacer?
1) Sumar los dos números
2) Restar los dos números
3) Multiplicar los dos números
""")

opcion = int(input("Introduce un número: ") )

if opcion == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opcion == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")
'''
