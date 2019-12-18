# Este ejemplo pide ingresar algun dato desde el teclado
# input solo puede leer cadena de texto (aunque se numeros)
# luego se almacena en la variable nombre
nombre = input("Ingrese nombre:")
print(nombre)
edad = input("Ingrese edad:")
print(edad,type(edad))
# len(str) mustra la cantidad de caracteres del string
print("Tu nombre tiene " + str(len(nombre)) + " letras")
