import math

def calc_factorial(x, n):
    if n == 1:
       return n
    else:
        return n*calc_factorial(x,n-1)

def series(x, n):
    print("Il valore di n deve essere maggiore o uguale a 1")
    if n < 1:
        return -1
    else:
        somma = 0
        for i in range(1, n+1):
            somma += (math.pow(x, i-1)) / calc_factorial(i+1, n)
    print(somma)

series(25, 5)