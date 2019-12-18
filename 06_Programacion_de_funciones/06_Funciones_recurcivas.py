# Funciones recursivas, estas funciones se 'llaman' asimismas.

# Ejemplo 1 de una funcion recursiva.
def cuenta_regresiva (n):
    n -= 1
    if n > 0:
        print (n)
        cuenta_regresiva(n)
    else:
        print ('Booom ¡¡¡¡¡¡¡¡¡¡')
cuenta_regresiva(3)

# Ejemplo 2 de una funcion recursiva
def factorial(num):
    print ('Valor inicial -->', num)
    if num > 1:
        num = num * factorial(num - 1)
    print ('valor final -->', num)
    return num
print(factorial(5))
