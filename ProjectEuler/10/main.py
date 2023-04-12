def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

n = 2000000
somma = 2
for i in range(3, n, 2):
    if is_prime(i):
        somma += i
print(somma)