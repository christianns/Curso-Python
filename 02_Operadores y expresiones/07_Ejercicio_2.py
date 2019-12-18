# Problema 02: Hallar el cociente y residuo (resto) de dos números
# enteros.
# Análisis: Para la solución de este problema, se requiere que
# ingrese dos números entero por teclado y el sistema realice el
# cálculo respectivo para hallar el cociente y residuo.

a = int(input("Ingrese primer dígito:"))
print (a)
b = int(input("Ingrese segundo dígito:"))
cuo = a // b
res = a % b
print ("El cuociente es:", cuo)
print ("El resto es:", res)
