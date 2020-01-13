# Sentencia for (para)

# for con listas
# Para ilustrar la utilidad de esta sentencia vamos a empezar mostrando como
# recorrer los elementos de una lista utilizando While:

numeros = [1, 2, 3, 4, 'hola', 6, 7, 8, 9, 10]

'''
count = 0
while count < len(numeros):
    print (numeros[count])
    count += 1
'''
# Listar numeros de una lista con for

for n in numeros:
    print (n)

# Listar cadenas de caracteres

cadena = 'hola mundo'
for dato in cadena:
    print (dato)

# Pero debemos recordar que las cadenas son inmutables:
'''
for i, c in enumerate(cadena):
    cadena[i] = "*"
'''
# Sin embargo siempre podemos generar una nueva cadena:
cadena = "Hola amigos"
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2

# Funcion de rago
for i in range(10):
    print (i)

for x in range(1,5):
    print (x)

# Si queremos conseguir la lista literal podemos transformar el range a una lista:
print (list(range(11)))

# Para asignar un nuevo valor a los elementos de una lista mientras la recorremos,
# podríamos intentar asignar al número el nuevo valor: La forma correcta
# de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:

indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numeros:
    numeros[indice] *= 10
    indice+=1
print (numeros)

# Podemos utilizar la función enumerate() para conseguir el índice y el valor
# en cada iteración fácilmente:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print (numeros)
