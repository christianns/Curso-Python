'''
Ejercicio 1 Realiza una función llamada area_rectangulo(base, altura) que devuelva
el área del rectangulo a partir de una base y una altura.
Calcula el área de un rectángulo: su base y altura ingrese por teclado.

Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura.
'''

base = int(input('Ingrese base:\n'))
altura = int(input('Ingrese altura:\n'))

def area_rectangulo (base, altura):
    area = base * altura
    return area

print ('El area del rectangulo es: ' + str(area_rectangulo(base, altura)))
