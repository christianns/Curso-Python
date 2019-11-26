# Problema 13: Dado un rango de números enteros, obtén la cantidad
# de números pares que contiene.
# Análisis: Para la solución de este problema, se requiere que usuario ingrese número inicial y final,
# luego el sistema procese y devuelva la cantidad de números pares que contiene el rango.

numero_inicial = None
numero_final = None
cuenta = -1
numeros_pares = None

print ("Ingrese numero inicial")
numero_inicial = int(input())
print ("Ingrese numero final")
numero_final = int(input())

while numero_final > numero_inicial:
        numero_inicial = numero_inicial + 1
        cuenta = cuenta + 1
        if numero_inicial == numero_final:
            numeros_pares = numero_final // 2
            print ("La cantidad los enteros entre los numero ingresados es:", str(int(cuenta)))
            print ("La cantidad de nuemros pares es:", str(input(numeros_pares)))
            print ("La cuenta a terminado")
