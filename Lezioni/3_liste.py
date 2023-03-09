# def somma(lista):
#     totale = 0
#     for numero in lista:
#         totale += numero
#     return totale

# numbers = range(1,3)
# print(list(numbers))
# print(somma(numbers))

# def maiuscole(strings):
#     result = list()
#     for string in strings:
#         result.append(string.capitalize())
#     return result

# strings = ['ciao', 'a', 'tutti']
# print(maiuscole(strings))

def solo_maiuscole(t):
    result = list()
    for string in strings:
        if string.isupper():
            result.append(string)
    return result

strings = ['Ciao', 'A', 'Tutti', 'VOI']
print(solo_maiuscole(strings))