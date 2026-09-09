#Calcula la potencia por medio de Ciclo for y recursion

base = int(input("Base: "))
potencia = int(input("Potencia: "))

#Usando ciclo For
def potenciaFor(base, potencia):
    resultado=1
    for i in range (0, potencia):
        resultado *= base
    return resultado

#Usando recursion
def potenciaRecursion(base, potencia):
    if potencia == 0:
        return 1
    return base*potenciaRecursion(base, potencia-1)

print("Ciclo For: ", potenciaFor(base, potencia))
print("Recursion: ", potenciaRecursion(base, potencia))