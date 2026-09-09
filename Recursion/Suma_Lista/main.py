# Programa: Suma de los elementos de una lista.
# Descripción general: Obtiene la suma de una lista predefinida mediante dos
# métodos de solución: recorrido recursivo y recorrido iterativo con un ciclo for.
lista =  [1, 2, 3, 5, 6, 3, 90, 89, 5, 7]

longitud = len(lista)

# Suma recursivamente el elemento ubicado en longitud - 1 y reduce la longitud
# en cada llamada hasta alcanzar el caso base.
def sumaListaRecursion(longitud):
    if longitud == 1:
        return 1
    return lista[longitud-1]+sumaListaRecursion(longitud-1)

# Recorre la lista desde el primer elemento hasta la longitud indicada y
# acumula el valor de cada posición en la variable suma.
def sumaListaFor(longitud):
    suma = 0
    for i in range (0, longitud):
        suma += lista[i]
    return suma

print("Recursion: ", sumaListaRecursion(longitud))

print("Ciclo For: ", sumaListaFor(longitud))
