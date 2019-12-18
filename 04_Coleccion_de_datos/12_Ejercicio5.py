# Ejercicio 6
# Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
#  Al parecer contiene el nombre de un alumno y la nota de un exámen.
# ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

print ('<nombre apellido> ha sacado un Nota de <nota>.')

cadena = "zeréP nauJ,01"
cadena_volteada = cadena[::-1] # Escribe la cadena al revés
print (cadena_volteada)
print(cadena_volteada[3:], "ha sacado un", cadena_volteada[:2], "de nota.")
