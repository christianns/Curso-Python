# Las excepciones son bloque de codigos que nos permite continuar con el programa a pesar de que
# se encuentre un error (funcion try:)

# Ejemplo 1

while True:
    try:
        n = float(input('Introduzca un numero:\n')) # Si se ingresa una letra, este codigo genera un error
        print (n + 5)
        # break --> este break permite terminar el programa, pero queda mejor después del else
    except:
        print ('Se detecto un error, por favor ingresar un número') # Esto se ejecuta solo cuando se detecta un error
    else:
        print ('Todo funciona correctamente')
        break
    finally:
        print ('Fin de la iteración')
