# Problema 05: Hallar la radicación de , donde a y n pertenecen
# a números enteros positivos.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese el valor de a y n por teclado y el sistema
# realice el cálculo respectivo y obtenga la radicación r.
# Expresión Algorítmica: r = a ^ (1/n)

print ("Ingrese valar de a:")
a = int(input())
print ("Ingrese valar de n:")
n = int(input())
rad = a ** (1/n)
print ("El radical n de a es:", rad)
