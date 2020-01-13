# Condiciones - Selectiva simple
# Sentencia if (si)
# El if se ejecuta siempre que la expresión que comprueba devuelva True:
opcion  = True
if opcion:
    print ("Se cumple la condición") # Reterna un True, ya que la "opcion" es verdadera

opcion1  = False
if opcion1:
    print ("No se cumple la condición") # No reterna nada, ya que la "opcion1" es fasla

n = 5
if n == 5:
    print ("N es igual a 5")

# Anidar If dentro de If:
a = 5
b = 10
if a == 5:
    print("a vale",a)
    if b == 10:
        print("y b vale",b)

# Como condición podemos evaluar múltiples expresiones, siempre que éstas devuelvan True o False:
if a==5 and b == 10:
    print("a vale 5 y b vale 10")
