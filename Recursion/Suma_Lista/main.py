lista =  [1, 2, 3, 5, 6, 3, 90, 89, 5, 7]

longitud = len(lista)

#Suma de elementos de una lista con recursion
def sumaListaRecursion(longitud):
    if longitud == 1:
        return 1
    return lista[longitud-1]+sumaListaRecursion(longitud-1)

#suma de elementos de una lista con ciclo for
def sumaListaFor(longitud):
    suma = 0
    for i in range (0, longitud):
        suma += lista[i]
    return suma

print("Recursion: ", sumaListaRecursion(longitud))

print("Ciclo For: ", sumaListaFor(longitud))