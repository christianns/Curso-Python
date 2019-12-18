# Funciones integradas

# Funcion int()
n = int('10')
print (n)

# Funcion float()
f = float('10.5')

# Funcion str() , string
c = 'Un texto y dos números ' + str(10) + ' y ' + str(3.14)
print (c)

# Convertir numero decimal a binario bin()
print (bin(256))

# Convertir numero decimal a hexadecimal hex()
print (hex(100))

# Converir un numero hexadecimal y binario a hexadecimal
print (int(0b100000000)) # Opcion 1, con numero binario
print (int('100000000', 2)) # Opcion 2, con numero binario mas base.

print (int(0x64))
print (int('64', 16))

# Funcion absoluto
print (abs(-10))

# Funcion round(), redondea el valar
print(round(15.5))
print(round(15.4))

# Funcion eval()
print (eval('2 + 5'))

n = 10
print (eval('n * 10 - 5'))

help() # Ayuda
