# Instrucción break: Sirve para "romper" la ejecución del While en cualquier momento.
# No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.

# break - Ejemplo 1
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)

# break - Ejemplo 2

opcion = 0
while opcion <= 10:
    print (opcion)
    if opcion == 5:
       break
    opcion += 1
else:
    print ("Termina el ciclo while")

# Instrucción continue
# Sirve para "saltarse" la iteración actual sin romper el bucle.

c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteración", c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)

# Ejemplo 3 - Menu interactivo

print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
