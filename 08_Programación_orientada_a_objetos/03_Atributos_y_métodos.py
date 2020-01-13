'''
Atributos y métodos

Si hay algo que ilustre el potencial de la POO esa es la capacidad de definir
variables y funciones dentro de las clases, aunque aquí se conocen como atributos
y métodos respectivamente.
'''

# Atributos

# A efectos prácticos los atributos no son muy distintos de las variables,
# la diferencia fundamental es que sólo existen dentro del objeto.

# Atributos dinámicos

# Dado que Python es muy flexible los atributos pueden manejarse de distintas formas,
# por ejemplo se pueden crear dinámicamente (al vuelo) en los objetos.

class Galleta:
    pass

galleta = Galleta()
galleta.sabor = "salado"
galleta.color = "marrón"

print(f"El sabor de esta galleta es {galleta.sabor} "
      f"y el color {galleta.color}")

# Atributos de clase

# Aunque la flexibilidad de los atributos dinámicos puede llegar a ser muy útil,
# tener que definir los atributos de esa forma es tedioso. Es más práctico definir
# unos atributos básicos en la clase. De esa manera todas las galletas podrían
# tener unos atributos por defecto:

class Galleta:
    chocolate = False

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")
