#El siguiente programa maneja la estructura de Fibonacci por medio de recursión y por medio de un ciclo FOR.

#Por recursión
def fact_rec(n):
    if n == 1:
        return 1
    return n*fact_rec(n-1)

print ("Recursion: ", fact_rec(3))

#Por medio de un ciclo FOR
def fact_for(n):
    resultado = 1
    for i in range (1,n+1):
        resultado *= i
    return resultado

print ("Ciclo For: ", fact_for(3))
    
