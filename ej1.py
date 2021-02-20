# Ejercicio 1

# Todas las variables y funciones son con snake_case
# Todas las clases son camel case
# Todo el código va comentado
# El hombre de las variables, funciones, clases tiene que ser legible

# Crear una función que reciba un número como argumenta y devuelva el largo de este número.

# Ejemplo
# number_length(10) -> 2
# number_length(1000) -> 5
# number_length(4321) -> 4

# Restricciones
# El número no puede ser negativo
# El número que se manda a la función tiene que ser de tipo INT
# No se puede utilizar el método length

def number_length(number):
    if isinstance(number, str):
        return 'Error'
    counter = 0
    for i in str(number):
        counter += 1
    return counter

number_length(10)