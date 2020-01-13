# Ejercicio 21
# Encontar la distancia mas cerca de una ambulancia respecto a nuestra posicion.
# Se debe ingresar por teclado cada posicion tanto la nuestra como la de las n ambulancias.


cantidad_ambulancia = int(input('Ingrese la cantidad de ambulancias:\n'))
cordX1 = float(input('Ingrese coordenada X de su posición:\n'))
cordY1 = float(input('Ingrese coordenada Y de su posición:\n'))


# print (cordX1,cordY1)
# print (range(cantidad_ambulancia))

lista =[]
lista_cord = []
for i in range(cantidad_ambulancia):
    cordX2 = float(input('Ingrese la coordenada X de la ambulancia ' + str(i + 1) + '\n'))
    cordY2 = float(input('Ingrese la coordenada Y de la ambulancia ' + str(i + 1) + '\n'))
    distancia = ((cordX1 - cordX2)**2 + (cordY1 - cordY2)**2)**0.5 # distancia entre dos puntos (posicion y ambulancia)
    lista.append(distancia)
    lista_cord.append([cordX2, cordY2])
    # print (lista)
    # print (lista_cord)
    min_dist = min(lista)
    min_cord = min(lista_cord)
print ('La distancia de la ambulancia mas cerca respecto a su posicion es:', min_dist , 'y sus cordenadas son', min_cord)
