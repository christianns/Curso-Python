# Diccionarios.
# Son junto a las listas las colecciones más utilizadas y se basan en una
# estructura mapeada donde cada elemento de la colección se encuentra
# identificado con una clave única, por lo que no puede haber dos claves iguales.
# En otros lenguajes se conocen como arreglos asociativos.

# Los diccionarios se definen igual que los conjuntos, utilizando llaves,
# pero también se pueden crear vacíos con ellas:

datos = {} # Diccionario vacio.

# Para cada elemento se define la estructura clave:valor

datos ={'blue': 'azul', 1: 'Uno', 2:'Dos'}
print (datos)
print (datos[1]) # Muestra la clave de la posición 1.
print (type(datos))

# Mutabilidad
# Los diccionarios son mutables, por lo que se les puede añadir
# elementos sobre la marcha a través de las claves:

datos ['Verde'] = "Green" # Agrega una clave y un valor
print (datos)

datos [1] = "UNO" # Reemplaza en valor.
print (datos)

del(datos['blue']) # Sirve para borrar un elemento del diccionario
print (datos)

# Una utilidad de los diccionarios es que podemos trabajar directamente
# con sus registros como si fueran variables:

edades = {'Hector':27,'Juan':45,'Maria':34}
edades['Hector']+=1
print (edades)

# Lectura secuencial
# Es posible utilizar iteraciones for para recorrer los elementos del diccionario:
# Muesta las claves del diccionario secuencialmente
for d in datos:
    print (d)

# Muesta las valores del diccionario secuencialmente
for clave in datos:
    print (datos[clave])

# El método .items() nos facilita la lectura en clave y valor de los elementos.
# Devuelve ambos valores en cada iteración automáticamente y nos permite almacenarlos:

for clave, valor in datos.items(): # Metodo .items permite leer
    print (clave,'-', valor)

# Lista de Diccionarios
# El método .items() nos facilita la lectura en clave y valor de los elementos.
# Devuelve ambos valores en cada iteración automáticamente y nos permite almacenarlos:

personajes = [] # Lista vacia

Gandalf = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
Legolas = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
Gimli = {'Nombre':'Gilmi','Clase':'Guerrero','Raza':'Enano'}

personajes.append(Gandalf)
personajes.append(Legolas)
personajes.append(Gimli)

# Muestra la lista de diccionarios
print (personajes)

# Mostras por partes
for personaje in personajes:
    print (personaje['Nombre'], '-', personaje['Clase'], '-', personaje['Raza'])
