try:
    n = None
    if n is None:
        # print ('Error. No se permite un valor None')
        raise ValueError('Error. No se permite un valor None') # Invocacion de excepcion, cambiando el mensaje de error
except ValueError:
    print('Error. No se permite un valor None (desde la excepción)')
