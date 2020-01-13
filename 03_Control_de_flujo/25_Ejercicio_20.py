# Ejercicio 5
# Realiza un programa que pida al usuario un número entero del 0 al 9,
# y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

num = int(input('Ingrese un munero entero entre el 0 y el 9:\n'))
while num < 0 or num > 9:
    num = int(input('Ingrese un munero entero entre el 0 y el 9:\n'))
    print ('==================================')
    print ('El numero ingresado no corresponde')
    print ('Intentelo nuevamente')
    print ('==================================')
else:
    print ('El numero ingresado es: ', num)
