# Problema 09: Un restaurante ofrece un descuento del 10% para consumos de hasta $ 100.00
#  y un descuento de 20% para consumos mayores, para ambos caso se aplica un impuesto de 19%.
# Determinar el monto del descuento, el impuesto y el importe a pagar.
# Análisis: Para la solución de este problema, se requiere que
# usuario ingrese el consumo y es sistema verifica y calcula el
# monto del descuento, el impuesto y el monto a pagar.

valor_cuenta = None
IVA = 0.19
desc_10 = 0.10
desc_20 = 0.20

print ("Ingrese el valor de la cuenta:")
valor_cuenta = float(input())

if valor_cuenta <= 100000:
    print ("Consumo:", float(int(valor_cuenta)))
    valor_IVA = valor_cuenta * IVA
    print ("IVA:", float(int(valor_IVA)))
    desc_10 = valor_cuenta * 0.10
    print ("Descuento 10%:", float(int(desc_10)))
    valor_final = valor_cuenta + valor_IVA - desc_10
    print ("Total:" , float(int(valor_final)))

if valor_cuenta > 100000:
    print ("Consumo:", float(int(valor_cuenta)))
    valor_IVA = valor_cuenta * IVA
    print ("IVA:", float(int(valor_IVA)))
    desc_20 = valor_cuenta * 0.20
    print ("Descuento 20%:", float(int(desc_20)))
    valor_final = valor_cuenta + valor_IVA - desc_20
    print ("Total:" , flaot(int(valor_final)))
