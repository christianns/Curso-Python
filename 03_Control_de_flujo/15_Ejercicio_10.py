# Problema 10: Debido a los excelentes resultados, el restaurante
# decide ampliar sus ofertas de acuerdo a la siguiente escala de
# consumo. Ver la tabla. Determinar el monto del descuento, el impuesto y el importe a pagar.
# Análisis: Para la solución de este problema, se requiere que usuario ingrese el consumo y
# es sistema verifica y calcula el monto del descuento, el impuesto y el monto a pagar.
# Consumo <= 100 descunto 10%
# Consumo > 100 and <= 200 descuento 20%
# Consumo > 200 descuento 30%

valor_iva = 0.19
desc_10 = 0.10
desc_20 = 0.20
desc_30 = 0.30

print ("Ingrese valor consumo:")
valor_consumo = int(input())
# Calcula la cuenta para consumos menores o iguales a 100000
if valor_consumo <= 100000:
    valor_con_iva = valor_consumo + (valor_consumo * valor_iva)
    valor_con_desc = valor_con_iva - (valor_con_iva * desc_10)
    print ("Su cuenta es:", str(int(valor_con_desc)))
# Calcula la cuenta para consumos mayoes a 100000 y menores a 200000
if valor_consumo > 100000 and valor_consumo <= 200000:
    valor_con_iva = valor_consumo + (valor_consumo * valor_iva)
    valor_con_desc = valor_con_iva - (valor_con_iva * desc_20)
    print ("Su cuenta es:", str(int(valor_con_desc)))
# Calcula la cuenta para consumos mayores a 200000
if valor_consumo > 200000:
    valor_con_iva = valor_consumo + (valor_consumo * valor_iva)
    valor_con_desc = valor_con_iva - (valor_con_iva * desc_30)
    print ("Su cuenta es:", str(int(valor_con_desc)))
