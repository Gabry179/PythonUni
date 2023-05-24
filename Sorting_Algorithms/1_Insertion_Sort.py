def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while lista[j-1] > lista[j] and j > 0:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista

list = [2, 6, 5, 1, 3, 4]
print(insertion_sort(list))