#Calcula el MCD con el algoritmo de Euclides mediante ciclo for y recursion

dividendo = int(input("Dividendo (mayor): "))
divisor = int(input("Divisor (menor): "))

#Por medio de recursion
def mcdRecursion(dividendo, divisor):
    if dividendo == 0:
        return divisor
    if divisor == 0:
        return dividendo
    return mcdRecursion(divisor, (dividendo%divisor))

##Por medio de ciclo for
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
