# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

print('Su nombre y apellido es:', nombre , apellido)

# Almacenar su nombre completo en una variable
# nombre_completo = .....

nombre_completo = nombre + ' ' + apellido


# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)

nombre = nombre_completo.split(' ')
cantidad_espacios = len(nombre) - 1
cantidad_letras = len(nombre_completo)

print('La cantidad de letras que posee su nombre completo es:', cantidad_letras - cantidad_espacios) # -1 por el espacio entre nombre y  apellido

