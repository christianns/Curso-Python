# Argumentos y parametros

def resta (x, y): # Se define como parametros a x e y. Se utilizan para recibir algun valor.
    r = x - y
    return r
r = resta(10, 5) # Se define como argumentos a los valores envidados.

print (r)
print (resta (45, 103))
print (resta(x = 12, y = 8)) # Argumentos por nombre
print (resta(y = 8, x = 12)) # Argumentos por nombre
