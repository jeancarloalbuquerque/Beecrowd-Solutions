"""
Bloco: 6 - Paradigmas
Problema: Fibonacci, Quantas Chamadas?
Autor: Neilor Tonin

Resolução: Jean Carlo de Albuquerque

"""

def fib(num):
    global calls 
    calls += 1

    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fib(num-1) + fib(num-2)

n = int(input())

for i in range(n):
    num = int(input())
    
    calls = 0
    result = fib(num)

    print(f'fib({num}) = {calls-1} calls = {result}')