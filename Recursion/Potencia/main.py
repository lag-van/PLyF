# Programa: Cálculo de la potencia de un número.
# Descripción general: Solicita una base y un exponente, y calcula la potencia
# mediante dos métodos de solución: un ciclo for y una función recursiva.

base = int(input("Base: "))
potencia = int(input("Potencia: "))

# Calcula la potencia de forma iterativa, multiplicando la base tantas veces
# como indique el exponente.
def potenciaFor(base, potencia):
    resultado=1
    for i in range (0, potencia):
        resultado *= base
    return resultado

# Calcula la potencia reduciendo el exponente en cada llamada recursiva.
# El exponente igual a cero es el caso base y devuelve el elemento neutro 1.
def potenciaRecursion(base, potencia):
    if potencia == 0:
        return 1
    return base*potenciaRecursion(base, potencia-1)

print("Ciclo For: ", potenciaFor(base, potencia))
print("Recursion: ", potenciaRecursion(base, potencia))
