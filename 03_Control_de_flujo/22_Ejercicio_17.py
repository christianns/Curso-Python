# Ejercicio 2
# Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
'''
num = int(input('Ingrese un numero:\n'))

while num % 2 == 0:
        print ('Ingrese otro numero:\n')
        break
else:
    print ('El numero es impar\n')
'''

numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: "))
