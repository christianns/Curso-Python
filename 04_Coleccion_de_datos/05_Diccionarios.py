# Diccionarios, el diccionario puede contener valores o ser vacio.
datos = {} # Diccionario vacio.

datos ={'blue': 'azul', 1: 'Uno', 2:'Dos'}
print (datos)
print (datos[1]) # Muestra la clave de la posición 1.

datos ['Verde'] = "Green" # Agrega una clave y un valor
print (datos)

datos [1] = "UNO" # Reemplaza en valor.
print (datos)

del(datos['blue']) # Elimina el data/clave
print (datos)

# Muesta las claves del diccionario secuencialmente
for d in datos:
    print (d)

# Muesta las valores del diccionario secuencialmente
for clave in datos:
    print (datos[clave])

# Concadena en diccionarios
for clave, valor in datos.items(): # Metodo .items permite leer
    print (clave,'-', valor)

# Lista de Diccionarios
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
