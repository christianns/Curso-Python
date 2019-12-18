# Se crean 2 conjuntos usuarios y administradores.
usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marta'}
print (usuarios)
print (administradores)

# Se quita Juan de administradores (si el elemento no existe indicara un error)
administradores.remove('Juan')
print (administradores)

# Se quita Juan de administradores (solo en casa de que exista)
administradores.discard('Marta')

# Agregar a Marcos y Marta a administradores sin quitar de usuarios
administradores.add('Marcos')
administradores.add('Marta')
print (administradores)

for user in usuarios:
    if user in administradores:
        print(user, "es un administrador")
    else:
        print(user, 'no es un administrador')
