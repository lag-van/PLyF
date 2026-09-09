# Programa: Cálculo del factorial de un número.
# Descripción general: Solicita una base y calcula su factorial para comparar
# dos métodos de solución: uno iterativo mediante un ciclo for y otro recursivo.
base = int(input("Base: "))


# Calcula el factorial de la base de forma iterativa, acumulando en resultado
# el producto de los números enteros desde 1 hasta base - 1.
# @param base: Número entero cuyo factorial se desea calcular.
# @return: Factorial de la base calculado mediante un ciclo for.
def factorialFor(base):
    resultado=base
    for i in range (1,base):
        resultado *= i
    return resultado

# Calcula el factorial mediante una llamada recursiva para reducir el problema.
# El caso base detiene las llamadas cuando la base llega a 1.
# @param base: Número entero cuyo factorial se desea calcular.
# @return: Resultado del cálculo recursivo del factorial.
def factorialRecursion(base):
    if base == 1:
        return 0
    return base*factorialFor(base-1)

print("Factorial For: ", factorialFor(base))
print("Factorial Recursion: ", factorialRecursion(base))
