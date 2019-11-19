# Este es un ejemplo de una cadena de caracteres o string
# Las comillas simple ('') definen una cadena, al igual que las comillas dobles ("")
nombre = 'Christian'
print (nombre)

nombre_apellido = "Christian Andres"
print (nombre_apellido)

# Con las comillas triples simples ('''''') se pueden escribir en mas de una linea
nombre_completo = '''Christian
Andres
Navarrete
Silva'''
print (nombre_completo)

# Las cadenas de escape sirven para saltar una linea
cadena = "Este es una \ncadena de escape \nla cual me permite \nescribir en \nmultiples lineas"
print (cadena)

#La cadena de escape "tabulador" se definie de la siguinete manera
cadena1 = "Este es \t tabulador"
print (cadena1)

cadena2 = "Esta cadena \rno muestra lo anterior 'Esta cadena'"
print (cadena2)

# Este ejemplo cadena de tipo formateo
# %s cadena de tipo caractere
# %d enteros
# %f float

n = "Christian"
e = 37
p = 70.91

print ("Nombre: %s Edad: %d Peso: %f" %(n, e, p))

nombre = "Christian Andes"
edad = 38
peso = 72.12

print ("Nombre: %s \nEdad: %d \nPeso: %f" %(nombre, edad, peso))
