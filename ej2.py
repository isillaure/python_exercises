# Ejercicio 2

# Crear una función que reciba dos números como argumentos (número, longitud) y devolver una lista con los múltiplos del número dada la longitud.

# Ejemplo
# list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
# list_of_multiples(17, 6) -> [17, 34, 51, 68, 85, 102]

# Restricciones 
# Los argumentos no pueden ser negativos.
# Los argumentos deben ser enteros.

def list_exponents(base, power):
    if not isinstance(base, int) and isinstance(power, int):
        return 'Error'
    if base < 0 or power < 0:
        return 'Error'
    result = [base * power for power in range(1, power + 1)]
    return result

list_exponents(10, 5)
