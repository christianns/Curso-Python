# variables
n1 = None
n2 = None
n_mayor = None

#Entrada
n1 = float(input("Ingrese primer número:"))
n2 = float(input("Ingrese segundo número:"))

#proceso
if n1 > n2:
    n_mayor = n1
elif n2 > n1:
    n_mayor = n2

#Salida
print ("El numero mayor es:", n_mayor)
