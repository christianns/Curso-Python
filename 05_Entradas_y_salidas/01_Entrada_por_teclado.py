# Entrda por teclado input()
# El inconveniete es que se debe convertir el dato de numerico a string

# Almacenar dato ingresado en una variable
decimal = float(input('Ingrese numero decimal:'))
print (decimal)

# Agregar valores a lista
valores = []  # Lista en blanco
print ('Introcucion 3 valores:\n')

for x in range(3):
    valores.append(input('Introduce valores para agregar a la lista:\n'))
    print (valores)

# Lista vacia
lista = []
c = int(input('Ingrese cantidad de Item:')) # Indica la cantidad de item para asigna a la lista.
for x in range(c):
    lista.append(input('Ingrese valor:')) # input, entrada por teclado
print (lista)
