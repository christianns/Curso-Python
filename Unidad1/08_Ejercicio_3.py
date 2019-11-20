# Problema 03: Dado el valor de venta de un producto, hallar el
# IGV (18%) y el precio de venta.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese el valor de venta del producto por teclado y el
# sistema realice el cálculo respectivo para hallar el IGV y el
# precio de venta.

# Opcion 1
# valor_producto = int(input("Ingrese valor del producto:"))
# print (valor_producto)

# Opcion 2
print ("Ingrese valor del producto:")
valor_producto = int(input())
IVA = valor_producto * 0.18
valor_venta = valor_producto + IVA
print ("El IVA es:",int(IVA))
print ("El precio de venta es:", int(valor_venta))
