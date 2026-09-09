#calcula el factorial de un numero con funciones de recursion y ciclo for
base = int(input("Base: "))


#calculo del factorial por medio de ciclo for
def factorialFor(base):
    resultado=base
    for i in range (1,base):
        resultado *= i
    return resultado

#calculo del factorial por medio de recursion
def factorialRecursion(base):
    if base == 1:
        return 0
    return base*factorialFor(base-1)

print("Factorial For: ", factorialFor(base))
print("Factorial Recursion: ", factorialRecursion(base))