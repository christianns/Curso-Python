'''
Ejercicio 1
Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
'''

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
