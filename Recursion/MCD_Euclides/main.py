# Programa: Cálculo del máximo común divisor (MCD).
# Descripción general: Solicita dos números y aplica el algoritmo de Euclides
# mediante dos métodos de solución: recursión y repetición con un ciclo for.

dividendo = int(input("Dividendo (mayor): "))
divisor = int(input("Divisor (menor): "))

# Aplica recursivamente el algoritmo de Euclides, reemplazando cada par de
# valores por el divisor y el residuo hasta que uno de ellos sea cero.
# @param dividendo: Primer número entero utilizado en el algoritmo.
# @param divisor: Segundo número entero utilizado para obtener el residuo.
# @return: Máximo común divisor de los dos números.
def mcdRecursion(dividendo, divisor):
    if dividendo == 0:
        return divisor
    if divisor == 0:
        return dividendo
    return mcdRecursion(divisor, (dividendo%divisor))

# Aplica el algoritmo de Euclides de forma iterativa. En cada vuelta actualiza
# simultáneamente el dividendo y el divisor, y termina cuando el divisor es cero.
# @param dividendo: Primer número entero utilizado en el algoritmo.
# @param divisor: Segundo número entero utilizado para obtener el residuo.
# @return: Máximo común divisor de los dos números.
def mcdFor(dividendo, divisor):
    if divisor == 0:
        return dividendo
    for _ in range(divisor + 1):
        if divisor == 0:
            return dividendo
        dividendo, divisor = divisor, dividendo % divisor

    return dividendo


print("MCD recursion: ", mcdRecursion(dividendo, divisor))
print("MCD for: ", mcdFor(dividendo, divisor))
