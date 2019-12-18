# Ejercicio 1 - Localiza el error en el siguiente bloque de codigo.
# Cree un excepción para evitar que el programa se bloquee y además explica en
# mensaje al usuario la cuasa y/o solucion.
# resultado = 10/0

while True:
    try:
        resultado = 10 / 0
        print ('Se ha detectado un error' + resultado)
    except ZeroDivisionError:
        print ('No se puede dividir por cero, intente con otro numero')
        c = int(input('Ingrese un nuevo digito: \n'))
        resultado = 10 / c
        print (resultado)
