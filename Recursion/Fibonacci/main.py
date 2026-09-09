# Programa: Cálculo del factorial de un número.
# Descripción general: Calcula el factorial de un valor fijo y compara dos
# métodos de solución: recursión y acumulación iterativa mediante un ciclo for.

# Calcula el factorial reduciendo n en cada llamada recursiva.
# El caso base n == 1 finaliza la recursión y permite acumular los productos.
# @param n: Número entero cuyo factorial se desea calcular.
# @return: Factorial de n calculado recursivamente.
def fact_rec(n):
    if n == 1:
        return 1
    return n*fact_rec(n-1)

print ("Recursion: ", fact_rec(3))

# Calcula el factorial de manera iterativa, multiplicando todos los enteros
# comprendidos entre 1 y n en la variable resultado.
# @param n: Número entero cuyo factorial se desea calcular.
# @return: Factorial de n calculado mediante un ciclo for.
def fact_for(n):
    resultado = 1
    for i in range (1,n+1):
        resultado *= i
    return resultado

print ("Ciclo For: ", fact_for(3))
    
