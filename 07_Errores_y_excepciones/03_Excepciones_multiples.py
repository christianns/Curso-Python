#
while True: # repite el bucle hasta que se false
    try:
        n = float(input('Introduzca un numero:\n'))# Para solucionar se puede colocar float o int
        print (5 / n)
    except TypeError:
        print ('No se puede dividir el numero con una cadena')
    except ValueError:
        print ('Debe ingresar un numero')
    except ZeroDivisionError:
        print ('No se puede dividir por cero, intente con otro numero')
    except Exception as e: # Guarda la excepcion como una variable
        print ('Ha ocurrido un error =>', type(e).__name__)
    else:
        print('Todo funciona correctamente')
