'''
Argumentos y parámetros
En la definición de una función los valores que se reciben se denominan parámetros,
pero durante la llamada los valores que se envían se denominan argumentos.
'''

# Argumentos por posición
# Cuando enviamos argumentos a una función, estos se reciben por orden en los
# parámetros definidos. Se dice por tanto que son argumentos por posición:

def resta (x, y): # Se define como parametros a x e y. Se utilizan para recibir algun valor.
    r = x - y
    return r
r = resta(10, 5) # argumento 10 => posición 0 => parámetro x
                 # argumento 5  => posición 1 => parámetro y

print (r)
print (resta (45, 103))

# Argumentos por nombre
# Sin embargo es posible evadir el orden de los parámetros si indicamos durante
# la llamada que valor tiene cada parámetro a partir de su nombre:

print (resta(x = 12, y = 8)) # Argumentos por nombre
print (resta(y = 8, x = 12)) # Argumentos por nombre

# Llamada sin argumentos
# Al llamar una función que tiene definidos unos parámetros,
# si no pasamos los argumentos correctamente provocará un error:

# resta()

# Parámetros por defecto
# Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros,
# de esa forma podríamos hacer una comprobación antes de ejecutar el código de la función:
def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return   # indicamos el final de la función aunque no devuelva nada
    return a-b

resta()
