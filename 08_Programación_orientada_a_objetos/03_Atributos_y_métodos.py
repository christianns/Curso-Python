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
    chocolate = False # Con True aplica el else:

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")

# Por lo menos de esta forma nos aseguraremos de que el atributo chocolate existe
# en todas las galletas desde el principio. Además es posible consultar el valor
# por defecto que deben tener las galletas haciendo referencia al atributo en la definición de la clase:

print(Galleta.chocolate)

# Lo curioso es que si cambiamos ese atributo de clase (que no de objeto) a True,
# las siguientes galletas se crearán con chocolate, es decir, habremos modificado
# las instrucciones de creación de los objetos:

class Galleta:
    chocolate = False

Galleta.chocolate = True

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")

# Métodos

# Si por un lado tenemos las "variables" de las clases, por otro tenemos sus "funciones",
# que evidentemente nos permiten definir funcionalidades para llamarlas desde las instancias.
# Definir un método es bastante simple, sólo tenemos que añadirlo en la clase y
# luego llamarlo desde el objeto con los paréntesis, como si de una función se tratase:

'''
class Galleta:
    chocolate = False

    def saludar():
        print("Hola, soy una galleta muy sabrosa")

galleta = Galleta()
galleta.saludar()
'''
# Sin embargo, al intentar ejecutar el código anterior desde una galleta veréis que no funciona.
# Nos indica que el método saludar() requiere 0 argumentos pero se está pasando uno.
# ¿Cómo puede ser? Si en ningún momento hemos enviado ninguna información a al galleta...
# Lo que tenemos aquí, estimados alumnos, es la diferencia fundamental entre métodos de clase y métodos de instancia.

# Probad a ejecutar el método llamando a la clase en lugar del objeto:
class Galleta:
    chocolate = False

    def saludar():
        print("Hola, soy una galleta muy sabrosa")

Galleta.saludar()

# Primer argumento self
# Los objetos tienen una característica muy importante: son conscientes de que existen. Y no, no es broma.
# Cuando se ejecuta un método desde un objeto (que no desde una clase), se envía un
# primer argumento implícito que hace referencia al propio objeto.
# Si lo definimos en nuestro método podremos capturarlo y ver qué es:

class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)

galleta = Galleta()
galleta.saludar()

# ¿Curioso que haya funcionado verdad? Además ¿no os suena de algo ese resultado
# que muestra el parámetro que hemos definido? Se trata de la propia representación del objeto.

class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)

galleta = Galleta()
galleta.saludar()
print(galleta)
