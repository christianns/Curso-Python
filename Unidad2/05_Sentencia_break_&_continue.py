# la sentencia break sirva para romper o detener una sentencia o ejecucion del while:
# La sentencia continue sirve para seguir ejecutandose

# break
opcion = 0
while opcion <= 10:
    print (opcion)
    if opcion == 5:
       break
    opcion += 1
else:
    print ("Termina el ciclo while")

# continue
opcion1 = 0
while opcion1 < 10:
    opcion1 += 1
    if opcion1 == 5:
        print("Estas en el numero",opcion1)
#        break
        continue
    print (opcion1)
else:
    print ("Termina el ciclo while")
