'''
Ejercicio 5: Realiza una función separar(lista) que tome una lista de números enteros
y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
Para ordenar una lista automáticamente puedes utilizar el método .sort().
numeros = [-12, 84, 13, 20, -33, 101, 9]
'''
num =  [-12, 84, 13, 20, -33, 101, 9]
def separar(x):
    x.sort()
    pares = []
    impares = []
    for n in x:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(num)

print(pares)
print(impares)
