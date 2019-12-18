'''
Ejercicio 4: Realizar una función llamada recortar (numero, minimo, maximo) que reciba tres parámetros.
El primero es el número a recortar, el segundo es el límite inferior y
el tercero el límite superior. La función tendrá que cumplir lo siguiente:
 * Devolver el límite inferior si el número es menor que éste
 * Devolver el límite superior si el número es mayor que éste.
 * Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10.
'''
numero = int(input('Ingrese 1er digito:\n'))
minimo = int(input('Ingrese 2do digito:\n'))
maximo = int(input('Ingrese 3er digito:\n'))

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print (recortar(numero, minimo, maximo))
